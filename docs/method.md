# The Method: Why Every Session Follows This Loop

This document explains the full learning methodology of the Frontier Engineer Field Manual. It is not a summary. It is the complete operating system: where the loop came from, why each step exists, how to manage AI, how to keep an engineering log, how to review your own work, and what to do when you are stuck.

If you are following along, read this before Session 01 and refer back to it constantly.

---

## Table of Contents

1. [Origin and Philosophy](#1-origin-and-philosophy)
2. [The Three Spines](#2-the-three-spines)
3. [The Dependency Rule](#3-the-dependency-rule)
4. [The 7-Step Daily Loop and Why Each Step Exists](#4-the-7-step-daily-loop-and-why-each-step-exists)
5. [The Programming Approach: Where Planning Fits](#5-the-programming-approach-where-planning-fits)
6. [Mastery Gate: Advance Only When All Are True](#6-mastery-gate-advance-only-when-all-are-true)
7. [The AI-Quarantine Protocol](#7-the-ai-quarantine-protocol)
8. [Understanding Debt](#8-understanding-debt)
9. [The Engineering Log](#9-the-engineering-log)
10. [The Question Ladder](#10-the-question-ladder)
11. [Review Cadence Without a Calendar](#11-review-cadence-without-a-calendar)
12. [When Stuck: The Reduction Hierarchy](#12-when-stuck-the-reduction-hierarchy)
13. [Repository Rules](#13-repository-rules)
14. [Field Checklists](#14-field-checklists)
15. [How to Ask Better Questions](#15-how-to-ask-better-questions)

---

## 1. Origin and Philosophy

This loop was designed for a specific kind of self-study: one where you are building a T-shaped technical identity (deep in computational physics + mission-grade software, broad across spacecraft systems, autonomy, and AI) without the structure of a university program or a code review team.

The core philosophy is simple:

**Every equation becomes an executable. Every implementation gets tested, broken deliberately, and verified independently. No borrowed understanding.**

The 7-step loop exists because each step catches a different kind of failure that the other steps miss. Skip one and you create a blind spot. Skip several and you are doing symbol memorization, not engineering.

The loop also matters because of what it replaces. Most self-study approaches fall into one of these traps:

| Trap | What happens | Why it fails |
|------|-------------|-------------|
| Tutorial consumption | Read/watch, feel like you learned, cannot reproduce | No prediction, no falsification |
| Calculator dependency | Type numbers into a solver, get answers, cannot explain | No derivation, no implementation |
| AI dependency | Ask AI for code, it works, you cannot reconstruct it | No cold start, no blank-page replay |
| Course pacing | Move on because the calendar says so, not because you own it | No mastery gate |
| Breadth without depth | Collect introductions to many topics, build nothing reusable | No dependency rule, no evidence ladder |

The loop is the countermeasure. It forces you to produce something at every step, compare it against reality, and keep only what you can defend.

---

## 2. The Three Spines

Everything builds along three simultaneous spines. No spine is optional.

**Language strategy across the spines:**

| Language | Role | When it enters |
|----------|------|----------------|
| **Rust** | Primary learning and systems language. Ownership, borrowing, explicit errors, and algebraic data types force design decisions into the open. | Day 1 (Session 01) |
| **Python** | Scientific/AI notebook and reference language. Exploration, visualization, ML training. Bridges to Rust via PyO3/maturin. | Stage 10 (Unit 73) |
| **C/C++** | Required bridge for flight frameworks (cFS, F Prime), libraries, interviews, and legacy integration. FFI via bindgen/cxx. | Stage 7 (Unit 51) |

Rust is the primary language, but Rust is not enough. Current SpaceX, Rocket Lab, Varda, Axiom, and quant roles still repeatedly signal C++, Python, or both. The curriculum does not restart from zero in each language -- it re-implements selected, already-validated components (Vec3, RK4, a parser, a telemetry packet) and focuses the comparison on ownership, errors, layout, build systems, testing, and ecosystem integration, not language marketing. The manual explicitly warns against trying to become simultaneously equivalent to a PhD physicist, a senior flight-software engineer, a GNC specialist, a quantum researcher, and a propulsion engineer. Instead, it builds a **T-shaped identity**: deep capability in computational physics + mission-grade software, supported by broad literacy across spacecraft systems, autonomy, AI, and quantum technology.

```
  Physical Reasoning          Software Systems           Evidence & Judgment
  +-------------------+      +-------------------+      +-------------------+
  | Mechanics         |      | Rust (from Day 1) |      | Requirements      |
  | Dynamics          |      | Python (science)  |      | Uncertainty       |
  | Calculus          |      | C/C++ interop     |      | Validation        |
  | Linear algebra    |      | Testing / fuzzing |      | Independent refs  |
  | Numerics          |      | OS / embedded     |      | Failure analysis  |
  | Controls          |      | Real-time         |      | Technical writing |
  | Estimation        |      | Networking        |      | Peer review       |
  | Probability       |      | Security          |      |                   |
  +--------+----------+      +--------+----------+      +--------+----------+
           |                          |                          |
           +--------------------------+--------------------------+
                                      |
                           +----------+----------+
                           | Computational Space |
                           | Systems Engineer    |
                           +---------------------+
```

**Why this matters:** A self-study program makes you unusually strong at the *interfaces* - translating models into software, testing scientific claims, integrating systems, and learning new domains quickly. That interface is commercially and scientifically valuable. Current SpaceX, Rocket Lab, Anduril, Varda, and Axiom roles all demand this exact overlap.

---

## 3. The Dependency Rule

Every unit answers four questions:

1. **What must already be true?** (prerequisites)
2. **What new mental model is being added?** (concept)
3. **What artifact extends the previous work?** (build evidence)
4. **What evidence proves readiness for the next unit?** (mastery gate)

If a prerequisite is weak, branch backward, repair it with a focused exercise, and return. This prevents later topics from becoming symbol memorization.

```
  Algebra +            Rust +               Measurement +
  trigonometry ----+-- software craft ---+-- probability
                    |                      |
         Calculus + linear algebra ------+
                    |
         Mechanics + numerics
                    |
         Systems + embedded
                    |
         GNC + astrodynamics
                    |
         Autonomy + AI
                    |
         Mission-grade evidence
```

**Why dependency-driven and not calendar-driven:** Calendar pacing turns depth into deadline pressure. When you track "week 6" you start cutting corners to hit the date. When you track "unit 6 requires mastery of unit 5" you either earn the next step or you go back and fix the gap. The unit numbers exist to show dependency order and rising difficulty, never to impose a schedule.

---

## 4. The 7-Step Daily Loop and Why Each Step Exists

This is the engine. Every session, every unit, every practice file follows this loop. It is not optional and it is not a suggestion. The loop exists because each step catches a different kind of failure that the other steps miss.

### Step 1: PREDICT

**What you do:** State sign, direction, order of magnitude, and failure cases *before any calculation*.

**Evidence produced:** A written prediction that can be wrong.

**Why it exists:** If you calculate first and then rationalize the answer, you never discover whether you actually understood the physics. A prediction you commit to *before* running the code creates a falsifiable hypothesis. When the code disagrees with your prediction, the discrepancy is where learning happens. When it agrees, you have evidence that your intuition is calibrated - not just that your code compiled.

**Example:** "A ball thrown up at 10 m/s under gravity should reach peak at about t=1s and be falling by t=2s. Position at t=2s should be near zero (it went up and came back down). Velocity should be negative (falling)."

> [!NOTE]
> For a detailed guide on understanding **Scale** (order of magnitude), learning how to predict when you do not yet know the equations, and doing practice exercises with solutions, see the [Predict Practice Workbook](predict_practice/README.md).


### Step 2: EXPLAIN

**What you do:** Draw the physical story. Name system boundary, frame, units, assumptions, inputs, and outputs.

**Evidence produced:** A diagram and a five-sentence explanation.

**Why it exists:** Most engineering errors are not math errors - they are *framing* errors. Wrong coordinate frame. Wrong system boundary (forgot drag, forgot a force). Wrong units. Wrong assumption (constant acceleration when acceleration varies). By forcing yourself to articulate the physical story in five sentences and a diagram *before* touching equations, you surface these errors while they are still cheap to fix.

This step replaced "understand" from the original Apocenter 6-step loop because "understand" is vague. "Explain" demands externalization - you must produce a diagram and sentences that someone else could follow.

### Step 3: DERIVE

**What you do:** Move from definitions to equation. Check dimensions and limiting cases.

**Evidence produced:** A hand derivation with every symbol defined.

**Why it exists:** Dimensional analysis catches algebra errors. Limiting cases (what happens at t=0? at t=infinity? at a=0?) catch physics errors. If you skip derivation and jump to code, you are implementing a formula you cannot verify - you are trusting a symbol string rather than understanding why it is correct.

Every symbol in your derivation must have a meaning, type, unit, frame, epoch, sign convention, and valid domain. If you cannot name these for every symbol, you do not own the equation yet.

### Step 4: IMPLEMENT

**What you do:** Create the smallest pure Rust function or type expressing the idea.

**Evidence produced:** Compiling code with a clear API and no hidden I/O.

**Why it exists:** Implementation is where the abstraction meets the machine. The constraints of a programming language expose everything vague in your derivation. "What type is this quantity?" "What happens when this input is zero?" "Can this return an error?" These questions, which derivation can dodge, become unavoidable in code.

The implementation should be **minimal** - the smallest function that expresses the idea. Not a framework, not a library, not a class hierarchy. One function. One type. One concept. You earn complexity through the later steps (test, falsify) when you discover why the minimal version is insufficient.

Rust specifically enforces this discipline through its type system: ownership, borrowing, lifetimes, and Result types make hidden assumptions impossible. You cannot ignore error cases. You cannot accidentally share mutable state. The compiler forces honesty.

### Step 5: TEST

**What you do:** Verify against a known case, a boundary case, a property/invariant, and an independent reference.

**Evidence produced:** Automated tests plus a short validation note.

**Why it exists:** A single test against a known value catches gross errors. A boundary test (t=0, a=0, very large t) catches edge-case failures. A property test (energy is conserved, magnitude is always non-negative, dot product of orthogonal vectors is zero) catches structural errors that survive individual examples. An independent reference (a published value, a different tool's output, an analytic solution) catches systematic errors where your derivation and code share the same blind spot.

The test hierarchy is intentional: known case is the weakest check, independent reference is the strongest. You need all four because each catches what the others miss.

### Step 6: FALSIFY

**What you do:** Change scale, sign, step, noise, or model assumptions to make it fail.

**Evidence produced:** A failure you can explain and a declared operating domain.

**Why it exists:** This is the step that most curricula skip. Knowing where your code *works* is not enough. You must know where it *breaks* and *why*. This is the difference between someone who has a working demo and someone who has engineering judgment.

Falsification means deliberately trying to break your own code:
- What happens at r=0 (singularity in gravity)?
- What happens with NaN inputs?
- What happens with very large step sizes in the integrator?
- What happens when acceleration is not constant?
- What happens at extreme time scales where floating-point precision degrades?

When you find a failure, you must classify it: Is it a **bug** (your code is wrong), a **numerical limit** (your math is right but the computer cannot represent it), or a **model limitation** (your equation is correct for its assumptions but those assumptions no longer hold)?

You then **declare the operating domain** - the range of inputs and conditions where your code is trustworthy. Everything outside that domain is explicitly unverified.

### Step 7: TEACH

**What you do:** Explain what changed in your mental model and where uncertainty remains.

**Evidence produced:** A README note, diagram, or two-minute recording.

**Why it exists:** Teaching is the ultimate test of understanding. If you cannot explain it simply, you do not own it. This step also produces external evidence - a note that another engineer (or your future self) can read and verify.

The teaching step closes the loop. What you predicted in Step 1 is compared against what you learned by Step 6. The gap between prediction and reality is the learning. Teaching makes that gap explicit and durable.

This step exists because producing external evidence is what separates a learner from an engineer. A learner consumes. An engineer produces artifacts others can inspect.

---

## 5. The Programming Approach: Where Planning Fits

People often ask: "Where does software design fit in the 7-step loop?" The answer is that design is not a separate phase -- it is distributed across the loop, and each step has a specific programming discipline attached to it.

### How the loop maps to code

```
  LOOP STEP          PROGRAMMING DISCIPLINE                 OUTPUT
  ─────────          ──────────────────────                  ──────
  1. Predict         Write expected output as a comment.     A comment that can be wrong.
                     Do not touch the keyboard yet.

  2. Explain         Sketch the types and data flow.         A type-level design on paper.
                     What are the inputs? Outputs? What
                     can fail? What units does each
                     quantity carry?

  3. Derive          Write the equation in a comment         A derivation comment block.
                     above where the function will go.
                     Check dimensions. This comment
                     IS the spec.

  4. Implement       Write the smallest function that        One compiling function.
                     matches the derivation. No framework.
                     No abstraction. Pure function:
                     inputs in, result out, no hidden I/O,
                     no side effects.

  5. Test            Write tests in this order:              A test module.
                     (a) Known value from a textbook
                     (b) Boundary case (zero, empty, max)
                     (c) Structural property (symmetry,
                         conservation, monotonicity)
                     (d) Independent reference if available

  6. Falsify         Deliberately feed bad inputs.           A failure catalog + declared
                     Classify each failure. Write the        operating domain in docs.
                     operating domain as a doc comment
                     on the function.

  7. Teach           Write a BRIEF.md note explaining        A reusable explanation.
                     what the code does, why it is
                     structured this way, and where it
                     fails. Another engineer should be
                     able to understand it from this
                     alone.
```

### The flexibility principle

The loop is a discipline, not a straightjacket. Real programming is messy. You will discover during implementation that your derivation was wrong. You will discover during testing that your API is awkward. You will discover during falsification that your model is too simple. That is fine. The loop is iterative:

```
  Predict ──► Explain ──► Derive ──► Implement ──► Test ──► Falsify
     ^                                                       |
     |                                                       |
     └───────────── loop back when reality surprises ◄──────┘
```

When you loop back, you do not restart from scratch. You update the specific step that was wrong:
- If the implementation exposed a physics error, fix the derivation (Step 3), then re-derive the code.
- If the test exposed a code bug, fix the implementation (Step 4).
- If falsification exposed a model limitation, either fix the model or declare the domain (Steps 3 and 6).

### Where API design happens

API design is not a separate meeting. It happens at Step 2 (Explain) and is refined at Step 4 (Implement):

- **Step 2**: You sketch function signatures on paper. `fn speed(distance: f64, time: f64) -> f64`. You ask: what units? What can fail? Should this return Result?
- **Step 4**: You discover the consequences of your design. Maybe `f64` for everything is too loose. Maybe you need a newtype for Meters. You revise.
- **Step 5**: Your tests reveal whether the API is usable. If every test needs three lines of setup, the API is too coupled. Simplify.

This is why the manual says "create the smallest pure Rust function or type." You start minimal and let the tests and falsification tell you what complexity you actually need. You do not design a framework and then try to fit physics into it.

### Where architecture happens

Software architecture enters in Stage 1 Session 10 (Build a maintainable crate) and compounds from there. The early sessions are intentionally single-file, single-function. Architecture is earned:

```
  Sessions 01-09:   One file, one or two functions. No modules.
  Session 10:       Split into lib.rs + main.rs. First real architecture.
  Sessions 11-14:   Add closures, generics, iterators. Still one crate.
  Session 15:       First release: crate boundaries, CLI, CSV output.
  Session 30:       First workspace: multiple modules, integration tests, CI.
```

You do not architect before you understand the domain. You architect when the pain of not archiving becomes real. Session 10 exists because by then you have nine sessions of single-file code and you can feel why separation matters. That feeling is the prerequisite for learning modules, pub, and lib.rs.

### The anti-patterns

| Anti-pattern | Why it fails | What to do instead |
|---|---|---|
| Design the full API before predicting | You optimize for code aesthetics, not physics | Predict first, let the equation drive the API |
| Build a framework, then fill in physics | Premature abstraction hides misunderstanding | One function. One concept. Earn complexity. |
| Write all tests after implementation | You subconsciously avoid testing edge cases you know will fail | Write test cases BEFORE implementation (Step 2-3) |
| Skip falsification because tests pass | Passing tests prove your code works for cases you thought of. They say nothing about cases you didn't. | Always falsify. Always declare the domain. |
| Start with AI-generated code | You bypass Steps 1-3 entirely. No prediction, no derivation, no design. | AI enters at Pass 3 (targeted help) or Pass 4 (adversarial review) |

---

## 6. Mastery Gate: Advance Only When All Are True

Do not move to the next unit until you can honestly answer YES to every one of these:

- [ ] I can solve a representative problem **without AI or notes**.
- [ ] I can explain the **assumptions, units, coordinate frame, valid domain**, and limiting behavior.
- [ ] I can **implement it in Rust** and explain every type, branch, allocation, and error path I wrote.
- [ ] Tests include a **known result**, an **edge case**, a **structural property**, and an **independent comparison** when available.
- [ ] I can show a **failure**, explain why it occurs, and state whether it is a bug, numerical limit, or model limitation.
- [ ] The repository is **reproducible** from a clean clone and the README tells another engineer how to verify it.

**Why all six:** If you can implement but not explain, you have borrowed understanding. If you can explain but not implement, you have theory without engineering. If your tests pass but you have never falsified, you have a demo you cannot trust under stress. If you cannot reproduce from a clean clone, your result is anecdotal.

---

## 7. The AI-Quarantine Protocol

This is the most important section for anyone using AI tools (including this repo's author). The manual does not ban AI. It quarantines it behind deliberate practice.

AI is a powerful accelerator. It is also the easiest way to destroy your own learning. The protocol resolves this tension with seven sequential passes. You do not skip ahead.

```
  Pass                  AI Access      Your Job
  ----                  ----------     --------
  1. Cold start         NONE           Restate the problem, draw it, predict
                                        sign/scale, define symbols and assumptions.

  2. First attempt      NONE           Derive, design API/tests, write the
                                        smallest implementation, record confusion.

  3. Targeted help      ALLOWED        Ask for ONE explanation, counterexample,
                          (narrow)      or critique. NOT an end-to-end answer.

  4. Adversarial        ALLOWED        Ask AI to find unit/frame/sign bugs,
     review                            hidden assumptions, edge cases, and
                                        missing tests.

  5. Independent        NONE           Check textbook/standard, hand case,
     verification       (no trust      dimensions, property, independent tool,
                        granted)       and experiment.

  6. Blank-page         NONE           Recreate the key derivation and code
     replay                            skeleton from memory later.

  7. Ownership          NONE           Write what you trust, why, where it
     statement                         fails, and what you would say in a
                                        mission review.
```

**Why Pass 1 and 2 have zero AI access:** If AI solves the problem before you have struggled with it, you learn nothing. The struggle IS the learning. The cold start forces you to engage with the problem on its own terms. The first attempt forces you to produce something, even if it is wrong. A wrong attempt you wrote yourself is worth more than a correct answer you copied.

**Why Pass 3 is narrow:** AI is useful for unblocking - one specific question, one counterexample, one critique. But if you ask for an end-to-end answer, you bypass the learning. The constraint is: ask for the *smallest possible piece of help* that unblocks you.

**Why Pass 4 is adversarial:** This is where AI is most valuable. You have a working implementation. Now you ask AI to attack it: find bugs, hidden assumptions, edge cases, missing tests. AI is better at finding flaws in existing code than at generating correct code from scratch. Use it as a reviewer, not a writer.

**Why Pass 5 grants no trust:** AI can be confidently wrong. An independent reference (textbook, standard, published value, different tool) is the only trustworthy oracle. Dimensions, hand calculations, and limiting cases are oracles that AI cannot hallucinate.

**Why Pass 6 exists (blank-page replay):** If you cannot recreate the essential derivation and code from memory, you did not learn it. You borrowed it. The blank-page replay is the test that distinguishes ownership from understanding debt.

**Why Pass 7 exists (ownership statement):** In a real mission review, you must be able to say "I trust this because X, it fails when Y, and the residual risk is Z." The ownership statement is practice for that moment.

---

## 8. Understanding Debt

> If AI gives you a correct solution that you cannot reconstruct, the task is not complete. Mark it as borrowed, schedule a blank-page replay, and do not build a dependent concept on top of it yet.

Understanding debt is like technical debt but worse. Technical debt means your code works but is messy. Understanding debt means your code works but you do not know why. Every concept built on top of borrowed understanding compounds the risk.

If you have understanding debt in Unit 9 (Newton's laws), then Unit 13 (ODE initial-value problems) will be memorization, not engineering. By Unit 25 (state derivatives), you will be lost.

The rule: **never build a dependent concept on top of borrowed understanding.** Schedule a blank-page replay first. If you cannot pass it, go back and repair the prerequisite.

---

## 9. The Engineering Log

Every session ends with a log entry. This is not optional. The log is the external memory that compounds across units.

| Field | What to write before leaving the session |
|-------|------------------------------------------|
| **Concept** | One sentence in ordinary language. |
| **Prediction** | Sign, scale, direction, trend, and expected failure. |
| **Derivation** | Definitions to equation; dimensions; limiting cases. |
| **Rust mapping** | Types, function contract, ownership, errors, allocation, modules. |
| **Evidence** | Known value, boundary, property, convergence/reference, fault. |
| **Discrepancy** | Expected vs observed; cause; whether model, numeric, code, or data. |
| **AI ledger** | What AI supplied; what you verified; what remains borrowed. |
| **Next dependency** | What this unlocks and the exact gate before proceeding. |

**The AI ledger field is critical.** It forces honesty about what is yours and what is borrowed. "AI wrote the test for orthogonal vectors. I verified it against the 3-4-5 triangle case by hand. The NaN case remains untested." This is the kind of entry that prevents understanding debt.

---

## 10. The Question Ladder

Not all questions are equal. The manual defines nine levels. The higher the level, the deeper the understanding required.

| Level | Question type | Example |
|:-----:|---------------|---------|
| 1 | Recall | What are the units of mu? |
| 2 | Calculate | Find circular speed at radius r. |
| 3 | Derive | Derive circular speed from gravity and centripetal acceleration. |
| 4 | Interpret | Why does speed decrease with radius? |
| 5 | Implement | What inputs, units, errors, and tests should `circular_speed` have? |
| 6 | Validate | Which independent formula, property, and reference case would detect a bug? |
| 7 | Falsify | What happens at r=0, huge r, mixed units, non-spherical gravity? |
| 8 | Design | When is two-body sufficient and how is a J2 model introduced without coupling? |
| 9 | Research | Can a hybrid residual model improve drag prediction without violating physical constraints? |

**How to use it:** After each session, write three retrieval prompts and one failure prompt using these levels. Aim for levels 3-7. If you can only answer levels 1-2, you have memorized facts but not understanding. If you can answer level 7 (falsify), you own the concept.

---

## 11. Review Cadence Without a Calendar

Since there is no fixed calendar, review happens at natural breakpoints:

- **End of session:** Write three retrieval prompts and one failure prompt.
- **Before next session:** Answer yesterday's prompts from memory in five minutes. No notes, no AI.
- **After several units:** Re-solve one early problem with no notes and extend the old crate rather than starting over. This tests whether earlier mastery has survived.
- **At each stage gate:** Oral defense, blank-page derivation, code walkthrough, and adversarial test review. You explain the capstone as if presenting to a mission review board.
- **After a release:** Postmortem and dependency map update. What newly became possible? Which weak prerequisite was exposed?
- **Periodically:** Have another engineer reproduce the artifact and challenge your assumptions.

---

## 12. When Stuck: The Reduction Hierarchy

Do not jump to a new subject when stuck. Reduce the problem. Complexity should be earned one assumption at a time.

```
  scalar         before    vector
  2-D            before    3-D
  constant       before    variable
  analytic       before    numerical
  deterministic  before    stochastic
  desktop        before    embedded
  baseline       before    AI
```

**Why this works:** If you cannot solve the scalar version, you will definitely not solve the vector version. If you cannot solve the 2-D case, 3-D will hide your misunderstanding behind extra complexity. Each reduction removes one variable so you can isolate what you actually do not understand.

When you solve the reduced version, add complexity back one assumption at a time. Each addition should produce a new prediction (Step 1 of the loop) before you run the code.

---

## 13. Repository Rules

These rules are enforced across every practice file:

1. **One concept per commit** until the design naturally requires composition.
2. Write the physical story and test cases **before** implementation.
3. Use explicit units in names; progress toward unit and frame types.
4. Run `cargo fmt`, `cargo clippy -- -D warnings`, and `cargo test` before every finished session.
5. Keep an engineering log: prediction, result, discrepancy, cause, change, remaining uncertainty.
6. AI may critique after your first attempt. If it writes code, you must re-derive and retype the essential path from memory later.

**Why these rules:** One concept per commit means your git history is a learning record - each commit is a single idea. Writing the physical story first means you cannot drift into code without a model. Explicit units in names (e.g. `velocity_mps` not `v`) make dimensional errors visible at read time. Running fmt, clippy, and tests before every finish means the repo is always in a reproducible state.

---

## 14. Field Checklists

Use these before declaring a result trustworthy. They are the fast reviews that a mission-grade engineer performs on every artifact.

### Physics and Mathematics Review

- [ ] System boundary and neglected interactions are explicit.
- [ ] Every symbol has meaning, type, units, frame, epoch, sign convention, and valid domain.
- [ ] Dimensions balance; limits and special cases behave physically.
- [ ] The initial/boundary conditions define a solvable problem.
- [ ] Fidelity is justified by the decision being made, not by available code.
- [ ] Uncertainty and sensitivity are reported where inputs/models are uncertain.

### Numerical Review

- [ ] Discretization, solver, tolerances, iteration limits, and failure returns are declared.
- [ ] Step/grid refinement demonstrates observed convergence or explains why it does not.
- [ ] Conserved quantities, residuals, monotonicity, symmetry, or other structural properties are checked.
- [ ] Conditioning, scaling, stiffness, cancellation, overflow/underflow, and non-finite values are considered.
- [ ] A separate implementation, analytic case, published vector, or trusted tool supplies independent evidence.
- [ ] Performance optimization occurs only after a correctness baseline and repeats the full validation.

### Rust and Software Review

- [ ] Public APIs expose units/frame/epoch/failure semantics; illegal states are difficult to construct.
- [ ] Ownership is intentional; clones/allocations/locks are explainable; unsafe is minimal and documented.
- [ ] Domain logic is separate from I/O, UI, networking, and serialization.
- [ ] Errors are typed and actionable; no silent fallback, truncation, saturation, or last-iteration return.
- [ ] Tests cover examples, boundaries, properties, malformed inputs, faults, and regression vectors.
- [ ] Build, dependencies, configuration, scenario, compiler, seed, and output schema are reproducible.

### AI/ML Review

- [ ] A non-ML or simpler ML baseline exists and the improvement is decision-relevant.
- [ ] Raw data, labels, splits, preprocessing, leakage checks, and licenses are versioned.
- [ ] Metrics match operational costs; slices expose rare regimes and failure modes.
- [ ] Calibration, OOD, robustness, shift, missing data, and uncertainty are evaluated.
- [ ] Latency, memory, energy, update, rollback, monitoring, security, and human handoff are designed.
- [ ] Safety constraints and authority remain outside an unconstrained generative model.

### Mission/System Review

- [ ] Stakeholder need traces to technical requirements, design, implementation, and verification evidence.
- [ ] Interfaces include data, physical, electrical, timing, environmental, operational, and organizational assumptions.
- [ ] Hazards, threats, faults, degraded modes, recovery, and contingency operations are exercised.
- [ ] Configuration and provenance allow exact replay of a result or anomaly.
- [ ] A reviewer can distinguish verification (built right) from validation (right thing/model for the use).
- [ ] Known limitations and residual risk are written in language a decision-maker can act on.

---

## 15. How to Ask Better Questions

When asking for help (from AI, a mentor, or a peer), use this form:

> Here is the physical story; here are my units, frame, assumptions, derivation, predicted result, Rust API, observed result, and tests. The discrepancy is X. Which assumption or implementation step should I inspect first, and what experiment would distinguish the possibilities?

This produces learning. "Give me the code" produces dependency.

**Why this matters:** The act of writing out the full context - physical story, derivation, prediction, code, observed result - often reveals the answer before you even ask the question. Even when it does not, the person (or AI) reviewing your question can give you a *diagnostic* answer (which step to inspect) rather than a *replacement* answer (here is the working code). Diagnostic answers teach. Replacement answers create understanding debt.

---

## Back to the root

[<- README](../README.md)  |  [<- Documentation Index](INDEX.md)  |  [Formula Reference](formula_reference.md)  |  [Concept Map](concept_map.md)
