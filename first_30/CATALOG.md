# Session Catalog: First 30 Sessions

The opening 30 hands-on sessions of the Frontier Engineer Field Manual. These are intentionally the most detailed because starting friction is high. Later units use the same loop on harder material.

---

## How to Use This Catalog

Each session is a directory: `practice_01/` through `practice_30/`. Every directory contains:

| File | Purpose |
|------|---------|
| `BRIEF.md` | The problem statement, the full 7-step learning loop, hints, checklist, and notes template |
| `Cargo.toml` | Independent Cargo project (no workspace) |
| `src/main.rs` | Scaffold with prediction/derivation/implementation/test sections to fill in |

The pattern is designed to scale beyond the first 30. Future stages will follow the same structure:

```
delta-v/
  first_30/          <-- Stages 1-2 (Sessions 01-30)
    practice_01/
      BRIEF.md
      Cargo.toml
      src/main.rs
    practice_02/
      ...
  stage_03/          <-- Stage 3 (Units 17-24) - future
    unit_17/
      BRIEF.md
      Cargo.toml
      src/main.rs
    ...
  stage_04/          <-- Stage 4 (Units 25-32) - future
    ...
```

---

## Difficulty Scale

| Level | Meaning | Sessions |
|:-----:|---------|----------|
| 1 | Single concept, one function, first exposure | 01-03 |
| 2 | Composition of 2-3 concepts, struct definitions | 04-08 |
| 3 | Abstraction, modules, closures, numerical methods | 09-14 |
| 4 | Multi-part builds, 3D math, crate releases | 15-20 |
| 5 | Physics modeling, ODEs, integrators, diagnostics | 21-29 |
| 6 | Capstone: full vertical slice with CI and docs | 30 |

---

## Session Index

| # | Title | Stage | Difficulty | Status |
|:-:|-------|:-----:|:----------:|:------:|
| 01 | Make an equation executable | 1 | \| | NOT STARTED |
| 02 | Turn algebra into a tested function | 1 | \| | NOT STARTED |
| 03 | Represent failure honestly | 1 | \| | NOT STARTED |
| 04 | Make units visible in types | 1 | \|\| | NOT STARTED |
| 05 | Own a small vector type | 1 | \|\| | NOT STARTED |
| 06 | Radians before trigonometry | 1 | \|\| | NOT STARTED |
| 07 | Sample a changing state | 1 | \|\| | NOT STARTED |
| 08 | Model context with enums | 1 | \|\| | NOT STARTED |
| 09 | Compute dot products from slices | 1 | \|\|\| | NOT STARTED |
| 10 | Build a maintainable crate | 1 | \|\|\| | NOT STARTED |
| 11 | Treat a graph as behavior | 1 | \|\|\| | NOT STARTED |
| 12 | Approximate a derivative | 1 | \|\|\| | NOT STARTED |
| 13 | Connect position, velocity, acceleration | 1 | \|\|\| | NOT STARTED |
| 14 | Accumulate change | 1 | \|\|\| | NOT STARTED |
| 15 | Release a constant-acceleration simulator | 1 | \|\|\|\| | NOT STARTED |
| 16 | Graduate to Vec3 | 2 | \|\|\|\| | NOT STARTED |
| 17 | Use projection and work | 2 | \|\|\|\| | NOT STARTED |
| 18 | Rotate coordinates | 2 | \|\|\|\| | NOT STARTED |
| 19 | Compose transformations | 2 | \|\|\|\| | NOT STARTED |
| 20 | Be honest about floating point | 2 | \|\|\|\| | NOT STARTED |
| 21 | Translate a free-body diagram | 2 | \|\|\|\|\| | NOT STARTED |
| 22 | Implement inverse-square gravity | 2 | \|\|\|\|\| | NOT STARTED |
| 23 | Use conservation as an oracle | 2 | \|\|\|\|\| | NOT STARTED |
| 24 | Connect impulse and momentum | 2 | \|\|\|\|\| | NOT STARTED |
| 25 | Write a state derivative | 2 | \|\|\|\|\| | NOT STARTED |
| 26 | Take the first numerical step | 2 | \|\|\|\|\| | NOT STARTED |
| 27 | Implement midpoint before RK4 | 2 | \|\|\|\|\| | NOT STARTED |
| 28 | Run a convergence study | 2 | \|\|\|\|\| | NOT STARTED |
| 29 | Test properties, not only examples | 2 | \|\|\|\|\| | NOT STARTED |
| 30 | Ship a verified mechanics vertical slice | 2 | \|\|\|\|\|\| | NOT STARTED |

---

## How Each Session is Organized

Every session follows the same workflow:

1. Open `BRIEF.md` and read the problem
2. Complete Steps 1-3 (Predict, Explain, Derive) on paper or in comments BEFORE coding
3. Open `src/main.rs` and implement your functions
4. Write tests (Step 5) and run `cargo test`
5. Falsify (Step 6): try to break your code
6. Fill in the Notes section of `BRIEF.md` (Step 7: Teach)
7. Check off the checklist items
8. Run `cargo fmt` and `cargo clippy -- -D warnings`
9. Commit with a message like `session-01: make an equation executable`

### Status Tracking

Update the status line at the top of each `BRIEF.md` as you progress:

- `NOT STARTED` - haven't begun
- `IN PROGRESS` - working through the steps
- `TESTS PASSING` - implementation done, tests green
- `Mastery gate passed` - can derive from memory, explain, and show a failure

Update the Status column in this catalog to match.

---

## Repository Rules Per Session

1. **One concept per commit** until the design naturally requires composition.
2. Write the physical story and test cases **before** implementation.
3. Use explicit units in names (`time_s`, `distance_m`, not `t`, `d`).
4. Run `cargo fmt`, `cargo clippy -- -D warnings`, and `cargo test` before finishing.
5. Keep an engineering log in the Notes section of each `BRIEF.md`.
6. AI may critique after your first attempt. If AI writes code, you must re-derive and retype the essential path from memory later.

---

[<- README](../README.md)
