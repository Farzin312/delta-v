# Session BRIEF.md Template — Attempt Page + Debrief Page Format

> This document defines the format for all session BRIEF.md files.
> It implements the Frontier Engineer Field Manual's two-page session design.
> The session generator (`scripts/new_session.py`) should be updated to
> produce this format for new sessions.

## Structure

Every session BRIEF.md has exactly two sections:

1. **ATTEMPT PAGE** — the learner works here first, no solutions shown
2. **DEBRIEF PAGE** — revealed only after the attempt is complete

```
# Session NN: <title>

> Mission N: <mission name> | Difficulty: <bars> | Status: NOT STARTED
>
> **Repository destination:** crates/<crate>/src/<module>.rs
> **Crate graduation gate:** Session NN (what unlocks graduation)

---

## ATTEMPT PAGE

Work through this page BEFORE opening the Debrief Page below.

### Three columns

| Mathematics        | Physical Meaning          | Rust / Engineering        |
|--------------------|---------------------------|---------------------------|
| <math concepts>    | <physics concepts>        | <rust concepts>           |

### Integrated Build
<the concrete thing to build — one sentence, specific>

### By-Hand Practice
- [ ] <2-3 manual exercises before code>
- [ ] <estimate, convert, draw, dimensional check>

### Prediction Before Code
<structured checklist: sign, scale, direction, units, failure case>
<API signature sketch: function name, parameters, return type, test names>

### Independent Rust Drill
<a language-fluency exercise SEPARATE from the physics build>
<from a blank file: write X, Y, Z>

### Tests Written First
<name 3-4 tests BEFORE implementation>
<write expected values by hand>

### Gate: Do Not Open the Debrief Until
- [ ] Hand result exists
- [ ] API is sketched
- [ ] Tests are named
- [ ] First implementation attempt compiles or has a diagnosed error

---

## DEBRIEF PAGE

### Hint Ladder
<3 progressive hints, only read when stuck>

### Failure Campaign
<specific way to break the code and what to observe>
<classify each failure: bug / numerical limit / model limitation>

### Repository Destination
<where the code migrates in the workspace crate structure>

### Python / Independent Check
<how to cross-validate with Python, only after Rust output exists>

### Reference Shape
<minimal code skeleton to compare against — only after attempt>

### Mastery Claim
<a single sentence the learner must be able to defend>

### Delayed Gate (1 week later)
- [ ] Recreate API from memory
- [ ] Solve changed case by hand
- [ ] Explain failure experiment and operating domain
- [ ] Reproduce from clean clone

---

## Session Notes
<discovery log: surprised, trust, fails, unlocks, mastery explanation>
```

## Design Rules

1. **No solutions on the Attempt Page.** The attempt page teaches through
   structure, not answers. It tells you WHAT to do, not HOW.

2. **The Debrief Page is earned.** The gate exists to prevent opening
   solutions before attempting. The struggle to derive, sketch, and fail
   IS the learning.

3. **By-hand practice is mandatory.** Every session has 2-3 exercises
   that must be done on paper before code. This builds physical intuition
   and catches prediction errors.

4. **The Rust drill is separate from the physics.** Language fluency and
   physics understanding are different skills. Practice them separately
   so gaps in one don't mask gaps in the other.

5. **Tests are named first.** Naming tests before implementation forces
   you to think about behavior, not mechanism. It also prevents tests
   from merely blessing whatever code you write.

6. **The failure campaign is deliberate.** You must try to break your
   code. Success that can't survive a stress test is not understanding.

7. **The delayed gate enforces spacing.** A concept isn't mastered until
   you can retrieve it after a week. This is non-negotiable.
