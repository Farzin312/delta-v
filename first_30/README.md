# First 30 Sessions

The opening 30 hands-on sessions of the Frontier Engineer Field Manual. These are intentionally the most detailed because starting friction is high. Later units use the same loop on harder material.

---

## Why 30?

The hardest part of a long curriculum is not the advanced material -- it is building the correct habits before complexity arrives. Sessions 01-30 create the permanent loop:

```
  predict → explain → derive → implement → test → falsify → teach
```

Once this loop is reflexive, the remaining 74 units apply it to orbital mechanics, controls, estimation, flight software, AI, robotics, and mission design.

---

## Session Map

| # | Concept | Key Rust Skills | Status |
|:-:|---------|-----------------|:------:|
| 1 | Make an equation executable | cargo, f64, functions, println!, assertions, #[test] | done |
| 2 | Turn algebra into a tested function | functions, parameters, return values, Result | ready |
| 3 | Represent failure honestly | Result, enums, pattern matching, ? operator | pending |
| 4 | Make units visible in types | tuple structs, impl, Copy, newtype pattern | pending |
| 5 | Own a small vector type | structs, methods, references, derive | pending |
| 6 | Radians before trigonometry | associated functions, constants, constructors | pending |
| 7 | Sample a changing state | for loops, ranges, Vec, iterators | pending |
| 8 | Model context with enums | enums, match, exhaustive handling | pending |
| 9 | Compute dot products from slices | arrays, slices, iterators, zip | pending |
| 10 | Build a maintainable crate | modules, pub, lib.rs, main.rs, rustdoc, Git | pending |
| 11 | Treat a graph as behavior | closures, function parameters, sampling | pending |
| 12 | Approximate a derivative | higher-order functions, validation | pending |
| 13 | Connect position, velocity, acceleration | data windows, Option, boundary handling | pending |
| 14 | Accumulate change | windows, iterators, numerical APIs | pending |
| 15 | Release a constant-acceleration simulator | crate boundaries, CLI, CSV, integration tests | pending |
| 16 | Graduate to Vec3 | operator traits, normalization, robust errors | pending |
| 17 | Use projection and work | methods, semantic wrappers | pending |
| 18 | Rotate coordinates | fixed arrays, matrix-vector multiplication | pending |
| 19 | Compose transformations | matrix composition, API design | pending |
| 20 | Be honest about floating point | f64, epsilon, approximate comparison | pending |
| 21 | Translate a free-body diagram | data modeling, pure dynamics function | pending |
| 22 | Implement inverse-square gravity | vector normalization, constants, singularities | pending |
| 23 | Use conservation as an oracle | diagnostic functions, invariants | pending |
| 24 | Connect impulse and momentum | state updates, sign conventions | pending |
| 25 | Write a state derivative | structs, traits, derivative APIs | pending |
| 26 | Take the first numerical step | immutable state updates, step functions | pending |
| 27 | Implement midpoint before RK4 | function composition, intermediate states | pending |
| 28 | Run a convergence study | experiment harnesses, CSV, log-log reasoning | pending |
| 29 | Test properties, not only examples | proptest concept, randomized cases | pending |
| 30 | Ship a verified mechanics vertical slice | workspace design, CI, documentation, release | pending |

---

## How to Use These Sessions

### For each session:

1. Read the concept and the Rust skills column.
2. **Before opening the code**: write a prediction (sign, scale, direction, failure cases).
3. Try to implement it yourself.
4. Compare with the reference implementation in `practice_N/`.
5. Run the tests: `cargo test`
6. Try to break it (falsify): What inputs cause failures? Why?
7. Write a short note on what you learned and what remains uncertain.

### Repository rules per session:

- One concept per commit.
- Write the physical story and test cases before implementation.
- Run `cargo fmt`, `cargo clippy -- -D warnings`, and `cargo test` before finishing.
- Keep an engineering log.

---

## Current State

### Session 01 -- Done

Implements basic kinematic equations (position, velocity under constant acceleration) and a minimal 2D vector type (`Vec2`) with dot product and magnitude. Six tests covering rest, constant velocity, known magnitudes, and orthogonal vectors.

```bash
cd practice_1
cargo run    # see kinematics + vectors in action
cargo test   # 6 tests, all passing
```

### Session 02 -- Ready to Start

Placeholder in place. The next concept: turn algebraic equations into properly tested functions with input validation and Result-based error handling.

---

## Back

[<- README](../README.md)
