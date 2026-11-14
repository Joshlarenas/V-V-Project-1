import random

from crv.transactions import FifoTxn


async def run_crv(dut, FifoTester, sample_cov, sample_rst_cov, sample_wrap_cov, coverage_db, DEPTH, SEED, CYCLES):
    tester = FifoTester(dut)
    await tester.reset()

    random.seed(SEED)
    txn = FifoTxn()
    writes = 0
    reads = 0

    for _ in range(CYCLES):
        count = tester.scoreboard.model.count
        txn.count = count
        txn.randomize()
        wr, rd, rst = int(txn.wr_en), int(txn.rd_en), int(txn.rst)

        if rst:
            sample_rst_cov(count, wr)
            writes = reads = 0
        else:
            sample_cov(count, wr, rd)
            sample_wrap_cov(int(writes >= DEPTH), int(reads >= DEPTH))
            if wr and count < DEPTH:
                writes += 1
            if rd and count > 0:
                reads += 1

        await tester.step(wr, rd, int(txn.wr_data), rst)

    dut._log.info(f"seed {SEED}, {CYCLES} cycles, {tester.scoreboard.checked} checked")
    coverage_db.report_coverage(dut._log.info, bins=True)
    for name in ("fifo.occ_x_op", "fifo.wr_wrapped", "fifo.rd_wrapped", "fifo.rst_occ", "fifo.wr_during_rst"):
        pct = coverage_db[name].cover_percentage
        assert pct == 100, f"seed {SEED}: {name} only {pct:.1f}% covered"
