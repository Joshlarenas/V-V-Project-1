# FINDINGS — Project 1 · Joshua Larenas & Caleb Allen

The mutation score represents how many faulty FIFO implementations our testbench was able to detect out of the total tested. Functional coverage measures how many of our defined testing scenarios were exercised. Both results help evaluate our testbench's effectiveness, but neither guarantees that every possible fault can be detected.

## Score

| Pool | found | total | % |
|------|------:|------:|--:|
| released (practice) | 8| 8| 100%|
| hidden (reported at grading) | | | |

**NOTE:** Although not necessarily stated, our bin score during our coverage was 76/76 bins! aka 100%. We believed this number was also beneficial to include in the FINDINGS file to show the representation of our code's capability.

**Command run:**

```bash
just mutate fifo_crv
```

**Command Output:**
```bash
clean RTL: 1 tests passed.

  [found  ] full_offbyone        (test-failed)  -- full asserts one entry too early (cnt == DEPTH-1)
  [found  ] empty_offbyone       (test-failed)  -- empty asserts one entry too early (cnt == 1)
  [found  ] ignore_full          (test-failed)  -- writes are accepted even when full (overflow)
  [found  ] ignore_empty         (test-failed)  -- reads are accepted even when empty (underflow)
  [found  ] count_wr_dec         (test-failed)  -- a write-only cycle decrements the count
  [found  ] rd_data_wrptr        (test-failed)  -- rd_data reads from the write pointer instead of the read pointer
  [found  ] mem_corrupt          (test-failed)  -- stored data is corrupted (+1) on write
  [found  ] wrptr_wrap_early     (test-failed)  -- write pointer wraps one slot early

==== found/total = 8/8  =  100.0%  (threshold 90%) ====
```
## Survivors

**NOTE:** Our mutation testing achieved 100% detection on the first run because we had already made the necessary adjustments to our testbench through `just test fifo_crv icarus`. By the time we ran mutation testing, our testbench was fully working and had achieved 100% functional coverage.

| Mutant | What it changes | Reachable by my stimulus? | Observable by my checks? | Why it survived |
|--------|-----------------|---------------------------|--------------------------|-----------------|
|        N/A|                 N/A| N/A             | N/A |  No Surviving Mutants|

## What I changed, and what it bought

**NOTE:** As stated before, our mutation testing was 100% successful on our first iteration due to adjustments made during our debugging faze in coordination with the just test fifo_crv icarus command.

| Change | Score before | Score after | Which survivors it caught |
|--------|-------------:|------------:|---------------------------|
|        N/A|              8/8|             8/8|  No Initial Surviving Mutants|

## Residual risk

What this suite still cannot catch, stated plainly. Name a fault class, not a
mutant id — the pool is a sample, not the population.

1. **Operation Sequence Faults (Reachability):** Certain bugs may only occur during specific sequences of read and write operations that our constrained-random testing did not generate.
2. **Timing Faults (Observability):** Since outputs are checked after each clock edge, temporary errors occurring between sampling points may not be detected.

**If I had another day:** I would test additional random seeds to explore more operation sequences and improve our chances of detecting faults.

## Corner Checklist

1. [x] **full_offbyone**
2. [x] **empty_offbyone**
3. [x] **ignore_full**
4. [x] **ignore_empty**
5. [x] **rd_data_wrptr**
6. [x] **mem_corrupt**
7. [x] **wrptr_wrap_early**
