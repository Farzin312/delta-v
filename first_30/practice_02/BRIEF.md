# Session 02: Turn algebra into tested functions

> Mission 1: Equation to Domain Type | Difficulty: | | Status: NOT STARTED
>
> **Repository destination:** `crates/foundation/src/kinematics.rs`
> (Note: foundation crate merges into units during graduation)

---

## ATTEMPT PAGE

Work through this page BEFORE opening the Debrief Page below.

### Three columns

| Mathematics | Physical Meaning | Rust / Engineering |
|-------------|-----------------|-------------------|
| Rearranging equations and inverse relationships | Average speed and round-trip consistency | Parameters, return values, unit tests |

---

### Integrated Build

Implement `speed(distance, time)` and `distance(speed, time)` as two pure functions. A rover moves 126 m in 42 s. Compute average speed. Then rearrange the same relation to recover distance from speed and time.

---

### By-Hand Practice

- [ ] Rearrange d = v x t for every variable. Write all three forms: v = d/t, d = v x t, t = d/v
- [ ] State the valid domain of time. Can time be zero? Can it be negative? Why or why not?
- [ ] Predict a round-trip property. If you compute speed from (d, t), then compute distance from (speed, t), do you get d back? Prove it algebraically.

---

### Prediction Before Code

```
Sign:         (positive / negative / zero?)
Scale:        (what order of magnitude for 126 m / 42 s?)
Direction:    (what happens to speed as distance increases at fixed time?)
Units:        (what units? how do they combine?)
Failure case: (what input breaks v = d / t?)
```

Sketch the API:

```
Function names:   ___________ and ___________
Parameters:       (names and types for each)
Return types:     ___________
Test names:       1. ___________
                  2. ___________
                  3. ___________
```

---

### Independent Rust Drill

Separate from the physics build. From a blank file:

- [ ] Write three small inverse functions (e.g., `double` and `halve`, `celsius_to_fahrenheit` and `fahrenheit_to_celsius`)
- [ ] Test that composition returns the starting value: `assert_eq!(halve(double(42.0)), 42.0)`
- [ ] Write a test that checks a large-scale value

---

### Tests Written First

Name your tests and write expected values by hand:

```
1. test_known_speed:        126 m / 42 s = ___ m/s
2. test_round_trip:         speed(126, 42) then distance(result, 42) = ___ m
3. test_large_scale_value:  1_000_000 m / 1000 s = ___ m/s
```

---

### Gate: Do Not Open the Debrief Until

- [ ] Hand result exists (computed speed and round-trip on paper)
- [ ] API is sketched
- [ ] Tests are named
- [ ] First implementation attempt compiles or has a diagnosed error

---

## DEBRIEF PAGE

### Hint Ladder

**Hint 1.** Derive first. Write v = d/t on paper. Write d = v x t. Check dimensions: (m/s) = m / s and m = (m/s) x s.

**Hint 2.** Make two pure functions. Each takes parameters, returns a value, no printing inside.

**Hint 3.** Test a property, not just a number. The round-trip property (speed then distance returns original d) is stronger than checking a single value.

---

### Failure Campaign

- [ ] Pass zero time (t = 0) to `speed`. What happens? Inspect IEEE-754 infinity. Is this a bug or a domain issue?

- [ ] Pass negative time. Does speed come out negative? Is negative speed meaningful here?

- [ ] Pass NaN. Does NaN propagate silently?

Classify each: **Bug**, **Numerical limit**, or **Model limitation**.

---

### Repository Destination

The kinematics functions graduate to `crates/foundation/src/kinematics.rs`
when Session 04 introduces unit types. For now, keep them in this session.

---

### Python / Independent Check

Use Python ONLY to compare floating-point output, not to design the API:

```python
d, t = 126.0, 42.0
v = d / t
print(f"{v} m/s")
assert d == v * t  # round-trip
```

---

### Reference Shape

```rust
fn speed_mps(distance_m: f64, time_s: f64) -> f64 { distance_m / time_s }
fn distance_m(speed_mps: f64, time_s: f64) -> f64 { speed_mps * time_s }
```

---

### Mastery Claim

After completing this session, you should be able to say:

> "I can create a metamorphic test (round-trip property) and explain why it is stronger than a duplicate example."

Write your explanation in Notes.

---

### Delayed Gate (complete at least ONE WEEK after the session)

- [ ] Recreate both functions from memory
- [ ] Solve a changed case by hand (e.g., 500 m / 25 s)
- [ ] Explain the failure experiment and operating domain
- [ ] Reproduce from clean clone

---

## Session Notes

- **What surprised me:**
- **What I trust:**
- **Where it fails:**
- **What this unlocks:**
- **Round-trip property explanation:**
- **Last practiced:** (date)
- **Delayed gate date:** (date + 1 week)
- **Mastery gate passed:** [ ] yes [ ] not yet
