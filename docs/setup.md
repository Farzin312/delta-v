# Setup: How to Follow Along

Everything you need to clone this repo and run the code yourself.

---

## Prerequisites

### 1. Install Rust

Install via [rustup](https://rustup.rs/) (the official Rust installer):

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

Verify your installation:

```bash
rustc --version
cargo --version
```

You should see version numbers for both. This project uses Rust Edition 2024, so make sure your toolchain is current (`rustup update` if needed).

### 2. Install Formatting and Linting Tools

These are used before every finished session:

```bash
rustup component add rustfmt clippy
```

### 3. Install Git

```bash
git --version   # verify it's installed
```

If not, install via your package manager or [git-scm.com](https://git-scm.com/).

---

## Clone and Run

```bash
git clone https://github.com/Farzin312/delta-v.git
cd delta-v
```

### Run Session 01 (Make an Equation Executable)

```bash
cd first_30/practice_01
cargo run
```

The scaffold prints a placeholder message until you implement the functions:

```
Session 01: Make an equation executable
Implement the functions below, then fill in main().
```

After you implement the solution (signal distance: speed * time), your output will show the computed distance in meters and kilometers.

### Run Tests

```bash
cargo test
```

The scaffold ships with the test module commented out. After you uncomment and implement your tests, you should see:

```
running N tests
...
test result: ok. N passed; 0 failed
```

### Run Lint Check

```bash
cargo fmt
cargo clippy -- -D warnings
```

---

## Repository Structure

```
delta-v/
|-- README.md                  <- Start here
|-- docs/
|   |-- INDEX.md               <- Master documentation index
|   |-- curriculum.md          <- Full 104-unit, 13-stage curriculum map
|   |-- method.md              <- The 7-step loop, dependency rule, mastery gates
|   |-- formula_reference.md   <- Every equation, organized by topic
|   |-- concept_map.md         <- Dependency chain, what each session teaches
|   |-- setup.md               <- This file
|   |-- scripts.md             <- Session generator documentation
|   |-- predict_practice/      <- PREDICT step workbook with examples
|-- first_30/                  <- Launch sessions (Stages 1-2)
|   |-- CATALOG.md             <- Session-by-session index with status tracking
|   |-- practice_01/           <- Session 01: Make an equation executable
|   |   |-- BRIEF.md           <- Problem, 7-step loop, checklist, notes
|   |   |-- Cargo.toml         <- Independent Cargo project
|   |   |-- src/main.rs        <- Scaffold: prediction/derivation/code/tests
|   |-- practice_02/ .. practice_30/
|-- scripts/
|   |-- new_session.py         <- Session generator (create, list, doctor, regenerate)
|-- LICENSE                    <- MIT
```

Each `practice_NN/` directory is an **independent Cargo project** -- no workspace, no shared dependencies. This is intentional: each session is self-contained and can be understood in isolation.

---

## How Each Session is Organized

Every practice directory follows the same structure:

1. **BRIEF.md** -- the problem statement, the full 7-step learning loop, hints, checklist, and notes template.
2. **Cargo.toml** -- an independent Cargo project (no workspace).
3. **src/main.rs** -- a scaffold with PREDICT/DERIVE/IMPLEMENT/TEST comment sections to fill in.

You write the code. The scaffold provides the structure. See [the method](method.md) for why each step exists.

---

## Recommended Background

The manual assumes:

- **Algebra** remembered (everything else may be blurry).
- **No prior Rust** required (Rust starts from Session 01).
- **No prior physics beyond high-school mechanics** (calculus and advanced topics are taught in-stage).

If your algebra is rusty, spend a weekend with any standard algebra review before Session 01. The manual will take care of the rest.

---

## Tools You Will Eventually Need (Not for Session 01)

These are NOT needed to start. They come in later stages:

| Tool | When | Purpose |
|------|------|---------|
| Python 3 + NumPy | Stage 10 | Scientific computing partner |
| PyTorch or JAX | Stage 10 | Neural network training |
| GMAT or Orekit | Stage 4 | Independent orbit validation |
| SPICE toolkit (NASA) | Stage 4 | Ephemerides and frame conversions |
| QEMU | Stage 7 | Embedded microcontroller simulation |
| bindgen / cxx | Stage 7 | C/C++ FFI bridges |

Do not install these upfront. Install them when the curriculum calls for them.

---

## The Engineering Log

Every session ends with a log entry. Eight fields, no shortcuts. This is your external memory that compounds across units. See [docs/method.md](method.md#8-the-engineering-log) for the full explanation.

```
## Session 01 - Make an Equation Executable

Concept:       Turn kinematic equations into executable, tested Rust.
Prediction:    Ball thrown up at 10 m/s with gravity -9.81 m/s^2:
               peak at ~t=1s, falling by t=2s. Position near zero
               at t=2s. Velocity negative (falling).
Derivation:    x(t) = x0 + v0*t + 0.5*a*t^2
               v(t) = v0 + a*t
               Dimensions: [m] = [m] + [m/s]*[s] + [m/s^2]*[s^2]  -> checks
               Limit t=0: x=x0, v=v0  -> checks
Rust mapping:  f64 params for x0,v0,a,t. Pure functions, no I/O.
               Vec2 struct with x,y: f64. Methods: new, magnitude, dot.
               Derive Debug, Clone, Copy, PartialEq.
Evidence:      Known: position_at_time(0,0,0,5)=0 [rest case]
               Boundary: position_at_time(0,10,0,3)=30 [no accel]
               Property: dot of orthogonal vectors = 0
               Known value: 3-4-5 triangle magnitude = 5
Discrepancy:   None. Prediction matched result.
AI ledger:     No AI used. All code self-derived.
Next dep:      Unlocks Session 02 (tested functions with validation).
               Gate: can I derive x(t) from memory and explain units?
```

This log is not busywork. It is the record that proves mastery and surfaces understanding debt before it compounds.

---

## Questions About the Curriculum?

- Read [docs/curriculum.md](curriculum.md) for the full 104-unit map.
- Read [docs/method.md](method.md) for the learning methodology.
- See [docs/INDEX.md](INDEX.md) for the master documentation index.
- The source document is the [Frontier Engineer Field Manual PDF](https://github.com/Farzin312/delta-v).

---

## Back to the root

[<- README](../README.md)  |  [<- Documentation Index](INDEX.md)
