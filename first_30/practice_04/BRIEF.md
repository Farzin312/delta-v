# Session 04: Make units visible in types

> Mission 1: Equation to Domain Type | Difficulty: || | Status: NOT STARTED
>
> **Repository destination:** `crates/units/src/lib.rs`
> **This is the crate graduation gate** — units defined here become the
> foundation for every other crate.

---

## ATTEMPT PAGE

Work through this page BEFORE opening the Debrief Page below.

### Three columns

| Mathematics | Physical Meaning | Rust / Engineering |
|-------------|-----------------|-------------------|
| Dimensional analysis | Preventing unit swaps and scale mistakes | Tuple structs, impl blocks, Copy, newtype pattern |

---

### Integrated Build

Define `Meters`, `Seconds`, and `MetersPerSecond` as distinct types with validated constructors. Compute speed from typed distance and typed time, where the caller cannot swap the two arguments.

---

### By-Hand Practice

- [ ] Write the dimensions of each quantity: [M] for meters, [T] for seconds, [L/T] for speed. Show that d/t has dimensions [L/T].
- [ ] Identify operations that should compile: `Meters + Meters`, `Meters / Seconds -> MetersPerSecond`
- [ ] Identify operations that should be IMPOSSIBLE: `Meters + Seconds`, `Seconds + MetersPerSecond`. Why? What would the result even mean?

---

### Prediction Before Code

```
Sign:         (same as before for valid inputs)
Scale:        (same as before)
Direction:    (same as before)
Units:        (the whole point — Meters, Seconds, MetersPerSecond are now types)
Failure case: (this session prevents an entire class of failures at compile time)
```

Sketch the API:

```
Type names:      Meters, Seconds, MetersPerSecond
Constructors:    Meters::new(f64) -> Result<Meters, ___>
                 Seconds::new(f64) -> Result<Seconds, ___>
Function name:   speed(d: ___, t: ___) -> Result<___, ___>
Test names:      1. ___________  2. ___________  3. ___________
```

---

### Independent Rust Drill

Separate from the physics build. From a blank file:

- [ ] Create three semantic wrappers around f64 (e.g., `Celsius(f64)`, `Fahrenheit(f64)`, `Kelvin(f64)`)
- [ ] Implement one conversion between them (e.g., Celsius to Kelvin)
- [ ] Derive `Debug`, `Clone`, `Copy`, `PartialEq` on each
- [ ] Write a constructor that validates (e.g., Kelvin cannot be negative)

---

### Tests Written First

```
1. test_typed_speed:            Meters(126) / Seconds(42) = MetersPerSecond(3.0)
2. test_constructor_rejection:  Meters::new(-5.0) should Err; Meters::new(NaN) should Err
3. test_conversion_round_trip:  meters_to_km then km_to_meters returns original value
```

---

### Gate: Do Not Open the Debrief Until

- [ ] Hand result exists (you wrote out the dimensional analysis)
- [ ] API is sketched (three types and the speed function)
- [ ] Tests are named
- [ ] First implementation attempt compiles or has a diagnosed error

---

## DEBRIEF PAGE

### Hint Ladder

**Hint 1.** Meaning can be encoded even when storage is f64. A `Meters(f64)` and a `Seconds(f64)` both store an f64 internally, but the type system treats them as different.

**Hint 2.** Hide raw fields. Make the inner f64 private (not `pub`). Force callers to go through constructors and methods. This prevents `.0 += 1.0` from breaking invariants.

**Hint 3.** Validate at boundaries. The constructor checks for NaN, infinity, and negative values. Once inside the type, the value is guaranteed valid.

---

### Failure Campaign

- [ ] Expose the inner `.0` field publicly (make it `pub`). Demonstrate how a caller can then write `meters.0 = -5.0` and break the invariant. This is why private fields matter.

- [ ] Remove the validation from the constructor. Show that `Meters(f64::NAN)` compiles and propagates silently through all operations.

- [ ] Try to add `Meters(10.0) + Seconds(5.0)`. If your types are designed correctly, this should be a COMPILE ERROR. If it compiles, your newtype pattern is wrong.

---

### Repository Destination

This is the first concept that graduates to a workspace crate. The unit
types defined here become `crates/units/src/lib.rs` and every other crate
in the workspace depends on them.

**Graduation steps (after mastery gate + delayed gate):**
1. Copy the type definitions to `crates/units/src/lib.rs`
2. Copy the tests
3. Run `cargo test --workspace`
4. Update this session's Notes with a link to the crate

---

### Python / Independent Check

Serialize values to CSV with explicit unit-bearing column names. Python
has no compile-time type checking for units, so the discipline must come
from conventions:

```python
# CSV with unit-bearing headers
# distance_m,speed_mps,time_s
# 126.0,3.0,42.0
```

Compare: how does Rust's type system enforce what Python can only
convention?

---

### Reference Shape

```rust
#[derive(Debug, Clone, Copy, PartialEq)]
pub struct Meters(f64);

#[derive(Debug, Clone, Copy, PartialEq)]
pub struct Seconds(f64);

#[derive(Debug, Clone, Copy, PartialEq)]
pub struct MetersPerSecond(f64);

fn speed(d: Meters, t: Seconds) -> Result<MetersPerSecond, PhysicsError> {
    // validate, then divide
}
```

---

### Mastery Claim

> "I can show one mistake that was moved from runtime to compile time."

What mistake? Write it in Notes. (Hint: swapping distance and time arguments.)

---

### Delayed Gate (complete at least ONE WEEK after the session)

- [ ] Recreate the three types from memory
- [ ] Solve a changed case by hand (different values)
- [ ] Explain why `.0` being public breaks invariants
- [ ] Reproduce from clean clone

---

## Session Notes

- **What surprised me:**
- **What I trust:**
- **Where it fails:**
- **What this unlocks:** (This unlocks typed physics for all future sessions)
- **The runtime-to-compile-time mistake:**
- **Last practiced:** (date)
- **Delayed gate date:** (date + 1 week)
- **Mastery gate passed:** [ ] yes [ ] not yet
