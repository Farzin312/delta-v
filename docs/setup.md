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

### Run Practice 1 (Session 01: Make an Equation Executable)

```bash
cd first_30/practice_1
cargo run
```

Expected output:

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

### Run Tests

```bash
cargo test
```

Expected:

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

### Run Lint Check

```bash
cargo fmt
cargo clippy -- -D warnings
```

---

## Repository Structure

```
delta-v/
├── README.md                  <- You are here (start here)
├── docs/
│   ├── curriculum.md          <- Full 104-unit, 13-stage curriculum map
│   ├── method.md              <- The 7-step loop, dependency rule, mastery gates
│   └── setup.md               <- This file
├── first_30/                  <- Launch sessions (highest detail)
│   ├── README.md              <- Session-by-session guide
│   ├── practice_1/            <- Session 01: Make an equation executable
│   │   ├── Cargo.toml
│   │   └── src/
│   │       └── main.rs        <- Kinematics + Vec2 with 6 tests
│   ├── practice_2/            <- Session 02: Turn algebra into a tested function
│   │   ├── Cargo.toml
│   │   └── src/
│   │       └── main.rs        <- (placeholder, ready to start)
│   └── ...                    <- Sessions 3-30 to be added as work progresses
└── .gitignore
```

Each `practice_N/` directory is an **independent Cargo project** -- no workspace, no shared dependencies. This is intentional: each session is self-contained and can be understood in isolation.

---

## How Each Session is Organized

Every practice file follows the same structure:

1. **Module doc comment** -- the physical story and what this session covers.
2. **Main function** -- demonstrates the concept with real values.
3. **Implementation** -- minimal, clean functions with documented parameters.
4. **Tests** (`#[cfg(test)] mod tests`) -- known values, edge cases, properties.

You'll see this pattern in every file as sessions are added. The consistency is the point -- it builds habit.

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
- The source document is the [Frontier Engineer Field Manual PDF](https://github.com/Farzin312/delta-v).

---

## Back to the root

[<- README](../README.md)
