# AI LOG — Project 1 · Joshua Larenas & Calleb Allen

## AI Prompt

**What AI was asked to generate:** Coverage model / Constraints

**Prompt used:**

```text
I am working on a project for my Verification and Validation class involving a synchronous FIFO using Python and 
cocotb. I would like help creating a functional coverage model using the `cocotb-coverage` library. The goal is 
to develop coverpoints and crosses that track different FIFO conditions, including occupancy levels (empty, 
partial, full), read and write operations, simultaneous reads and writes, reset behavior, and pointer positions.
Please keep the implementation simple and organized so that it can be integrated into our existing `test_fifo.py` 
without requiring major changes to the current testbench. Include any additional coverpoints or crosses that would 
be useful for verifying the FIFO, and briefly explain the purpose of each one.If any part of the implementation 
depends on the FIFO specification, please identify it rather than making assumptions.
```

## Prediction

What we expected might be incorrect or missing before running the code.

1. We predict that the used AI may miss necessary coverpoints or crosses, especially the FIFO boundary conditions.
2. The genearted code may give issues initially pairing with our already created testing files, causing inconsistencies and maybe even some redundancy.

## Testing and Evidence

**Command run:**

```bash
just test fifo_crv icarus
```

| What we tested | Expected result | Actual result |
|----------------|-----------------|---------------|
|                Coverage Code Integration|                Code runs into compatibility errors |               Test failed due to NameError: name 'dut' is not defined|
|                Functional coverage collection|                 Coverpoints record FIFO operations and occupancy|               Unable to test|
|                Coverage Crosses|                 Different combinations of occupancy and operations are recorded|               Unable to test|

## Fixes and Adjustments

| Issue found | Change made | Result after fix |
|-------------|-------------|------------------|
|             Coverage Code integration wasn't able to be compatible on first run|             We adjusted the coverage code to work properly with our testbench by fixing the reset settings, signal timing, and coverage reporting. We also added resets while the FIFO had data and tested read/write operations during reset, allowing us to reach 100% functional coverage.|                  After making these adjustments, the testbench successfully ran and achieved 93.5% functional coverage (43/46 bins). The only remaining issue was three missing coverage bins involving read and write operations during reset.|
|After Integration fix, our test output missed 3 out 46 bins. It was the missing coverage bins for read and write during reset.            |             The remaining coverage bins were missing because read and write operations were not being tested during reset. We fixed this by adding those operations during reset, which allowed us to reach 100% functional coverage.|                  After making these fixes, the testbench successfully passed all 2,000 cycles and achieved 100% functional coverage (76/76 bins), with no failures.|

## Final Verdict

**What worked:** The AI-generated coverage model successfully tracked FIFO operations, occupancy, resets, and pointer behavior. After making adjustments, we achieved 100% functional coverage (76/76 bins).

**What did not work:** The original code had compatibility issues with our testbench and missed certain reset conditions, requiring additional changes, hitting 43/46 orignal bins.

**Remaining limitations:** Although we achieved 100% functional coverage, this does not guarantee that every possible FIFO fault can be detected.

**If we had another day:** We would run additional seeds and expand our testing to cover more scenarios and improve our chances of detecting faults.
