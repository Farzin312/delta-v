<div align="center">

# Δv

### The energy cost of changing trajectories.

A self-paced, dependency-driven curriculum for becoming a **computational space systems engineer**.

Physics &nbsp;·&nbsp; Rust &nbsp;·&nbsp; Space Systems &nbsp;·&nbsp; AI &nbsp;·&nbsp; Quantum

Every equation becomes an executable. Every implementation gets tested, broken deliberately, and verified independently.

No borrowed understanding.

</div>

---

## Table of Contents

- [What is this?](#what-is-this)
- [Why does this exist?](#why-does-this-exist)
- [The Three Spines](#the-three-spines)
- [The 7-Step Learning Loop](#the-7-step-learning-loop)
- [Curriculum at a Glance](#curriculum-at-a-glance)
- [Repository Structure](#repository-structure)
- [Quick Start](#quick-startart-starting)
- [Session Map (First 30)](#session-map-first-30)
- [How to Follow Along](#how-to-follow-along)
- [The AI Rule](#the-ai-rule)
- [Documentation](#documentation)

---

## What is this?

This repo is the code implementation of the [Frontier Engineer Field Manual](https://github.com/Farzin312/delta-v) -- a 104-unit path that takes you from high-school algebra to building mission-grade space systems software. It's not a collection of tutorials. It's a **build log**: every concept is implemented in Rust, tested against known physics, deliberately broken, and verified independently.

The destination is a specific kind of engineer:

> **Computational space systems engineer** -- someone who can move from physical law to verified software, from data to trustworthy autonomy, and from a mission idea to reproducible evidence.

This is the overlap that most candidates leave empty:

```
  ┌─────────────────────────────────────────────────────────────┐
  │                                                             │
  │    "I can derive the physics, implement it in safe Rust,    │
  │     test it against independent references, and tell you    │
  │     exactly where and why it will fail."                    │
  │                                                             │
  │           Most people can do one of these.                  │
  │           Very few can do all four.                         │
  │           That intersection is the point.                   │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘
```

---

## Why does this exist?

The world doesn't need another "learn to code" tutorial. It needs engineers who can:

- Translate a physics equation into a typed, tested, performant program.
- Recognize when a model is invalid, when a numerical method is lying, and when AI is hallucinating.
- Design systems that survive hardware constraints, real-time deadlines, and operational failure.
- Own outcomes when the model is wrong.

Current SpaceX simulation roles call for classical physics, math, C++, Python, debugging, performance, and testing. SpaceX GNC work combines orbital mechanics, control, estimation, optimization, production software, data analysis, and documentation. Rocket Lab, Anduril, Varda, and Axiom show the same pattern.

This curriculum builds exactly that profile, from first principles, in public.

---

## The Three Spines

Everything is built along three spines simultaneously. No spine is optional.

```
  ┌─────────────────────┐  ┌─────────────────────┐  ┌─────────────────────┐
  │  PHYSICAL REASONING │  │  SOFTWARE SYSTEMS   │  │ EVIDENCE & JUDGMENT │
  ├─────────────────────┤  ├─────────────────────┤  ├─────────────────────┤
  │ Mechanics           │  │ Rust (from Day 1)   │  │ Requirements        │
  │ Dynamics            │  │ Python (science)    │  │ Uncertainty         │
  │ Calculus            │  │ C/C++ interop       │  │ Validation          │
  │ Linear algebra      │  │ Testing / fuzzing   │  │ Independent refs    │
  │ Numerics            │  │ OS / embedded       │  │ Failure analysis    │
  │ Controls            │  │ Real-time           │  │ Technical writing   │
  │ Estimation          │  │ Networking          │  │ Peer review         │
  │ Probability         │  │ Security            │  │                     │
  └─────────┬───────────┘  └─────────┬───────────┘  └─────────┬───────────┘
            │                        │                        │
            └────────────────────────┼────────────────────────┘
                                     │
                          ┌──────────┴──────────┐
                          │ Computational Space │
                          │ Systems Engineer    │
                          └─────────────────────┘
```

Read more: [docs/method.md](docs/method.md) - covers the full methodology including the AI-quarantine protocol, understanding debt, field checklists, and the question ladder.

Every session follows this loop. It is the engine of the entire curriculum.

```
  PREDICT      →  Write down sign, scale, direction BEFORE coding.
                   (A prediction that can be wrong.)

  EXPLAIN      →  Draw the physical story. Name boundaries, frames, units.
                   (A diagram + 5-sentence explanation.)

  DERIVE       →  From definitions to equation. Check dimensions.
                   (Hand derivation, every symbol defined.)

  IMPLEMENT    →  Smallest clean Rust function expressing the idea.
                   (Compiling code, clear API, no hidden I/O.)

  TEST         →  Known case + boundary + property + independent reference.
                   (Automated tests + validation note.)

  FALSIFY      →  Change scale, sign, step, noise to make it BREAK.
                   (A failure you can explain + declared domain.)

  TEACH        →  Explain what changed in your mental model.
                   (README note, diagram, or recording.)
```

You can see this loop in the practice files. Look at `first_30/practice_1/src/main.rs` -- the module doc comment is the Explain step, the function stubs with `todo!()` are where you Implement, and the commented-out tests describe what you must Test and Falsify.

Read more: [docs/method.md](docs/method.md)

## Curriculum at a Glance

104 units across 13 stages. Unit numbers show dependency order, not weeks.

```
  Stage  1  ████████████  Rust + Mathematical Language          (Units  1- 8)
  Stage  2  ████████████  Calculus + Numerical Mechanics         (Units  9-16)
  Stage  3  ████████████  Orbital Mechanics Core                 (Units 17-24)
  Stage  4  ████████████  Mission Analysis                       (Units 25-32)
  Stage  5  ████████████  Attitude + Control                     (Units 33-40)
  Stage  6  ████████████  Estimation + Signals                   (Units 41-48)
  Stage  7  ████████████  Systems + Embedded                     (Units 49-56)
  Stage  8  ████████████  Flight Software Architecture           (Units 57-64)
  Stage  9  ████████████  Verification + Security                (Units 65-72)
  Stage 10  ████████████  Scientific AI                          (Units 73-80)
  Stage 11  ████████████  Robotics + Autonomy                    (Units 81-88)
  Stage 12  ████████████  Multiphysics Space Systems             (Units 89-96)
  Stage 13  ████████████  Specialization + Public Evidence       (Units 97-104)
```

Each stage ends with a **capstone** you must defend without AI-generated explanations.

Read the full map: [docs/curriculum.md](docs/curriculum.md)

---

## Repository Structure

```
delta-v/
│
├── README.md                  ← You are here. Start here.
├── docs/                      ← Deep guides for following along
│   ├── curriculum.md          ← Full 104-unit, 13-stage map with build evidence
│   ├── method.md              ← The 7-step loop, dependency rule, mastery gates
│   └── setup.md               ← Environment setup, tools, how to run
│
├── first_30/                  ← Launch sessions (highest friction, highest detail)
│   ├── README.md              ← Session-by-session guide
│   │
│   ├── practice_1/            ← Session 01: Make an equation executable
│   │   ├── Cargo.toml         ← Independent Cargo project (no workspace)
│   │   └── src/
│   │       └── main.rs        ← Kinematics + Vec2, 6 passing tests
│   │
│   ├── practice_2/            ← Session 02: Turn algebra into a tested function
│   │   ├── Cargo.toml
│   │   └── src/
│   │       └── main.rs        ← (placeholder, ready to start)
│   │
│   └── ...                    ← Sessions 03-30 added as work progresses
│
└── .gitignore
```

**Key design decision:** Each `practice_N/` is a standalone Cargo project -- no shared workspace, no shared dependencies. Every session is self-contained and can be understood in isolation. This is intentional: it means anyone can clone, `cd` into any session, and run it without context from previous sessions.

---

## Quick Start

```bash
# Clone
git clone https://github.com/Farzin312/delta-v.git
cd delta-v

# Run Session 01
cd first_30/practice_1
cargo run
```

Output:

```
=== Practice 1: Make an Equation Executable ===

[Kinematics]
  Initial position: 0 m
  Initial velocity: 10 m/s
  Acceleration:     -9.81 m/s^2
  After 2 s:
    Position: 0.3800 m
    Velocity: -9.6200 m/s

[Vectors]
  v = (3, 4)
  w = (1, 0)
  |v|   = 5.0000
  v . w = 3.0000
```

Run the tests:

```bash
cargo test
```

```
running 6 tests
test tests::test_position_constant_velocity ... ok
test tests::test_vec2_dot_known ... ok
test tests::test_position_rest ... ok
test tests::test_vec2_dot_orthogonal ... ok
test tests::test_velocity_linear ... ok
test tests::test_vec2_magnitude ... ok

test result: ok. 6 passed; 0 failed
```

Full setup instructions: [docs/setup.md](docs/setup.md)

---

## Session Map (First 30)

The first 30 sessions are intentionally the most detailed because starting friction is high. Later units use the same loop on harder material.

| # | Concept | Rust Skills | Artifact |
|:-:|---------|-------------|----------|
| 1 | Make an equation executable | cargo, f64, functions, println!, assertions | Unit-safe conversion CLI |
| 2 | Turn algebra into a tested function | functions, parameters, return values, #[test] | Equation evaluator |
| 3 | Represent failure honestly | Result, enums, pattern matching, ? operator | Error-handling module |
| 4 | Make units visible in types | tuple structs, impl, Copy, newtype | Unit-safe types |
| 5 | Own a small vector type | structs, methods, references, derive | Vec2 library |
| 6 | Radians before trigonometry | associated functions, constants, constructors | Angle toolkit |
| 7 | Sample a changing state | for loops, ranges, Vec, iterators | Motion-table generator |
| 8 | Model context with enums | enums, match, exhaustive handling | State machine |
| 9 | Compute dot products from slices | arrays, slices, iterators, zip | Linear algebra core |
| 10 | Build a maintainable crate | modules, pub, lib.rs, rustdoc, Git | Modular crate |
| 11 | Treat a graph as behavior | closures, function parameters, sampling | Function grapher |
| 12 | Approximate a derivative | higher-order functions, validation | Finite-difference lab |
| 13 | Connect position, velocity, acceleration | data windows, Option, boundary handling | Kinematic chain |
| 14 | Accumulate change | windows, iterators, numerical APIs | Trapezoid integrator |
| 15 | Release a constant-acceleration simulator | crate boundaries, CLI, CSV, integration tests | Simulator release |
| 16 | Graduate to Vec3 | operator traits, normalization, robust errors | 3D vector library |
| 17 | Use projection and work | methods, semantic wrappers | Work calculator |
| 18 | Rotate coordinates | fixed arrays, matrix-vector multiplication | Rotation library |
| 19 | Compose transformations | matrix composition, API design | Transform chain |
| 20 | Be honest about floating point | f64, epsilon, approximate comparison | Float comparison toolkit |
| 21 | Translate a free-body diagram | data modeling, pure dynamics function | FBD-to-code translator |
| 22 | Implement inverse-square gravity | vector normalization, constants, singularities | Gravity model |
| 23 | Use conservation as an oracle | diagnostic functions, invariants | Conservation checker |
| 24 | Connect impulse and momentum | state updates, sign conventions | Impulse simulator |
| 25 | Write a state derivative | structs, traits, derivative APIs | ODE state system |
| 26 | Take the first numerical step | immutable state updates, step functions | Euler integrator |
| 27 | Implement midpoint before RK4 | function composition, intermediate states | Midpoint integrator |
| 28 | Run a convergence study | experiment harnesses, CSV, log-log reasoning | Convergence report |
| 29 | Test properties, not only examples | proptest concept, randomized cases | Property tests |
| 30 | Ship a verified mechanics vertical slice | workspace design, CI, documentation, release | **Mechanics engine** |

---

## How to Follow Along

**If you're learning alongside this repo:**

1. Read [docs/setup.md](docs/setup.md) to get Rust running.
2. Start with Session 01 (`first_30/practice_1/`). Read the code. Run it. Read the tests.
3. Before reading the implementation, try to write your own. The whole point is to build it yourself.
4. Follow the [7-step loop](#the-7-step-learning-loop) for each session.
5. Check the [mastery gate](docs/method.md#mastery-gate-advance-only-when-all-are-true) before moving on.
6. Keep an engineering log (template in [docs/setup.md](docs/setup.md)).

**If you're browsing:**

- [docs/curriculum.md](docs/curriculum.md) -- see the full 104-unit path.
- [docs/method.md](docs/method.md) -- understand why the code is structured this way.
- Each practice file is self-contained and readable in isolation.

**No fixed calendar.** A unit may take two days or a month. Advance only when the mastery gate is met.

---

## The AI Rule

> Use AI to accelerate explanation, scaffolding, test generation, literature discovery, refactoring, and critique.
>
> Never let AI become the only entity that can explain a formula, invariant, unit, unsafe block, convergence result, dataset split, or mission decision.
>
> If AI writes code, you must re-derive and retype the essential path from memory later.

This repo is built following that rule. The code you see was written by hand, tested, broken, and understood before any AI critique was applied.

---

## Documentation

| Document | What's in it |
|----------|-------------|
| [docs/curriculum.md](docs/curriculum.md) | Full 104-unit map across 13 stages, portfolio evidence ladder, competitive positioning |
| [docs/method.md](docs/method.md) | The 7-step learning loop, dependency rule, mastery gates, when-stuck heuristics, AI operating rule |
| [docs/setup.md](docs/setup.md) | Environment setup, tool installation, how to run, engineering log template |

---

## Source

This repo implements the **Frontier Engineer Field Manual** (July 2026).

<div align="center">

**Building in public. No borrowed understanding.**

</div>
