# Session 03: Represent failure honestly

> Mission 1: Equation to Domain Type | Difficulty: | | Status: NOT STARTED
>
> **Repository destination:** `crates/foundation/src/error.rs`

---

## ATTEMPT PAGE

Work through this page BEFORE opening the Debrief Page below.

### Three columns

| Mathematics | Physical Meaning | Rust / Engineering |
|-------------|-----------------|-------------------|
| Domains, inequalities, finite values | Physical validity versus algebraic definition | Result, enums, match, ? operator |

---

### Integrated Build

Redesign average speed so zero, negative, NaN, or infinity elapsed time cannot silently return a misleading value. Return a typed error instead.

---

### By-Hand Practice

- [ ] List mathematical and physical domains separately. Mathematically, division is defined for all t != 0. Physically, what values of t are valid for elapsed time?
- [ ] Classify these four cases: t = 0, t < 0, t = NaN, t = infinity. Which are mathematically undefined? Which are physically meaningless? Which are both?
- [ ] Write the error contract before code. What error variants do you need? Name them.

---

### Prediction Before Code

```
Sign:         (what sign should the result have for valid inputs?)
Scale:        (same as Session 02 for valid inputs)
Direction:    (N/A — focus is on the error paths)
Units:        (m/s for valid inputs; what does an error "unit" look like?)
Failure case: (this IS the failure case session — list all 4 invalid inputs above)
```

Sketch the API:

```
Error enum name:  ___________
Variants:         1. ___________  (which invalid input?)
                  2. ___________  (which invalid input?)
Function name:    ___________
Parameters:       ___________
Return type:      Result<___________, ___________>
Test names:       1. ___________  2. ___________  3. ___________  4. ___________
```

---

### Independent Rust Drill

Separate from the physics build. From a blank file:

- [ ] Create a small parser function returning a custom enum with at least three error variants
- [ ] Use `match` to handle each variant explicitly (no wildcard `_ =>`)
- [ ] Use the `?` operator to propagate an error from a helper function

---

### Tests Written First

```
1. test_zero_time:          speed(100, 0) should return Err(___________)
2. test_negative_time:      speed(100, -5) should return Err(___________)
3. test_nan_time:           speed(100, NaN) should return Err(___________)
4. test_infinite_time:      speed(100, infinity) should return Err(___________)
5. test_valid_input:        speed(100, 10) should return Ok(10.0)
```

---

### Gate: Do Not Open the Debrief Until

- [ ] Hand result exists (you classified all four invalid cases on paper)
- [ ] API is sketched (error enum and function signature written)
- [ ] Tests are named (all five)
- [ ] First implementation attempt compiles or has a diagnosed error

---

## DEBRIEF PAGE

### Hint Ladder

**Hint 1.** An equation has a domain. v = d/t is defined for t != 0, but physically t must also be positive and finite.

**Hint 2.** Validate before division. Check all preconditions before you ever divide.

**Hint 3.** NaN defeats ordinary comparisons. `NaN > 0` is false, and `NaN < 0` is also false. `f64::is_nan()` or `f64::is_finite()` is the only reliable check.

---

### Failure Campaign

- [ ] Use only `time_s <= 0.0` as your guard. Show how NaN passes through. This is why you need `is_finite()`.

- [ ] Use `time_s > 0.0` without checking for infinity. Show how infinity passes through and produces zero speed (d / inf = 0).

- [ ] Compare: what does Python do with `d / float('nan')`? Does it error or return NaN? How does this differ from your Rust Result approach?

Classify each: **Bug** (fix the guard), **Numerical limit** (document IEEE-754 behavior), **Model limitation** (declare the domain).

---

### Repository Destination

The error type graduates to `crates/foundation/src/error.rs` and becomes
the shared error type for all physics functions in the workspace.

---

### Python / Independent Check

Construct the same NaN comparison in Python and compare behavior:

```python
import math
t = float('nan')
print(t > 0)   # False
print(t < 0)   # False
print(t == t)  # False — NaN is never equal to itself
print(math.isnan(t))  # True — this is the reliable check
```

Notice: Python silently returns NaN for `100.0 / t`. Your Rust function
returns `Err(NonFiniteInput)`. Which is more useful for engineering?

---

### Reference Shape

```rust
#[derive(Debug, PartialEq)]
enum PhysicsError {
    NonPositiveTime,
    NonFiniteInput,
}

fn speed_mps(d: f64, t: f64) -> Result<f64, PhysicsError> {
    if !t.is_finite() {
        return Err(PhysicsError::NonFiniteInput);
    }
    if t <= 0.0 {
        return Err(PhysicsError::NonPositiveTime);
    }
    Ok(d / t)
}
```

---

### Mastery Claim

> "I can explain why panic, Option, Result, and sentinel values communicate different contracts, and why Result is the right choice here."

Write your explanation in Notes.

---

### Delayed Gate (complete at least ONE WEEK after the session)

- [ ] Recreate the error enum and function from memory
- [ ] Solve a changed case by hand (different distance and time values)
- [ ] Explain the NaN comparison trap and how your guard prevents it
- [ ] Reproduce from clean clone

---

## Session Notes

- **What surprised me:**
- **What I trust:**
- **Where it fails:**
- **What this unlocks:**
- **Why Result over panic/Option/sentinel:**
- **Last practiced:** (date)
- **Delayed gate date:** (date + 1 week)
- **Mastery gate passed:** [ ] yes [ ] not yet
