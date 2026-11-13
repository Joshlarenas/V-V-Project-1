import os
import random
from dataclasses import dataclass
from typing import Optional

import cocotb
import vsc
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, RisingEdge, Timer
from cocotb_coverage.coverage import CoverPoint, CoverCross, coverage_db

from models.fifo_model import FifoModel

WIDTH = 8
DEPTH = 8
SEED = 1
CYCLES = 10000

def op_bin(wr, rd):
    if wr and rd:
        return "rw"
    if wr:
        return "write"
    if rd:
        return "read"
    return "idle"


def occ_bin(cnt):
    if cnt == 0:
        return "empty"
    if cnt == DEPTH:
        return "full"
    return "partial"


@CoverPoint("fifo.occ", xf=lambda cnt, wr, rd: cnt, bins=list(range(DEPTH + 1)))
@CoverPoint("fifo.op", xf=lambda cnt, wr, rd: op_bin(wr, rd),
            bins=["idle", "write", "read", "rw"])
@CoverCross("fifo.occ_x_op", items=["fifo.occ", "fifo.op"])
def sample_cov(cnt, wr, rd):
    pass


@CoverPoint("fifo.rst_occ", xf=lambda cnt, wr: occ_bin(cnt),
            bins=["empty", "partial", "full"])
@CoverPoint("fifo.wr_during_rst", xf=lambda cnt, wr: wr, bins=[0, 1])
@CoverCross("fifo.rst_occ_x_wr", items=["fifo.rst_occ", "fifo.wr_during_rst"])
def sample_rst_cov(cnt, wr):
    pass


@CoverPoint("fifo.wr_pos", xf=lambda wpos, rpos: wpos, bins=list(range(DEPTH)))
@CoverPoint("fifo.rd_pos", xf=lambda wpos, rpos: rpos, bins=list(range(DEPTH)))
def sample_ptr_cov(wpos, rpos):
    pass


class FifoDriver:

    def __init__(self, dut, period_ns=10):
        self.dut = dut
        cocotb.start_soon(Clock(dut.clk, period_ns, units="ns").start())

    async def reset(self, cycles=3):
        self.dut.wr_en.value = 0
        self.dut.rd_en.value = 0
        self.dut.wr_data.value = 0
        self.dut.rst_n.value = 0
        for _ in range(cycles):
            await RisingEdge(self.dut.clk)
        self.dut.rst_n.value = 1

    async def cycle(self, wr_en, rd_en, wr_data=0, rst=0):
        await FallingEdge(self.dut.clk)
        self.dut.rst_n.value = 0 if rst else 1
        self.dut.wr_en.value = wr_en
        self.dut.rd_en.value = rd_en
        self.dut.wr_data.value = wr_data
        await RisingEdge(self.dut.clk)
        await Timer(1, units="ns")


@dataclass
class ObservedState:
    cycle: int
    wr_en: int
    rd_en: int
    wr_data: int
    count: int
    full: bool
    empty: bool
    rd_data: Optional[int]
    rst: bool


class FifoMonitor:

    def __init__(self, dut):
        self.dut = dut
        self.cycle = 0

    def capture(self):
        self.cycle += 1
        return ObservedState(
            self.cycle,
            int(self.dut.wr_en.value),
            int(self.dut.rd_en.value),
            int(self.dut.wr_data.value),
            int(self.dut.count.value),
            bool(self.dut.full.value),
            bool(self.dut.empty.value),
            None if bool(self.dut.empty.value) else int(self.dut.rd_data.value),
            not bool(self.dut.rst_n.value),
        )


def hx(v):
    return "--" if v is None else f"0x{v:02X}"


class FifoScoreboard:

    def __init__(self):
        self.model = FifoModel(WIDTH, DEPTH)
        self.checked = 0

    def reset(self):
        self.model.reset()

    def update(self, obs):
        if obs.rst:
            self.model.reset()
        else:
            self.model.step(obs.wr_en, obs.wr_data, obs.rd_en)

        if not (
            obs.count == self.model.count and obs.full == self.model.full
            and obs.empty == self.model.empty
            and (self.model.empty or obs.rd_data == self.model.head)
        ):
            cocotb.log.error(
                f"first divergence: cycle {obs.cycle} -- "
                f"count {obs.count} vs model {self.model.count}, "
                f"full {int(obs.full)} vs {int(self.model.full)}, "
                f"empty {int(obs.empty)} vs {int(self.model.empty)}, "
                f"rd_data {hx(obs.rd_data)} vs head {hx(self.model.head)} | "
                f"pins that cycle: rst={int(obs.rst)} wr_en={obs.wr_en} rd_en={obs.rd_en} "
                f"wr_data={hx(obs.wr_data)}"
            )

        assert obs.count == self.model.count, f"cycle {obs.cycle}: count {obs.count} != model {self.model.count}"
        assert obs.full == self.model.full, f"cycle {obs.cycle}: full {obs.full} != model {self.model.full}"
        assert obs.empty == self.model.empty, f"cycle {obs.cycle}: empty {obs.empty} != model {self.model.empty}"
        if not self.model.empty:  # FWFT: head valid only when not empty
            assert obs.rd_data == self.model.head, f"cycle {obs.cycle}: rd_data {hx(obs.rd_data)} != head {hx(self.model.head)}"

        self.checked += 1


class FifoTester:

    def __init__(self, dut):
        self.driver = FifoDriver(dut)
        self.monitor = FifoMonitor(dut)
        self.scoreboard = FifoScoreboard()

    async def reset(self):
        await self.driver.reset()
        self.scoreboard.reset()

    async def step(self, wr_en, rd_en, wr_data=0, rst=0):
        await self.driver.cycle(wr_en, rd_en, wr_data, rst)
        state = self.monitor.capture()
        self.scoreboard.update(state)


@cocotb.test()
async def test_crv(dut):
    from crv.seeded_regression import run_crv
    await run_crv(dut, FifoTester, sample_cov, sample_rst_cov, sample_ptr_cov, coverage_db, DEPTH, SEED, CYCLES)
