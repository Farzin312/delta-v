# Daily Practice Guide

> Open this file every morning. It tells you exactly what to do.

This guide implements the Frontier Engineer Field Manual's daily system.
You run four lanes every day: retrieval, mathematics, programming craft,
and integrated build. No lane is optional, but the time blocks flex.

---

## The Three Modes

Pick ONE mode based on your available time. Don't mix modes mid-day.

### Mode A: Full Session (3 hours 25 minutes)

The complete learning engine. Use this when you have the full morning or
evening. The order matters — it protects independent reasoning.

```
 15 min  Retrieval warm-up     Closed-book recall from yesterday
 45 min  Mathematics           Formal lesson + 2-4 hand problems
 45 min  Programming craft     Blank-file Rust drill (unrelated to physics task)
 45 min  Physics/Engineering   System diagram, assumptions, derivation
 45 min  Integrated build      Implement, test, falsify, document
 10 min  Exit review           What changed? What's borrowed? Next review date?
```

### Mode B: Minimum Viable Day (75 minutes)

When life is busy. Three compact blocks. Still covers all four lanes.

```
 20 min  Retrieval + ONE hand problem
 25 min  ONE Rust concept from a blank file
 30 min  ONE integrated test or experiment
```

### Mode C: Review Day (45-60 minutes)

Use on Day 6-7 of the weekly rhythm. No new concepts. Pure retrieval,
interleaving, and defense.

```
 15 min  Retrieval warm-up
 20 min  Mixed review: pick 3 past sessions, restate the core idea closed-book
 15 min  Pick ONE session, redo the by-hand exercise from memory
 10 min  Update status in CATALOG.md
```

---

## How to Run Each Block

### 1. Retrieval Warm-Up (15 min)

Close everything. No notes, no code, no AI. Grab paper or a blank text file.

Write down from memory:
- The key equation from yesterday's session
- The API signature you wrote yesterday
- The bug or failure you found yesterday
- One Rust syntax pattern you used yesterday

If you can't recall something, mark it with a question mark. Do NOT look it
up yet — the struggle to recall IS the learning. Look it up at the end of
the block and add it to your error log.

**Output:** A dated recall sheet. Save it in `docs/learning-log/`.

### 2. Mathematics Block (45 min)

Structure:
1. **Read or watch the formal lesson** for the current session's math concept
   (MIT OCW, OpenStax, Khan Academy — whichever matches the BRIEF.md)
2. **Solve 2-4 hand problems** on paper. Not code. Paper.
3. **Repair one gap** if the diagnostic revealed a weak prerequisite node.

**Output:** A worked derivation with dimensional checks. Scan or photograph
it. Put it in the session's Notes section.

### 3. Programming Craft Block (45 min)

This block is SEPARATE from the physics task. It builds Rust fluency
independently. Pick ONE drill mode per day:

| Mode | Task | Time |
|------|------|------|
| **Syntax retrieval** | From a blank file: write a struct, an enum with 3 variants, an impl block, a Result-returning function, an iterator chain, and a test. No IDE autocomplete. | 15-30 min |
| **Ownership tracing** | Take a function you wrote previously. Annotate every variable: owner, move, borrow, lifetime, allocation site. Explain why each clone or reference is needed. | 15-30 min |
| **Code reading** | Pick one function from the Rust std library (e.g., `Vec::retain`, `Iterator::fold`). Read the source. Explain its contract, error path, and ownership model. | 15-30 min |
| **Debugging** | Introduce a deliberate bug in old code (wrong sign, off-by-one, type confusion). Then diagnose it from scratch using compiler messages and reasoning, not undo. | 15-30 min |
| **Refactoring** | Take a function you wrote. Separate I/O from domain logic, or replace a bool flag with an enum. | 15-30 min |
| **Algorithms** | Implement a small data structure (ring buffer, min-heap) or traversal. Benchmark it. | 15-30 min |
| **Library study** | Read the docs for one crate method. Write a tiny example. Inspect the types. Then reproduce it from memory. | 15-30 min |

