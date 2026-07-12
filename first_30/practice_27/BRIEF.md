# Session 27: Implement midpoint before RK4

> Stage 2 | Difficulty: ||||| | Status: NOT STARTED

## The Problem

Implement the midpoint method for a generic 1-D derivative and compare one step with Euler on the spring.

## What This Teaches

| Dimension | Focus |
|-----------|-------|
| Math / Physics | Second-order integration |
| Rust / Engineering | function composition, intermediate states |

---

## The Learning Loop

Follow all seven steps. Do not skip. Each step catches a failure the others miss. See [docs/method.md](../../docs/method.md) for the full explanation of why each step exists.

### Step 1: PREDICT

Write your prediction BEFORE any calculation or code. No AI. No hints.

Fill in:

```
Sign:         (positive / negative / zero?)
Scale:        (order of magnitude)
Direction:    (which way? increasing / decreasing?)
Units:        (what units should the answer have?)
Failure case: (what input would break this?)
```

### Step 2: EXPLAIN

Draw the physical story in 5 sentences or less. Name:

- System boundary (what is inside / outside the model?)
- Coordinate frame (which axis points where?)
- Assumptions (what are you simplifying away?)
- Inputs (what values go in?)
- Outputs (what comes out?)

### Step 3: DERIVE

Write the equation from definitions. Show dimensional analysis.

```
Equation:
  (write it here)

Dimensional check:
  (do the units match on both sides?)

Limiting cases:
  t = 0:    (what happens?)
  t -> inf: (what happens?)
  a = 0:    (what happens?)
```

### Step 4: IMPLEMENT

Write the smallest pure Rust function that matches your derivation.

Rules:
- One concept per function
- No hidden I/O (no println! inside a pure math function)
- No premature abstraction (no framework, no trait hierarchy)
- Explicit units in variable names (e.g. `time_s` not `t`)

### Step 5: TEST

Write tests in this order. Each catches a different class of error:

1. **Known value** - a textbook or hand-calculated result
2. **Boundary** - zero, empty, maximum, or degenerate input
3. **Property** - a structural invariant (symmetry, conservation, monotonicity)
4. **Independent reference** - cross-check with a different formula or tool (if available)

### Step 6: FALSIFY

Deliberately break your code. Try:

- Extreme values (very large, very small)
- Invalid inputs (negative, NaN, infinity)
- Wrong units (pass seconds where meters expected)
- Model violations (what if acceleration is not constant?)

For each failure, classify it:

- **Bug** - your code is wrong. Fix it.
- **Numerical limit** - your math is right but the computer cannot represent it. Document it.
- **Model limitation** - your equation is correct for its assumptions but they no longer hold. Declare the valid domain.

### Step 7: TEACH

Write what you learned in the Notes section below. Explain:

- What surprised you (where did prediction differ from reality?)
- What you trust and why
- Where the code fails and what the valid domain is
- What concept this unlocks next

---

## Hints (only if stuck after Steps 1-3)

1. Think about what physical quantity you are computing and what units it must have.
2. Consider edge cases: what inputs are invalid? What should happen?

## Checklist

- [ ] Prediction written before any code
- [ ] Derivation includes dimensional check
- [ ] Implementation compiles with `cargo build`
- [ ] At least one known-value test passes
- [ ] At least one boundary test passes
- [ ] At least one property or independent-reference test
- [ ] `cargo fmt` clean
- [ ] `cargo clippy -- -D warnings` clean
- [ ] At least one failure case identified and classified (bug / numerical / model)
- [ ] Operating domain declared in comments or docs
- [ ] Engineering log entry written
- [ ] Notes section filled in below

## Notes

_Write your discoveries, surprises, and remaining questions here as you work._

- **What surprised me:**
- **What I trust:**
- **Where it fails:**
- **What this unlocks:**
- **Last practiced:** (date)
- **Mastery gate passed:** [ ] yes [ ] not yet
