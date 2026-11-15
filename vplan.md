# Verification plan — FIFO

**Author:** Caleb Allen, Josh Larenas **Spec version:** 1 **Date:** 11/13/2026

> A vplan is an argument that "done" is definable before you write tests. Every
> row here should be something you could defend in a signoff meeting. Rows you
> cannot defend are the honest content of the Risk section, not omissions.

## 1. Scope

**In scope:** This plan claims to verify that the dut meets the functional requirements of the design spec.
**Out of scope:** This plan does not claim to test if the requirements themselves are correct for making a functioning fifo.
**Assumptions about the environment:** Assumes the golden model is correct and adheres to the spec.

## 2. Feature list

One row per behavior the spec requires. `Req` cites a line or section of the
spec — if you cannot cite one, that is a spec gap and it belongs in section 5.

| ID | Feature | Req | Priority | How it is verified |
|----|---------|-----|----------|--------------------|
| F1 | Reset | while `rst_n==0`, on the next clock edge `count→0`, `empty=1`, `full=0` | H | CRV |
| F2 | Write | a write occurs iff `wr_en && !full`. A write asserted while `full` is **dropped** (no overflow, no corruption) | H | CRV |
| F3 | Read | a read occurs iff `rd_en && !empty`. A read asserted while `empty` is **ignored** (no underflow). `rd_data` continuously shows the current head | H | CRV |
| F4 | Simultaneous read+write | both happen on the same edge and `count` is **unchanged** | H | CRV |
| F5 | Flags | `full == (count==DEPTH)`, `empty == (count==0)` at all times | H | CRV |
| F6 | Ordering | strictly first-in-first-out | H | CRV |

## 3. Coverage model

Coverpoints and their bins. A cross earns its place only if the interaction is
where a bug would hide — say which bug.

| ID | Coverpoint | Bins | Why these bins |
|----|-----------|------|----------------|
| C1 | Fifo occupancy | 0-8 | Tests all occupancy levels of the fifo. |
| C2 | Fifo operation | idle, read, write, simultaneous read & write | Tests all possible fifo operations. |
| C3 | Reset & occupancy | empty, partial, full | Tests reset at different occupancy levels. |
| C4 | Write during reset | 0, 1 | Tests write during reset. |
| C5 | Write wrap | 1 | Testing that a write wrap occurred. |
| C6 | Read wrap | 1 | Testing that a read pointer wrap occurred. |

**Crosses**

| ID | Cross | The interaction it is aimed at |
|----|-------|-------------------------------|
| X1 | occ_x_op | Testing operations at different levels of occupancy |

**Illegal / ignore bins:** Wrap before max occupancy. Pointer wrap can only occur once the number of elements in the fifo has exceeded the depth of the fifo.

## 4. Test matrix

Every feature maps to at least one test; every test traces back to a feature.
An untraceable test is a test nobody can defend.

| Test | Features | Kind | Pass criterion |
|------|----------|------|----------------|
| test_crv | F1, F2, F3, F4, F5, F6 | random | All required coverage bins hit and scoreboard checks pass |

## 5. Risk and spec ambiguity

| # | Ambiguity or risk | Where in the spec | How I resolved it | Residual |
|---|-------------------|-------------------|-------------------|----------|
| 1 | Read during reset, does reset take place first? | Not listed | tested and assumed that reset occurs immediately | N/A |

## 6. Closure criteria

State the numbers *before* you start, so closure is a measurement and not a
negotiation.

- Functional coverage target: **100%** of the model in section 3
- Mutation target: **15/20** on the hidden pool
- Assertions: every property paired with a passing `cover` (no vacuous passes)
- What I will report as **not verified**: This plan only covers the functionality of the fifo and not the actual values of the inputs. Exhaustive testing would include tests for every possible value that could be put into the fifo.