**Output:** A small commit or a note in your learning log.

### 4. Physics/Engineering Block (45 min)

Structure:
1. **Draw the physical system** — free-body diagram, circuit, thermal
   network, orbit geometry. Label every force, frame, and boundary.
2. **State assumptions** — what are you simplifying away? Constant mass?
   Point particle? No drag? Rigid body?
3. **Estimate the scale** — before computing, predict the order of
   magnitude. (See `docs/predict_practice/README.md`)
4. **Derive the equation** — from definitions, not from memory. Check
   dimensions on both sides.

**Output:** A physical story: diagram + assumptions + equation + limiting
cases.

### 5. Integrated Build Block (45 min)

This is where math meets code. Open the session's BRIEF.md.

1. Follow the **Attempt Page** (Steps 1-4 of the 7-step loop)
2. Write tests FIRST (Step 5)
3. Implement the smallest function that satisfies the derivation
4. Run `cargo test`
5. **Falsify** (Step 6): try to break it — extreme values, invalid inputs,
   wrong units. Classify each failure.
6. **Teach** (Step 7): write what you learned in the Notes section.

Before finishing the build block, run:
```bash
cargo fmt
cargo clippy -- -D warnings
cargo test
```

**Output:** A committed session with passing tests and a filled Notes section.

### 6. Exit Review (10 min)

Answer three questions. Write the answers in `docs/learning-log/`:

