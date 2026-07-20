# Session Catalog: First 30 Sessions

The opening 30 sessions of the Frontier Engineer Field Manual. These are
organized into six missions — each producing a release artifact.

Every session follows the **Attempt Page + Debrief Page** format:
- **Attempt Page** = the work you do before looking at any solutions
- **Debrief Page** = hints, failure campaigns, reference shapes, and the delayed gate

See [docs/session_template.md](../docs/session_template.md) for the format spec.

---

## The Six Missions

| Mission | Sessions | Capability | Release Evidence |
|:-------:|:--------:|------------|-----------------|
| **1. Equation to Domain Type** | 01-05 | Units, algebra, errors, vectors, basic Rust | Foundation crate |
| **2. Context and Reusable Code** | 06-10 | Angles, sampling, frames, dot product, crate design | Typed motion toolkit |
| **3. Calculus Becomes Computation** | 11-15 | Functions, differentiation, integration, simulation | Motion CLI + validation |
| **4. Geometry and Numerical Honesty** | 16-20 | Vec3, work, rotations, transforms, floating point | Math/frames release |
| **5. Dynamics and Physical Oracles** | 21-25 | Forces, gravity, invariants, impulse, ODE state | Mechanics/orbit core |
| **6. Verified Numerical Engine** | 26-30 | Euler, midpoint, convergence, properties, release | v0.1 evidence package |

---

## How to Use This Catalog

1. Find the first session below with status `NOT STARTED` or `IN PROGRESS`
2. Open its `BRIEF.md`
3. Work through the Attempt Page first
4. Only open the Debrief Page after the gate is met
5. Update the status line in BRIEF.md and the table below

**Session rule:** Stop at the hint ladder until you have written a prediction,
equation, API signature, and tests. The debrief is a review tool, not the
starting point.

---

## File Structure (Per Session)

| File | Purpose |
|------|---------|
| `BRIEF.md` | Attempt Page + Debrief Page (the work and the review) |
| `Cargo.toml` | Independent Cargo project (no workspace) |
| `src/main.rs` | Binary entry point (I/O, demos) |
| `src/lib.rs` | Library logic (pure functions, types, tests) |

Each session is standalone. No shared dependencies. Concepts graduate
into `crates/` one at a time after the mastery gate and delayed gate pass.

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

## Mission 1: Equation to Domain Type (Sessions 01-05)

> **Goal:** Make equations executable. Define typed units. Handle errors honestly.
> **Release:** Foundation crate (`crates/units/`)

| # | Title | Math | Physics | Rust | Destination | Status |
|:-:|-------|------|---------|------|:-----------:|:------:|
| 01 | Make an equation executable | Units, scientific notation | Signal travel | cargo, f64, functions | `crates/units/src/units.rs` | NOT STARTED |
| 02 | Turn algebra into tested functions | Inverse relationships | Average speed | parameters, #[test] | `crates/foundation/src/kinematics.rs` | NOT STARTED |
| 03 | Represent failure honestly | Domains, inequalities | Physical validity | Result, enums, ? | `crates/foundation/src/error.rs` | NOT STARTED |
| 04 | Make units visible in types | Dimensional analysis | Unit safety | tuple structs, newtype | `crates/units/src/lib.rs` | NOT STARTED |
| 05 | Own a small vector type | Pythagorean theorem | Displacement | structs, methods, derive | `crates/math/src/vec2.rs` | NOT STARTED |

---

## Mission 2: Context and Reusable Code (Sessions 06-10)

> **Goal:** Add frame context, reusable code, and crate structure.
> **Release:** Typed motion toolkit

| # | Title | Math | Physics | Rust | Destination | Status |
|:-:|-------|------|---------|------|:-----------:|:------:|
| 06 | Radians before trigonometry | Unit circle, radians | Direction vectors | associated functions | `crates/units/src/angle.rs` | NOT STARTED |
| 07 | Sample a changing state | Discrete samples | Continuous vs sampled | ranges, Vec, iterators | `crates/mechanics/src/sampling.rs` | NOT STARTED |
| 08 | Model context with enums | Coordinate labels | Inertial/Earth-fixed/body frames | enums, match | `crates/frames/src/lib.rs` | NOT STARTED |
| 09 | Compute dot products from slices | Projection, angle | Alignment, work | slices, zip, iterators | `crates/math/src/dot.rs` | NOT STARTED |
| 10 | Build a maintainable crate | Model/presentation separation | Documentation | lib.rs, modules, pub | workspace milestone | NOT STARTED |

---

## Mission 3: Calculus Becomes Computation (Sessions 11-15)

> **Goal:** Turn calculus into executable numerical methods.
> **Release:** Motion CLI + validation

