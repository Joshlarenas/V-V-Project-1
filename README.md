# Project 1 – Constrained-Random Verification of a Synchronous FIFO

**Course:** EEE 4701 / EEE 5703 – Verification and Validation of Digital Systems  
**Project Type:** Team Assignment (2–3 Members)  
**Deadline:** Sunday, 11:59 PM (See Webcourses)  
**Project Weight:** 15% of Course Grade

---

## 1. Project Overview

The goal of this project is to develop a complete verification environment for a synchronous FIFO (First-In, First-Out) design.

Using the provided FIFO RTL and specification, our team will build a constrained-random testbench to verify the design's functionality, measure functional coverage, and evaluate how effectively our tests detect intentional design faults (mutants).

The project builds upon the previous FIFO testbench and expands it into a more complete verification environment.

### Tools
- Python
- cocotb
- pyvsc
- cocotb-coverage
- GTKWave

---

## 2. Project Tasks

### Task 1 – Verification Plan
**File:** `vplan.md`

- Identify FIFO features and requirements.
- Create a test matrix.
- Define functional coverage points, bins, and crosses.
- Identify testing risks and priorities.
- Connect each planned test to a specification requirement.

### Task 2 – Layered Verification Environment
**Directory:** `tb/`

Develop a cocotb testbench consisting of:

- **Driver:** Sends transactions to the FIFO.
- **Monitor:** Observes FIFO inputs and outputs.
- **Scoreboard:** Compares actual FIFO behavior against a reference queue.

### Task 3 – Constrained-Random Verification
**Directory:** `crv/`

- Create a `pyvsc` transaction class.
- Implement constraints to keep transactions legal.
- Test near-full and near-empty conditions.
- Test bursts of reads and writes.
- Test simultaneous reads and writes.
- Document the generated stimulus distribution.
- Implement reproducible, seeded regressions.

### Task 4 – Functional Coverage
**Deliverable:** Coverage model and report

- Define and collect functional coverage.
- Reach the required coverage target.
- Identify missing coverage bins (coverage holes).
- Adjust constraints to close coverage holes.
- Document how coverage improved (convergence argument).
- Justify any directed tests used for closure.

### Task 5 – Mutation Testing
**File:** `FINDINGS.md`

- Run tests against the released mutant pool.
- Record the number of mutants detected (`found/total`).
- Analyze at least two surviving mutants.
- Explain why each survivor was not detected.
- Describe what additional testing could detect them.

**Note:** A mutation detection rate of 90% on the hidden pool earns full credit for mutation quality.

### Task 6 – Final Report and Demo
**Files:** `REPORT.pdf`, demo link

- Prepare a 4–6 page report.
- Explain the verification environment and methodology.
- Present functional coverage results.
- Present mutation testing results.
- Discuss remaining limitations and risks.
- Record a short demonstration of the environment and supporting evidence.

---

## 3. Additional Requirements

### AI Verification Log
**File:** `ai_log.md`

- Use AI to draft a coverage model or block of constraints.
- Record the AI prompt.
- Predict potential issues before running the generated code.
- Test the generated implementation.
- Document actual results, evidence, and any corrections made.

### Security & Trust
- Add at least one coverpoint or assertion for an illegal or undefined control combination.
- Examples include a write during reset or simultaneous read/write behavior at the empty boundary.

### Team Contributions
**File:** `CONTRIBUTIONS.md`

- Record each team member's contributions.
- Ensure every team member commits to the repository.
- Review work across the verification environment.

---

## 4. Required Deliverables

- [ ] `vplan.md` – Verification plan
- [ ] `tb/` – Driver, monitor, and scoreboard
- [ ] `crv/` – Transactions, constraints, and seeded regression
- [ ] Functional coverage model and report
- [ ] `FINDINGS.md` – Mutation results and survivor analysis
- [ ] `REPORT.pdf` – Final 4–6 page report
- [ ] Demo video link
- [ ] `ai_log.md` – AI verification log
- [ ] `CONTRIBUTIONS.md` – Team contributions
- [ ] All local checks passing
- [ ] Final team repository or ZIP submitted

---

## 5. Grading Breakdown

| Category | Weight |
|---|---:|
| Mutation Quality | 35% |
| Functional Coverage | 25% |
| Verification Environment | 15% |
| Final Report | 15% |
| Reproducibility | 10% |
| **Total** | **100%** |

---

## 6. Submission Instructions

1. Complete all required project tasks.
2. Verify that all local checks pass.
3. Confirm that seeded regressions can reproduce results.
4. Include all required files and directories.
5. Include the final report and demonstration link.
6. Ensure `CONTRIBUTIONS.md` documents team participation.
7. Submit the completed team repository or ZIP by **Sunday at 11:59 PM**, according to Webcourses.

---

## 7. Graduate Extension (EEE 5703)

*Required for EEE 5703 teams; optional bonus for EEE 4701.*

- Plot the occupancy distribution produced by the constraints.
- Compare the distribution against a uniform distribution.
- Derive a constraint that reaches a selected corner with probability greater than `p` within `N` draws.
- Analyze the relationship between coverage closure and mutation detection.

---

**Reference:** Project 1 – Constrained-Random Verification of a Synchronous FIFO, EEE 4701 / EEE 5703, Fall 2026.
