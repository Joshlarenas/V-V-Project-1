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

**Initial Output:**
```bash
 just test fifo_crv icarus
make -C tb/fifo_crv SIM=icarus
make: Entering directory '/home/wraps03/Fall2026/craft-vv-student/code/tb/fifo_crv'
rm -f results.xml
"make" -f Makefile results.xml
make[1]: Entering directory '/home/wraps03/Fall2026/craft-vv-student/code/tb/fifo_crv'
rm -f results.xml
MODULE=test_fifo TESTCASE= TOPLEVEL=fifo TOPLEVEL_LANG=verilog \
         /usr/bin/vvp -M /home/wraps03/.venv/craft-vv/lib/python3.12/site-packages/cocotb/libs -m libcocotbvpi_icarus   sim_build/sim.vvp
     -.--ns INFO     gpi                                ..mbed/gpi_embed.cpp:108  in set_program_name_in_venv        Using Python virtual environment interpreter at /home/wraps03/.venv/craft-vv/bin/python
     -.--ns INFO     gpi                                ../gpi/GpiCommon.cpp:101  in gpi_print_registered_impl       VPI registered
     0.00ns INFO     cocotb                             Running on Icarus Verilog version 12.0 (stable)
     0.00ns INFO     cocotb                             Running tests with cocotb v1.9.2 from /home/wraps03/.venv/craft-vv/lib/python3.12/site-packages/cocotb
     0.00ns INFO     cocotb                             Seeding Python random module with 1794619978
     0.00ns CRITICAL cocotb.regression                  Failed to import module test_fifo: name 'dut' is not defined
     0.00ns INFO     cocotb.regression                  MODULE variable was "test_fifo"
     0.00ns INFO     cocotb.regression                  Traceback (most recent call last):
                                                          File "/home/wraps03/.venv/craft-vv/lib/python3.12/site-packages/cocotb/regression.py", line 203, in _discover_tests
                                                            module = _my_import(module_name)
                                                                     ^^^^^^^^^^^^^^^^^^^^^^^
                                                          File "/home/wraps03/.venv/craft-vv/lib/python3.12/site-packages/cocotb/regression.py", line 72, in _my_import
                                                            mod = __import__(name)
                                                                  ^^^^^^^^^^^^^^^^
                                                          File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
                                                          File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
                                                          File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
                                                          File "/home/wraps03/.venv/craft-vv/lib/python3.12/site-packages/_pytest/assertion/rewrite.py", line 188, in exec_module
                                                            exec(co, module.__dict__)
                                                          File "/home/wraps03/Fall2026/craft-vv-student/code/tb/fifo_crv/test_fifo.py", line 254, in <module>
                                                            cocotb.start_soon(cov.monitor(dut))
                                                                                          ^^^
                                                        NameError: name 'dut' is not defined

     0.00ns ERROR    cocotb                             name 'dut' is not defined
ERROR: results.xml was not written by the simulation!
make[1]: *** [/home/wraps03/.venv/craft-vv/lib/python3.12/site-packages/cocotb/share/makefiles/simulators/Makefile.icarus:96: results.xml] Error 1
make[1]: Leaving directory '/home/wraps03/Fall2026/craft-vv-student/code/tb/fifo_crv'
make: *** [/home/wraps03/.venv/craft-vv/lib/python3.12/site-packages/cocotb/share/makefiles/Makefile.inc:40: sim] Error 2
make: Leaving directory '/home/wraps03/Fall2026/craft-vv-student/code/tb/fifo_crv'
error: Recipe `test` failed on line 24 with exit code 2
```

## Fixes and Adjustments

| Issue found | Change made | Result after fix |
|-------------|-------------|------------------|
|             Coverage Code integration wasn't able to be compatible on first run|             We adjusted the coverage code to work properly with our testbench by fixing the reset settings, signal timing, and coverage reporting. We also added resets while the FIFO had data and tested read/write operations during reset, allowing us to reach 100% functional coverage.|                  After making these adjustments, the testbench successfully ran and achieved 93.5% functional coverage (43/46 bins). The only remaining issue was three missing coverage bins involving read and write operations during reset.|
|After Integration fix, our test output missed 3 out 46 bins. It was the missing coverage bins for read and write during reset.            |             The remaining coverage bins were missing because read and write operations were not being tested during reset. We fixed this by adding those operations during reset, which allowed us to reach 100% functional coverage.|                  After making these fixes, the testbench successfully passed all 2,000 cycles and achieved 100% functional coverage (76/76 bins), with no failures.|

