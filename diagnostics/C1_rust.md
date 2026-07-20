# C1 Diagnostic: Rust Fundamentals

> No notes. No AI. No IDE autocomplete. Blank text file only.
> Time: 30 minutes. Write actual Rust code.

This tests whether you can write basic Rust from memory. If you score
below 65%, work through drills 01-05 before starting the sessions.

---

## Instructions

Open a blank file. Write Rust code that satisfies each task below.
Compile and test with `cargo test` when done. Score yourself based on
what compiles and passes WITHOUT looking anything up.

---

## Tasks

### Task 1: Bindings and Types (5 min)

Write:
- A `let` binding for an integer, a float, and a string slice
- A `const` for the speed of light: 299_792_458.0 m/s
- Print each using `println!` with `{}` format

### Task 2: Pure Function (5 min)

Write a function `fn distance_m(speed_mps: f64, time_s: f64) -> f64` that
computes distance. No printing inside the function. Call it from `main`
and print the result.

### Task 3: Enum and Result (5 min)

Write:
- An enum `PhysicsError` with variants: `NonPositiveTime`, `NonFiniteInput`
- A function `fn speed_mps(d: f64, t: f64) -> Result<f64, PhysicsError>`
  that validates t (finite, positive) and returns Ok(d/t) or the appropriate error
- Derive `Debug` and `PartialEq` on the enum

### Task 4: Struct with Methods (7 min)

Write:
- A struct `Vec2 { x: f64, y: f64 }`
- An `impl` block with:
  - `fn new(x: f64, y: f64) -> Self`
  - `fn norm(self) -> f64` (use `hypot`)
- Derive `Debug, Clone, Copy, PartialEq`

### Task 5: Tests (8 min)

Write a `#[cfg(test)] mod tests` block with:
- `test_distance`: distance_m(10.0, 5.0) == 50.0
- `test_speed_ok`: speed_mps(100.0, 10.0) == Ok(10.0)
- `test_speed_zero_time`: speed_mps(100.0, 0.0) returns an error
- `test_speed_nan`: speed_mps(100.0, f64::NAN) returns an error
- `test_vec2_norm`: Vec2::new(3.0, 4.0).norm() == 5.0

---

## Scoring

Score each task independently:

| Task | Full credit if... | Partial if... |
|------|-------------------|---------------|
| 1 | Compiles, correct types, prints correctly | Wrong format specifier |
| 2 | Compiles, function is pure (no I/O), correct result | Printing inside function |
| 3 | Compiles, validates correctly, derives present | Missing NaN check |
| 4 | Compiles, hypot used, traits derived | Used sqrt instead of hypot |
| 5 | All 5 tests pass | 3-4 tests pass |

| Score | Interpretation |
|-------|---------------|
| 5/5 tasks full credit | Strong Rust foundation. Proceed to sessions. |
| 4/5 full credit | Good. Review the weak area. |
| 3/5 full credit | Complete drills 01-05 before sessions. |
| Below 3/5 | Start with Rust Book chapters 1-5, then drills. |

---

## What This Reveals

| If you struggled with... | Repair with... |
|--------------------------|----------------|
| `let` vs `const` | Rust Book ch 3, drill 01 |
| Function signatures, return types | Rust Book ch 3, drill 02 |
| Enums, Result, match | Rust Book ch 6 + 9, drill 03 |
| Structs, impl, derive | Rust Book ch 5, drill 05 |
| Test modules, assert_eq | Rust Book ch 11, drill 16 |
| `?` operator, error propagation | Rust Book ch 9, drill 03 + 19 |

---

## Score: ____ / 5 tasks

Record in the Diagnostic Log in diagnostics/README.md.
