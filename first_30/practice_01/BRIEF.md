# Session 01: Make an equation executable

> Mission 1: Equation to Domain Type | Difficulty: | | Status: NOT STARTED
>
> **Repository destination:** `crates/units/src/units.rs`
> **Crate graduation gate:** Session 04 (newtype quantities)

---

## ATTEMPT PAGE

Work through this page BEFORE opening the Debrief Page below.
Do not skip to the debrief. The struggle IS the learning.

### Three columns

| Mathematics | Physical Meaning | Rust / Engineering |
|-------------|-----------------|-------------------|
| Units, scientific notation, proportional reasoning | Signal travel and dimensional consistency | Cargo, bindings, f64, functions, assertions |

---

### Integrated Build

Compute distance travelled by light in a measured interval and print both SI scales.

A signal travels at 299,792,458 m/s for 12.5 ms. Predict the distance scale, convert milliseconds to seconds, compute meters and kilometers, and print both with units.

---

### By-Hand Practice

Do these on paper BEFORE writing any code.

- [ ] Estimate the order of magnitude before calculating. Will the answer be in the thousands? Millions? Billions? Write your estimate.
- [ ] Convert milliseconds to seconds in a separate line. Write: 12.5 ms = 12.5 x 10^-3 s = 0.0125 s
- [ ] Write the unit cancellation explicitly. Show how (m/s) x (s) = m. Cross out the seconds.

---

### Prediction Before Code

Fill this in. No code, no AI, no hints.

```
Sign:         (positive / negative / zero?)
Scale:        (order of magnitude — millions? billions?)
Direction:    (increasing / decreasing / constant as time grows?)
Units:        (what units should the answer have?)
Failure case: (what input would break this or give a wrong answer?)
```

Then sketch the API:

```
Function name:    ___________
Parameters:       (names and types)
Return type:      ___________
Test names:       1. ___________
                  2. ___________
                  3. ___________
```

---

### Independent Rust Drill

This drill is SEPARATE from the physics build. Its purpose is language
fluency, not physics.

From a blank file (no copy-paste, no AI autocomplete), write:
- [ ] A pure multiply function: `fn multiply(a: f64, b: f64) -> f64`
- [ ] A named constant: `const SPEED_OF_LIGHT_MPS: f64 = 299_792_458.0;`
- [ ] Formatted output: print a value with `{}` and `{:.4}` format specifiers
- [ ] Two assertions: `assert_eq!(...)` for known values

Time yourself. If you can't do this from a blank file in under 10 minutes,
you need more syntax retrieval practice before proceeding.

---

### Tests Written First

Name your tests BEFORE writing implementation. Write the test names here:

```
1. test_zero_duration          — light traveling for 0 seconds
2. test_one_full_second        — light traveling for 1.0 second exactly
3. test_missing_prefix_conversion — deliberately testing the ms->s conversion path
```

What should each test assert? Write the expected values by hand:

```
1. test_zero_duration:           distance = ___ m
2. test_one_full_second:         distance = ___ m  (= c exactly)
3. test_missing_prefix:          12.5 ms should give distance = ___ m
```

---

### Gate: Do Not Open the Debrief Until

- [ ] Hand result exists (you computed the answer on paper)
- [ ] API is sketched (function signatures written above)
- [ ] Tests are named (all three test names written above)
- [ ] First implementation attempt compiles or has a diagnosed error

---

## DEBRIEF PAGE

Open this section ONLY after completing the Attempt Page above.

### Hint Ladder

Only read the next hint if you are stuck.

**Hint 1.** milli means 10^-3. To convert milliseconds to seconds, multiply by 10^-3 (or divide by 1000).

**Hint 2.** d = v x t. Distance equals speed multiplied by time. Make sure time is in seconds before multiplying.

**Hint 3.** Name conversions instead of hiding them. Write a separate line `let time_s = time_ms / 1000.0;` rather than inlining `time_ms / 1000.0` inside the multiply. Explicit is better than clever.

---

### Failure Campaign

After your implementation works, deliberately break it:

- [ ] **Remove the millisecond conversion.** Pass 12.5 directly as seconds instead of converting from ms. Observe the 1000x error. What distance do you get? How would you detect this in a test?

- [ ] **Pass NaN as input.** What happens? Does your function return NaN silently? Should it?

- [ ] **Pass negative time.** Is negative time physically meaningful for signal travel? Should the function accept it?

For each failure, classify: **Bug** (fix it), **Numerical limit** (document it), or **Model limitation** (declare the valid domain).

---

### Repository Destination

When this concept graduates (after Session 04), the unit conversion logic
lives here:

```
crates/units/src/units.rs
```

For now, keep everything in this session's `src/main.rs` (or `src/lib.rs`).
Graduation happens only after the mastery gate and the 1-week delayed gate.

---

### Python / Independent Check

Recompute in a one-line Python script ONLY AFTER your Rust result is predicted
and computed:

```python
c = 299_792_458.0  # m/s
t_ms = 12.5
t_s = t_ms * 1e-3
d_m = c * t_s
print(f"{d_m:.4} m")
print(f"{d_m / 1000:.4} km")
```

Does your Rust output match? If not, find the discrepancy before proceeding.

---

### Reference Shape

Compare ONLY after your attempt. This is a minimal shape, not the answer.

```rust
const C_MPS: f64 = 299_792_458.0;

fn distance_m(speed_mps: f64, time_s: f64) -> f64 {
    speed_mps * time_s
}
```

Your implementation may differ — more validation, different structure, better
naming. The reference shape confirms you're on the right track, not that you
must match it exactly.

---

### Mastery Claim

After completing this session, you should be able to say:

> "Compiling successfully does not prove physical correctness. I can explain why."

Can you? Write your explanation in the Notes section below.

---

### Delayed Gate (complete at least ONE WEEK after the session)

- [ ] Recreate the essential API from memory (no notes, no AI)
- [ ] Solve a changed numerical case by hand (e.g., 45.3 ms instead of 12.5 ms)
- [ ] Explain the failure experiment and the operating domain
- [ ] Run `cargo test` and reproduce the output from a clean clone

Do not check these off until a full week has passed. Spacing is the point.

---

## Session Notes

_Write your discoveries, surprises, and remaining questions here as you work._

- **What surprised me:**
- **What I trust:**
- **Where it fails (operating domain):**
- **What this unlocks next:**
- **Mastery claim explanation** (why compiling != correct):
- **Last practiced:** (date)
- **Delayed gate date:** (date + 1 week)
- **Mastery gate passed:** [ ] yes [ ] not yet