1. **What changed in my mental model?** (One sentence)
2. **What remains borrowed?** (Things AI explained that I haven't re-derived)
3. **When is the next review?** (Tomorrow recall, 1-week retrieval, 1-month)

---

## Weekly Rhythm

| Day | Focus | Lane Emphasis |
|-----|-------|---------------|
| **1** | New concept + baseline | Math + Physics (predict, derive, known case) |
| **2** | Language depth + second representation | Programming craft (blank-file drill) |
| **3** | Numerical/experimental variation | Integrated build (convergence, error sweeps) |
| **4** | Debugging and edge cases | Integrated build (falsify, failure campaign) |
| **5** | Integration and documentation | Finish session, update CATALOG, write Notes |
| **6** | Mixed review and defense | Review Day (Mode C) |
| **7** | Rest, wonder, or light reading | No structured blocks. Read a paper or watch a talk. |

---

## How to Know Which Session to Work On

1. Open `first_30/CATALOG.md`
2. Find the first session with status `NOT STARTED` or `IN PROGRESS`
3. Open its `BRIEF.md`
4. Follow the Attempt Page -> Debrief Page structure
5. Update the status line in BRIEF.md when done:
   - `NOT STARTED` -> haven't begun
   - `IN PROGRESS` -> working through the steps
   - `TESTS PASSING` -> implementation done, tests green
   - `MASTERY GATE PASSED` -> can derive from memory, explain, show a failure

---

## Where Everything Lives

You practice in FIVE places. Each serves a different purpose.

### 1. Sessions (integrated build + physics + math, together)
`first_30/practice_NN/`

This is where math meets code. Each session integrates a physics problem,
a math derivation, and a Rust implementation into one working artifact.
Follow the BRIEF.md Attempt Page -> Debrief Page structure.

### 2. Drills (Rust language fluency, separate from physics)
`drills/NN-name/`

Short, focused exercises for Rust syntax, ownership, iterators, traits.
You do these from a blank file. They are SEPARATE from the sessions because
language fluency and physics understanding are different skills. If you
can implement a physics equation but can't write a struct from memory,
you have a language gap, not a physics gap.

See `drills/README.md` for the full progression.

### 3. Diagnostics (readiness assessment)
`diagnostics/`

Before starting a new module, take its diagnostic. These identify weak
prerequisite nodes so you can repair them before proceeding. No notes,
no AI, timed. Score honestly.

See `diagnostics/README.md` for the diagnostic index.

### 4. Workspace Crates (graduated concepts)
`crates/units/`, `crates/math/`, `crates/numerics/`, etc.

When a concept from a session is fully understood (mastery gate + delayed
gate passed), it graduates to its target crate. This is where stable,
tested, reusable code lives. You don't practice here - you migrate here.

See `docs/knowledge_tracker.md` for which sessions feed which crates.

### 5. Learning Log (your engineering notebook)
`docs/learning-log/`

Daily recall sheets, exit reviews, AI ledgers. This is your personal
engineering notebook. Date every entry.

---

## What to Do Each Day (Quick Reference)

```
MORNING ROUTINE:

1. Open docs/daily_practice.md          (this file)
2. Open first_30/CATALOG.md             (find your current session)
3. Decide your mode:
   - Mode A (3h25m): full session
   - Mode B (75min): minimum viable day
   - Mode C (45-60m): review day
4. Run the four lanes:
   a. Retrieval warm-up (15 min)
   b. Math OR Programming drill (45 min)  [alternate daily]
   c. Physics/engineering derivation (45 min)
   d. Integrated build in the session (45 min)
   e. Exit review (10 min)

BEFORE STARTING A NEW MODULE:
   Take the diagnostic in diagnostics/

FOR RUST FLUENCY:
   Do one drill from drills/ per day (15-30 min)

TO TRACK PROGRESS:
   Update docs/knowledge_tracker.md after each session
```

---

## When to Graduate a Concept to a Crate

After you complete a session and its delayed gate (1-week retrieval), if
the concept is stable:

1. Copy the tested function/type into the target crate module
   (e.g., `crates/units/src/angle.rs`)
2. Add tests to the crate
3. Run `cargo test --workspace`
4. Update the crate's lib.rs status from "Stub" to the module name
5. Commit with: `feat(units): graduate angle type from session 06`

**Never graduate before the delayed gate.** The 1-week retrieval test is
what confirms you actually own the concept.

---

## The Finish Line for Each Session

A session is DONE when ALL of these are true:

- [ ] Prediction was written before any code
- [ ] Derivation includes dimensional check
- [ ] Implementation compiles and passes `cargo test`
- [ ] At least one known-value test
- [ ] At least one boundary test
- [ ] At least one property or independent-reference test
- [ ] At least one failure case identified and classified
- [ ] Operating domain declared in comments
- [ ] Notes section filled in
- [ ] `cargo fmt` clean
- [ ] `cargo clippy -- -D warnings` clean

The **delayed gate** (1 week later) is separate:
- [ ] Can recreate the essential API from memory
- [ ] Can solve a changed numerical case by hand
- [ ] Can explain the failure experiment and operating domain
- [ ] Can run tests and reproduce output from a clean clone

---

## Quick Command Reference

```bash
# Work on a session
cd first_30/practice_01
cat BRIEF.md                    # read the brief
cargo test                      # run tests
cargo clippy -- -D warnings     # lint
cargo fmt                       # format

# Check the whole workspace (crates only, not sessions)
cargo check --workspace
cargo test --workspace

# Python validation
cd python && pip install -e '.[dev]'
pytest -v

# Session management
python3 scripts/new_session.py list     # see all sessions
python3 scripts/new_session.py doctor   # health check
```

---

## AI Protocol (Reminder)

- **Allowed early:** extra practice problems, critique of your work,
  locating docs, explaining compiler errors after your diagnosis
- **Quarantined:** full solutions before your attempt, code you can't
  retype, derivations with undefined symbols, tests written after
  implementation only

**Four-pass rule:**
1. Independent attempt (predict, sketch, derive, design API, list tests)
2. Targeted assistance (hint, counterexample, critique — not replacement)
3. Verification (official sources, tests, tools, failure inspection)
4. Reconstruction (reproduce reasoning and code without the model, later)

**AI ledger:** In your learning log, note what AI supplied, what you
verified independently, and what remains borrowed.