**Final Output:**
```bash
just test fifo_crv icarus
make -C tb/fifo_crv SIM=icarus
make: Entering directory '/home/wraps03/Fall2026/craft-vv-student/code/tb/fifo_crv'
rm -f results.xml
"make" -f Makefile results.xml
make[1]: Entering directory '/home/wraps03/Fall2026/craft-vv-student/code/tb/fifo_crv'
rm -f results.xml
MODULE=test_fifo TESTCASE= TOPLEVEL=fifo TOPLEVEL_LANG=verilog \
         /usr/bin/vvp -M /home/wraps03/.venv/craft-vv/lib/python3.12/site-packages/cocotb/libs -m libcocotbvpi_icarus   sim_build/sim.vvp
     -.--ns INFO     gpi                                ..mbed/gpi_embed.cpp:108  in set_program_name_in_venv        Using Python virtual environment interpreter at /home/wraps03/.venv/craft-vv/bin/python
     -.--ns INFO     gpi                                ../gpi/GpiCommon.cpp:101  in gpi_print_registered_impl       VPI registered
     0.00ns INFO     cocotb                             Running on Icarus Verilog version 12.0 (stable)
     0.00ns INFO     cocotb                             Running tests with cocotb v1.9.2 from /home/wraps03/.venv/craft-vv/lib/python3.12/site-packages/cocotb
     0.00ns INFO     cocotb                             Seeding Python random module with 1794621056
     0.00ns INFO     cocotb.regression                  Found test test_fifo.test_crv
     0.00ns INFO     cocotb.regression                  running test_crv (1/1)
     0.00ns INFO     cocotb.fifo                        Pointer coverage: using wr_ptr / rd_ptr
/home/wraps03/.venv/craft-vv/lib/python3.12/site-packages/vsc/model/field_scalar_model.py:93: DeprecationWarning: __int__ returned non-int (type ValueInt).  The ability to return an instance of a strict subclass of int is deprecated, and may be removed in a future version of Python.
  self.val.v = int(val)
    25.00ns INFO     cocotb                             Starting CRV test with seed 12345
/home/wraps03/.venv/craft-vv/lib/python3.12/site-packages/vsc/model/value_scalar.py:48: DeprecationWarning: __int__ returned non-int (type ValueInt).  The ability to return an instance of a strict subclass of int is deprecated, and may be removed in a future version of Python.
  v = int(rhs)
/home/wraps03/.venv/craft-vv/lib/python3.12/site-packages/vsc/visitors/dist_constraint_builder.py:102: DeprecationWarning: __int__ returned non-int (type ValueInt).  The ability to return an instance of a strict subclass of int is deprecated, and may be removed in a future version of Python.
  weight = int(w.weight.val())
/home/wraps03/.venv/craft-vv/lib/python3.12/site-packages/vsc/model/variable_bound_in_propagator.py:31: DeprecationWarning: __int__ returned non-int (type ValueInt).  The ability to return an instance of a strict subclass of int is deprecated, and may be removed in a future version of Python.
  in_r_l_t = list(map(lambda e:[int(e.lhs.val()),int(e.rhs.val())] if isinstance(e, ExprRangeModel)
/home/wraps03/.venv/craft-vv/lib/python3.12/site-packages/vsc/model/expr_literal_model.py:42: DeprecationWarning: __int__ returned non-int (type ValueInt).  The ability to return an instance of a strict subclass of int is deprecated, and may be removed in a future version of Python.
  return btor.Const(int(self.val()), ctx_width)
/home/wraps03/.venv/craft-vv/lib/python3.12/site-packages/vsc/model/value_scalar.py:80: DeprecationWarning: __int__ returned non-int (type ValueInt).  The ability to return an instance of a strict subclass of int is deprecated, and may be removed in a future version of Python.
  v = int(rhs)
/home/wraps03/.venv/craft-vv/lib/python3.12/site-packages/vsc/model/expr_partselect_model.py:40: DeprecationWarning: __int__ returned non-int (type ValueInt).  The ability to return an instance of a strict subclass of int is deprecated, and may be removed in a future version of Python.
  return btor.Slice(
/home/wraps03/.venv/craft-vv/lib/python3.12/site-packages/vsc/model/rand_state.py:33: DeprecationWarning: __int__ returned non-int (type ValueInt).  The ability to return an instance of a strict subclass of int is deprecated, and may be removed in a future version of Python.
  low = int(low)
/home/wraps03/.venv/craft-vv/lib/python3.12/site-packages/vsc/model/rand_state.py:34: DeprecationWarning: __int__ returned non-int (type ValueInt).  The ability to return an instance of a strict subclass of int is deprecated, and may be removed in a future version of Python.
  high = int(high)
  6691.00ns INFO     cocotb                             Mid-test reset (partial) at cycle 666, count = 1
 13651.00ns INFO     cocotb                             Mid-test reset (full) at cycle 1358, count = 8
 20111.00ns INFO     cocotb                             Seed: 12345
 20111.00ns INFO     cocotb                             Cycles checked: 2000
 20111.00ns INFO     cocotb                             Occupancy histogram: {0: 94, 1: 239, 2: 289, 3: 239, 4: 258, 5: 239, 6: 266, 7: 290, 8: 87}
 20111.00ns INFO     cocotb                             Simultaneous R/W: 602
 20111.00ns INFO     cocotb                             Write while full: 24
 20111.00ns INFO     cocotb                             Read while empty: 30
 20111.00ns INFO     cocotb.fifo                        fifo : <cocotb_coverage.coverage.CoverItem object at 0x7d9fd0709e80>, coverage=76, size=76
 20111.00ns INFO     cocotb.fifo                           fifo.empty_flag : <cocotb_coverage.coverage.CoverPoint object at 0x7d9fd070b920>, coverage=2, size=2
 20111.00ns INFO     cocotb.fifo                              BIN False : 1908
 20111.00ns INFO     cocotb.fifo                              BIN True : 103
 20111.00ns INFO     cocotb.fifo                           fifo.full_flag : <cocotb_coverage.coverage.CoverPoint object at 0x7d9fd070b8c0>, coverage=2, size=2
 20111.00ns INFO     cocotb.fifo                              BIN False : 1923
 20111.00ns INFO     cocotb.fifo                              BIN True : 88
 20111.00ns INFO     cocotb.fifo                           fifo.illegal : <cocotb_coverage.coverage.CoverItem object at 0x7d9fd07082c0>, coverage=3, size=3
 20111.00ns INFO     cocotb.fifo                              fifo.illegal.flags_vs_occupancy : <cocotb_coverage.coverage.CoverCheck object at 0x7d9fd0708350>, coverage=1, size=1
 20111.00ns INFO     cocotb.fifo                                 BIN PASS : 2003
 20111.00ns INFO     cocotb.fifo                                 BIN FAIL : 0
 20111.00ns INFO     cocotb.fifo                              fifo.illegal.full_and_empty : <cocotb_coverage.coverage.CoverCheck object at 0x7d9fd07082f0>, coverage=1, size=1
 20111.00ns INFO     cocotb.fifo                                 BIN PASS : 2011
 20111.00ns INFO     cocotb.fifo                                 BIN FAIL : 0
 20111.00ns INFO     cocotb.fifo                              fifo.illegal.ptr_vs_occupancy : <cocotb_coverage.coverage.CoverCheck object at 0x7d9fd0708380>, coverage=1, size=1
 20111.00ns INFO     cocotb.fifo                                 BIN PASS : 2003
 20111.00ns INFO     cocotb.fifo                                 BIN FAIL : 0
 20111.00ns INFO     cocotb.fifo                           fifo.occ_transition : <cocotb_coverage.coverage.CoverPoint object at 0x7d9fd070bbf0>, coverage=4, size=4
 20111.00ns INFO     cocotb.fifo                              BIN empty->one : 75
 20111.00ns INFO     cocotb.fifo                              BIN one->empty : 74
 20111.00ns INFO     cocotb.fifo                              BIN almost_full->full : 76
 20111.00ns INFO     cocotb.fifo                              BIN full->almost_full : 76
 20111.00ns INFO     cocotb.fifo                           fifo.occupancy : <cocotb_coverage.coverage.CoverPoint object at 0x7d9fd0708260>, coverage=5, size=5
 20111.00ns INFO     cocotb.fifo                              BIN empty : 103
 20111.00ns INFO     cocotb.fifo                              BIN one : 239
 20111.00ns INFO     cocotb.fifo                              BIN partial : 1291
 20111.00ns INFO     cocotb.fifo                              BIN almost_full : 290
 20111.00ns INFO     cocotb.fifo                              BIN full : 88
 20111.00ns INFO     cocotb.fifo                           fifo.op : <cocotb_coverage.coverage.CoverPoint object at 0x7d9fd0709d90>, coverage=4, size=4
 20111.00ns INFO     cocotb.fifo                              BIN idle : 215
 20111.00ns INFO     cocotb.fifo                              BIN write : 598
 20111.00ns INFO     cocotb.fifo                              BIN read : 594
 20111.00ns INFO     cocotb.fifo                              BIN read_write : 604
 20111.00ns INFO     cocotb.fifo                           fifo.op_x_occupancy : <cocotb_coverage.coverage.CoverCross object at 0x7d9fd07081d0>, coverage=20, size=20
 20111.00ns INFO     cocotb.fifo                              BIN ('idle', 'empty') : 17
 20111.00ns INFO     cocotb.fifo                              BIN ('idle', 'one') : 22
 20111.00ns INFO     cocotb.fifo                              BIN ('idle', 'partial') : 137
 20111.00ns INFO     cocotb.fifo                              BIN ('idle', 'almost_full') : 31
 20111.00ns INFO     cocotb.fifo                              BIN ('idle', 'full') : 8
 20111.00ns INFO     cocotb.fifo                              BIN ('write', 'empty') : 51
 20111.00ns INFO     cocotb.fifo                              BIN ('write', 'one') : 81
 20111.00ns INFO     cocotb.fifo                              BIN ('write', 'partial') : 384
 20111.00ns INFO     cocotb.fifo                              BIN ('write', 'almost_full') : 77
 20111.00ns INFO     cocotb.fifo                              BIN ('write', 'full') : 4
 20111.00ns INFO     cocotb.fifo                              BIN ('read', 'empty') : 7
 20111.00ns INFO     cocotb.fifo                              BIN ('read', 'one') : 74
 20111.00ns INFO     cocotb.fifo                              BIN ('read', 'partial') : 376
 20111.00ns INFO     cocotb.fifo                              BIN ('read', 'almost_full') : 82
 20111.00ns INFO     cocotb.fifo                              BIN ('read', 'full') : 55
 20111.00ns INFO     cocotb.fifo                              BIN ('read_write', 'empty') : 27
 20111.00ns INFO     cocotb.fifo                              BIN ('read_write', 'one') : 62
 20111.00ns INFO     cocotb.fifo                              BIN ('read_write', 'partial') : 394
 20111.00ns INFO     cocotb.fifo                              BIN ('read_write', 'almost_full') : 100
 20111.00ns INFO     cocotb.fifo                              BIN ('read_write', 'full') : 21
 20111.00ns INFO     cocotb.fifo                           fifo.op_x_reset : <cocotb_coverage.coverage.CoverCross object at 0x7d9fd0708230>, coverage=4, size=4
 20111.00ns INFO     cocotb.fifo                              BIN ('idle', True) : 2
 20111.00ns INFO     cocotb.fifo                              BIN ('write', True) : 2
 20111.00ns INFO     cocotb.fifo                              BIN ('read', True) : 2
 20111.00ns INFO     cocotb.fifo                              BIN ('read_write', True) : 2
 20111.00ns INFO     cocotb.fifo                           fifo.ptrs_equal : <cocotb_coverage.coverage.CoverPoint object at 0x7d9fd0708170>, coverage=2, size=2
 20111.00ns INFO     cocotb.fifo                              BIN empty : 97
 20111.00ns INFO     cocotb.fifo                              BIN full : 87
 20111.00ns INFO     cocotb.fifo                           fifo.rd_burst : <cocotb_coverage.coverage.CoverPoint object at 0x7d9fd070be30>, coverage=4, size=4
 20111.00ns INFO     cocotb.fifo                              BIN 1 : 200
 20111.00ns INFO     cocotb.fifo                              BIN 2-3 : 106
 20111.00ns INFO     cocotb.fifo                              BIN 4-7 : 64
 20111.00ns INFO     cocotb.fifo                              BIN 8+ : 40
 20111.00ns INFO     cocotb.fifo                           fifo.rd_ptr : <cocotb_coverage.coverage.CoverPoint object at 0x7d9fd07080e0>, coverage=8, size=8
 20111.00ns INFO     cocotb.fifo                              BIN 0 : 235
 20111.00ns INFO     cocotb.fifo                              BIN 1 : 262
 20111.00ns INFO     cocotb.fifo                              BIN 2 : 255
 20111.00ns INFO     cocotb.fifo                              BIN 3 : 234
 20111.00ns INFO     cocotb.fifo                              BIN 4 : 227
 20111.00ns INFO     cocotb.fifo                              BIN 5 : 277
 20111.00ns INFO     cocotb.fifo                              BIN 6 : 244
 20111.00ns INFO     cocotb.fifo                              BIN 7 : 277
 20111.00ns INFO     cocotb.fifo                           fifo.rd_wrap : <cocotb_coverage.coverage.CoverPoint object at 0x7d9fd0708140>, coverage=1, size=1
 20111.00ns INFO     cocotb.fifo                              BIN True : 144
 20111.00ns INFO     cocotb.fifo                           fifo.reset : <cocotb_coverage.coverage.CoverPoint object at 0x7d9fd070bb30>, coverage=1, size=1
 20111.00ns INFO     cocotb.fifo                              BIN True : 8
 20111.00ns INFO     cocotb.fifo                           fifo.reset_occ : <cocotb_coverage.coverage.CoverPoint object at 0x7d9fd070bb90>, coverage=3, size=3
 20111.00ns INFO     cocotb.fifo                              BIN empty : 6
 20111.00ns INFO     cocotb.fifo                              BIN partial : 1
 20111.00ns INFO     cocotb.fifo                              BIN full : 1
 20111.00ns INFO     cocotb.fifo                           fifo.wr_burst : <cocotb_coverage.coverage.CoverPoint object at 0x7d9fd1169dc0>, coverage=4, size=4
 20111.00ns INFO     cocotb.fifo                              BIN 1 : 170
 20111.00ns INFO     cocotb.fifo                              BIN 2-3 : 125
 20111.00ns INFO     cocotb.fifo                              BIN 4-7 : 61
 20111.00ns INFO     cocotb.fifo                              BIN 8+ : 38
 20111.00ns INFO     cocotb.fifo                           fifo.wr_ptr : <cocotb_coverage.coverage.CoverPoint object at 0x7d9fd07080b0>, coverage=8, size=8
 20111.00ns INFO     cocotb.fifo                              BIN 0 : 260
 20111.00ns INFO     cocotb.fifo                              BIN 1 : 234
 20111.00ns INFO     cocotb.fifo                              BIN 2 : 248
 20111.00ns INFO     cocotb.fifo                              BIN 3 : 232
 20111.00ns INFO     cocotb.fifo                              BIN 4 : 236
 20111.00ns INFO     cocotb.fifo                              BIN 5 : 248
 20111.00ns INFO     cocotb.fifo                              BIN 6 : 276
 20111.00ns INFO     cocotb.fifo                              BIN 7 : 277
 20111.00ns INFO     cocotb.fifo                           fifo.wr_wrap : <cocotb_coverage.coverage.CoverPoint object at 0x7d9fd0708110>, coverage=1, size=1
 20111.00ns INFO     cocotb.fifo                              BIN True : 145
 20111.00ns INFO     cocotb.regression                  test_crv passed
 20111.00ns INFO     cocotb.regression                  **************************************************************************************
                                                        ** TEST                          STATUS  SIM TIME (ns)  REAL TIME (s)  RATIO (ns/s) **
                                                        **************************************************************************************
                                                        ** test_fifo.test_crv             PASS       20111.00          14.24       1412.70  **
                                                        **************************************************************************************
                                                        ** TESTS=1 PASS=1 FAIL=0 SKIP=0              20111.00          14.95       1344.79  **
                                                        **************************************************************************************

make[1]: Leaving directory '/home/wraps03/Fall2026/craft-vv-student/code/tb/fifo_crv'
make: Leaving directory '/home/wraps03/Fall2026/craft-vv-student/code/tb/fifo_crv'
```


## Final Verdict

**What worked:** The AI-generated coverage model successfully tracked FIFO operations, occupancy, resets, and pointer behavior. After making adjustments, we achieved 100% functional coverage (76/76 bins).

**What did not work:** The original code had compatibility issues with our testbench and missed certain reset conditions, requiring additional changes, hitting 43/46 orignal bins.

**Remaining limitations:** Although we achieved 100% functional coverage, this does not guarantee that every possible FIFO fault can be detected.

**If we had another day:** We would run additional seeds and expand our testing to cover more scenarios and improve our chances of detecting faults.