| # | Title | Math | Physics | Rust | Destination | Status |
|:-:|-------|------|---------|------|:-----------:|:------:|
| 11 | Treat a graph as behavior | Functions, shape, slope | State evolution | closures, generics | `crates/numerics/src/sample.rs` | NOT STARTED |
| 12 | Approximate a derivative | Difference quotient | Instantaneous rate | higher-order functions | `crates/numerics/src/differentiation.rs` | NOT STARTED |
| 13 | Connect position, velocity, acceleration | Derivatives, data geometry | Rates of change | windows, Option | `crates/numerics/src/finite_data.rs` | NOT STARTED |
| 14 | Accumulate change | Riemann sums, trapezoids | Displacement, impulse | windows, folds | `crates/numerics/src/integration.rs` | NOT STARTED |
| 15 | Release a constant-acceleration simulator | Kinematic equations | Model assumptions | CLI, CSV, integration tests | `apps/motion-cli` + `scenarios/` | NOT STARTED |

---

## Mission 4: Geometry and Numerical Honesty (Sessions 16-20)

> **Goal:** Master 3-D geometry and floating-point honesty.
> **Release:** Math/frames release

| # | Title | Math | Physics | Rust | Destination | Status |
|:-:|-------|------|---------|------|:-----------:|:------:|
| 16 | Graduate to Vec3 | 3-D dot, cross, norm | Planes, torque | operator traits | `crates/math/src/vec3.rs` | NOT STARTED |
| 17 | Use projection and work | Scalar projection | Mechanical work | semantic wrappers | `crates/mechanics/src/work.rs` | NOT STARTED |
| 18 | Rotate coordinates | Rotation matrices | Frame transforms | fixed arrays, sin_cos | `crates/frames/src/rotation2.rs` | NOT STARTED |
| 19 | Compose transformations | Noncommutativity | Frame chains | ordered operations | `crates/frames/src/transform2.rs` | NOT STARTED |
| 20 | Be honest about floating point | Representation, error | Tolerance | f64, approx compare | `crates/math/src/approx.rs` | NOT STARTED |

---

## Mission 5: Dynamics and Physical Oracles (Sessions 21-25)

> **Goal:** Model physical forces and use conservation laws as oracles.
> **Release:** Mechanics/orbit core

| # | Title | Math | Physics | Rust | Destination | Status |
|:-:|-------|------|---------|------|:-----------:|:------:|
| 21 | Translate a free-body diagram | Vector sums | Newton's second law | domain modeling | `crates/mechanics/src/dynamics.rs` | NOT STARTED |
| 22 | Implement inverse-square gravity | Inverse powers, singularities | Central gravity | constants, validation | `crates/orbit/src/gravity.rs` | NOT STARTED |
| 23 | Use conservation as an oracle | Invariants | Energy, angular momentum | diagnostics, property tests | `crates/orbit/src/diagnostics.rs` | NOT STARTED |
| 24 | Connect impulse and momentum | Integral of force | Impulse, delta-v | state updates | `crates/mechanics/src/impulse.rs` | NOT STARTED |
| 25 | Write a state derivative | ODE state-space | Instantaneous change | state structs, traits | `crates/numerics/src/dynamics.rs` | NOT STARTED |

---

## Mission 6: Verified Numerical Engine (Sessions 26-30)

> **Goal:** Ship a verified mechanics vertical slice with CI and evidence.
> **Release:** v0.1 evidence package

| # | Title | Math | Physics | Rust | Destination | Status |
|:-:|-------|------|---------|------|:-----------:|:------:|
| 26 | Take the first numerical step | Explicit Euler recurrence | Approximating change | immutable state updates | `crates/numerics/src/euler.rs` | NOT STARTED |
| 27 | Implement midpoint before RK4 | Second-order approximation | Vector field sampling | generic steppers | `crates/numerics/src/midpoint.rs` | NOT STARTED |
| 28 | Run a convergence study | Global error, observed order | Evidence of behavior | experiment harness, CSV | `experiments/convergence/` | NOT STARTED |
| 29 | Test properties, not only examples | Invariants, metamorphic relations | Structural laws | proptest, seeds | `crates/*/tests/properties.rs` | NOT STARTED |
| 30 | Ship a verified mechanics vertical slice | Model, numerics, uncertainty | Operating domain | workspace, CI, release | v0.1 release | NOT STARTED |

---

## Status Tracking

Update the Status column above AND the status line at the top of each `BRIEF.md`:

| Status | Meaning |
|--------|---------|
| `NOT STARTED` | Haven't begun |
| `IN PROGRESS` | Working through the Attempt Page |
| `TESTS PASSING` | Implementation done, tests green |
| `MASTERY GATE PASSED` | Can derive from memory, explain, show a failure |
| `DELAYED GATE PASSED` | 1-week retrieval test complete — concept is yours |
| `GRADUATED` | Concept migrated to `crates/` workspace crate |

---

## Repository Rules Per Session

1. **One concept per commit** until the design naturally requires composition.
2. Write the physical story and test cases **before** implementation.
3. Use explicit units in names (`time_s`, `distance_m`, not `t`, `d`).
4. Run `cargo fmt`, `cargo clippy -- -D warnings`, and `cargo test` before finishing.
5. Keep an engineering log in the Notes section of each `BRIEF.md`.
6. AI may critique after your first attempt. If AI writes code, you must re-derive and retype the essential path from memory later.

---

[<- README](../README.md) | [<- Documentation Index](../docs/INDEX.md) | [<- Daily Practice Guide](../docs/daily_practice.md)
