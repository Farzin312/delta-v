# Frontier Engineer — The Field Manual (Markdown Edition)

> This document is the markdown companion to the **Frontier Engineer Field Manual, Master Edition (July 2026)** PDF. It captures what the course is, what you will learn, how it is organized, and how this repository should evolve to match the manual's design. The PDF is the authoritative source; this document is the navigable, editable version.

---

## Table of Contents

1. [What This Course Is](#1-what-this-course-is)
2. [Who This Is For](#2-who-this-is-for)
3. [The Honest Target](#3-the-honest-target)
4. [The Four Concurrent Lanes](#4-the-four-concurrent-lanes)
5. [Depth Labels (L1 / L2 / L3)](#5-depth-labels-l1--l2--l3)
6. [The Daily and Weekly Study System](#6-the-daily-and-weekly-study-system)
7. [Diagnostics and Narrow Repair](#7-diagnostics-and-narrow-repair)
8. [The Mastery Gate](#8-the-mastery-gate)
9. [The AI Protocol](#9-the-ai-protocol)
10. [The Six Missions (Sessions 01-30)](#10-the-six-missions-sessions-01-30)
11. [Session Structure: Attempt Page + Debrief Page](#11-session-structure-attempt-page--debrief-page)
12. [The Four Knowledge Spines](#12-the-four-knowledge-spines)
   - [Mathematics (M0-M10)](#mathematics-m0-m10)
   - [Physics and Engineering (P0-P8)](#physics-and-engineering-p0-p8)
   - [Programming and Systems (C1-C9)](#programming-and-systems-c1-c9)
   - [Space Systems (S1-S9)](#space-systems-s1-s9)
13. [Specialization Tracks and Evidence Ladder](#13-specialization-tracks-and-evidence-ladder)
14. [Repository Transformation Plan](#14-repository-transformation-plan)
15. [Quality Gates and CI](#15-quality-gates-and-ci)
16. [Resource Directory](#16-resource-directory)
17. [Engineering Opinion: Where This Repo Should Deviate](#17-engineering-opinion-where-this-repo-should-deviate)

---

## 1. What This Course Is

A self-paced, dependency-driven curriculum for becoming a **computational space systems engineer** — someone who can move from physical law to verified software, from sensor data to trustworthy decisions, and from a mission idea to reproducible engineering evidence.

The manual is explicit: this is an **operating system, not a reading list**. It is practice-first, dependency-aware, and evidence-driven. Every concept must be derived by hand, implemented in code, tested against known physics, deliberately broken, and verified independently.

The core loop, repeated for every concept:

```
PREDICT → EXPLAIN → DERIVE → IMPLEMENT → TEST → FALSIFY → TEACH
```

**Languages:**
- **Rust** — primary language from Day 1. Ownership, borrowing, explicit errors, and algebraic data types force design decisions into the open.
- **Python** — scientific partner: NumPy, SciPy, plotting, reference implementations, AI. Enters as a validation tool and later as a first-class language.
- **C/C++** — required for flight frameworks (cFS, F Prime), FFI, legacy systems, and the aerospace ecosystem. Enters at the systems/embedded stage.

**No borrowed understanding.** If you cannot re-derive, re-type, and defend it, it is not yours.

---

## 2. Who This Is For

**You should be here if:**
- You want to build things that fly, orbit, land, or operate autonomously
- You are tired of tutorials that teach syntax without physics
- You want to understand equations well enough to implement, break, and defend them
- You are self-motivated and do not need a classroom calendar
- You believe AI is a tool, not a replacement for engineering judgment

**You should NOT be here if:**
- You want a quick "learn Rust in 30 days" course
- You are looking for copy-paste solutions
- You are not willing to write code that fails and figure out why
- You want to skip the physics and go straight to building product

**Prerequisites:** High-school algebra. Everything else is rebuilt from scratch.

---

## 3. The Honest Target

The target is NOT simultaneous mastery of every aerospace discipline. The target is:

- **Deep common foundations** — algebra through differential equations, linear algebra, probability, numerical analysis, mechanics, E&M, thermodynamics, waves, Rust, scientific Python, systems engineering, verification.
- **Broad literacy** with **selective depth** — orbital mechanics, GNC, estimation, thermal, structures, power, comms, propulsion, flight software, space environment, operations, AI, autonomy, robotics.

The manual rejects the fantasy that reading every chapter makes you a propulsion engineer, GNC specialist, quantum researcher, and flight-software lead at once. Capability is demonstrated by **difficult, reproducible artifacts and judgment under failure**.

The destination is a specific kind of engineer:

> *"I can derive the physics, implement it in safe Rust, test it against independent references, and tell you exactly where and why it will fail."*

Most people can do one of these. Very few can do all four. That intersection is the point.

---

## 4. The Four Concurrent Lanes

Every study day runs four lanes simultaneously. No lane is optional.

| Lane | Daily Question | Evidence |
|------|---------------|----------|
| **Mathematics** | Can I derive, estimate, and manipulate the model? | Hand solution, diagram, dimensional check |
| **Physics / Engineering** | What system, assumptions, frame, and failure domain exist? | Physical story, model, experiment or reference |
| **Programming Craft** | Can I write and explain the language and architecture independently? | Blank-file drill, tests, debugging note, code review |
| **Integrated Build** | Can another engineer reproduce and challenge the result? | Versioned artifact, validation, limitations, README |

The order protects independent reasoning: retrieve first, learn formally, practice the language separately, then integrate.

---

## 5. Depth Labels (L1 / L2 / L3)

| Depth | Meaning | Expected Output |
|-------|---------|-----------------|
| **L1 — Literacy** | Explain the field, interfaces, risks, and when to consult a specialist | Concept map and trade-off summary |
| **L2 — Working Competence** | Solve standard problems, implement models, validate, and debug | Tested laboratory or subsystem model |
| **L3 — Specialization** | Handle unfamiliar problems, read papers, make design decisions | Research replication, upstream contribution, mission capstone |

You reach L1 broadly, L2 in the common core, and L3 in ONE chosen specialization.

---

## 6. The Daily and Weekly Study System

### Default Full Session — 3 hours 25 minutes

| Block | Time | What You Do | Output |
|-------|------|-------------|--------|
| Retrieval warm-up | 15 min | Closed-book equations, diagrams, Rust syntax, yesterday's bug | Dated recall sheet |
| Mathematics | 45 min | Formal lesson + 2-4 hand problems + one gap repair | Worked derivation |
| Programming craft | 45 min | Blank-file Rust drill, code reading, debugging, or refactoring unrelated to the physics task | Small commit and explanation |
| Physics / Engineering | 45 min | System diagram, assumptions, estimates, model derivation, experiment/reference | Physical story |
| Integrated build | 45 min | Implement, test, compare, break, document | Repository artifact |
| Exit review | 10 min | State what changed, what remains borrowed, and next review date | Engineering log |

### Minimum Viable Day — 75 minutes

- 20 min: Retrieval + one hand problem
- 25 min: One Rust concept from a blank file
- 30 min: One integrated test or experiment

### Weekly Rhythm

| Day | Focus | Reason |
|-----|-------|--------|
| 1 | New concept + baseline | Create a simple mental model and known case |
| 2 | Language depth + second representation | Prevent domain work from hiding language gaps |
| 3 | Numerical / experimental variation | Expose assumptions and error behavior |
| 4 | Debugging and edge cases | Learn through failure, not only construction |
| 5 | Integration and documentation | Turn fragments into a reusable system |
| 6 | Mixed review and defense | Interleave related concepts and retrieve after delay |
| 7 | Rest, wonder, or light reading | Preserve motivation and allow spacing |

---

## 7. Diagnostics and Narrow Repair

Course labels are too coarse. "I took Calculus II" says little about convergence, series, parametric curves, or integration fluency. Every module begins with a **capability contract** and a diagnostic.

### The Process

```
Attempt diagnostic (no notes, no AI, timed lightly)
    → Locate smallest failed node (e.g. "logarithms," not "all algebra")
        → Repair and return (2-6 focused exercises + one application)
```

### Readiness Scoring

| Result | Action |
|--------|--------|
| 85-100% | Proceed; schedule cumulative review |
| 65-84% | Proceed with targeted repair embedded in the week |
| Below 65% | Pause the dependent topic; repair the failed nodes first |
| Correct answer, weak explanation | Treat as NOT mastered. Reconstruct assumptions and reasoning |

---

## 8. The Mastery Gate

Advance only when ALL are true:

- Solve a representative problem without notes or AI
- Explain assumptions, units, valid domain, and limiting behavior
- Implement the essential path and explain every type and error path
- Show a known case, edge case, property, and independent comparison
- Demonstrate a failure and classify it as model, numerical, software, or requirements error
- Retrieve the idea successfully after at least one week

**Do not advance because the calendar says so.**

---

## 9. The AI Protocol

### Allowed Early
- Generate extra practice after your attempt
- Critique assumptions and tests
- Locate official documentation
- Explain compiler messages after your diagnosis
- Compare alternate API designs
- Review a finished derivation for gaps

### Quarantined Until Later
- Full solution before prediction
- Code you cannot retype or explain
- Derivation with undefined symbols
- Automatic library selection without reading contracts
- Mission decision without independent evidence
- Tests generated after implementation only

### The Four-Pass Rule

1. **Independent attempt** — Predict, sketch, derive, design API, and list tests.
2. **Targeted assistance** — Ask for a hint, counterexample, or critique rather than replacement.
3. **Verification** — Check official sources, run tests, compare tools, and inspect failure.
4. **Reconstruction** — Later reproduce the essential reasoning and code without the model.

**AI ledger:** Record what the model supplied, what you independently verified, and what remains borrowed. A system you cannot explain is not your capability.

---

## 10. The Six Missions (Sessions 01-30)

The first 30 sessions are organized into six missions. Each mission produces a release artifact.

| Mission | Sessions | Capability | Release Evidence |
|---------|----------|------------|-----------------|
| **1. Equation to Domain Type** | 01-05 | Units, algebra, errors, vectors, basic Rust | Foundation crate |
| **2. Context and Reusable Code** | 06-10 | Angles, sampling, frames, dot product, crate design | Typed motion toolkit |
| **3. Calculus Becomes Computation** | 11-15 | Functions, differentiation, integration, simulation | Motion CLI + validation |
| **4. Geometry and Numerical Honesty** | 16-20 | Vec3, work, rotations, transforms, floating point | Math/frames release |
| **5. Dynamics and Physical Oracles** | 21-25 | Forces, gravity, invariants, impulse, ODE state | Mechanics/orbit core |
| **6. Verified Numerical Engine** | 26-30 | Euler, midpoint, convergence, properties, release | v0.1 evidence package |

**Session rule:** Stop at the hint ladder until you have written a prediction, equation, API signature, and tests. The debrief page is a review tool, not the starting point.

### Full Session Roster

| # | Title | Mission | Math | Physics | Rust/Engineering | Repository Destination |
|:-:|-------|:-------:|------|---------|-----------------|----------------------|
| 01 | Make an equation executable | M1 | Units, scientific notation, proportional reasoning | Signal travel and dimensional consistency | Cargo, bindings, f64, functions, assertions | `crates/foundation/src/units.rs` |
| 02 | Turn algebra into tested functions | M1 | Rearranging equations and inverse relationships | Average speed and round-trip consistency | Parameters, return values, unit tests | `crates/foundation/src/kinematics.rs` |
| 03 | Represent failure honestly | M1 | Domains, inequalities, finite values | Physical validity vs algebraic definition | Result, enums, match, ? operator | `crates/foundation/src/error.rs` |
| 04 | Make units visible in types | M1 | Dimensional analysis | Preventing unit swaps and scale mistakes | Tuple structs, impl blocks, Copy, newtype | `crates/units/src/lib.rs` |
| 05 | Own a small vector type | M1 | Coordinate pairs, magnitude, Pythagorean theorem | Displacement has direction and magnitude | Structs, methods, self, references, derive | `crates/math/src/vec2.rs` |
| 06 | Radians before trigonometry | M2 | Unit circle, radians, sine and cosine | Direction vectors and periodic motion | Associated functions, constructors, constants | `crates/units/src/angle.rs` |
| 07 | Sample a changing state | M2 | Functions as mappings and discrete samples | Continuous model vs sampled output | Ranges, Vec, iterators, collect | `crates/mechanics/src/sampling.rs` |
| 08 | Model context with enums | M2 | Coordinates need labels and transformation rules | Inertial, Earth-fixed, and body frames | Enums, match, exhaustive handling | `crates/frames/src/lib.rs` |
| 09 | Compute dot products from slices | M2 | Projection, angle, summation | Alignment, work, covariance | Slices, zip, iterators, sum | `crates/math/src/dot.rs` |
| 10 | Build a maintainable crate | M2 | Separation of model and presentation | Documenting units, frame, valid domain | lib.rs, main.rs, modules, pub, rustdoc, Git | Workspace foundation milestone |
| 11 | Treat a graph as behavior | M3 | Functions, shape, slope, intercept, extrema | State evolution and qualitative prediction | Closures, generic function parameters, sampling | `crates/numerics/src/sample.rs` |
| 12 | Approximate a derivative | M3 | Difference quotient, limits, truncation error | Instantaneous rate from samples | Higher-order functions, validation, experiments | `crates/numerics/src/differentiation.rs` |
| 13 | Connect position, velocity, acceleration | M3 | First and second derivatives; data geometry | Rates of change and endpoint policy | Windows, Option, timestamp validation | `crates/numerics/src/finite_data.rs` |
| 14 | Accumulate change | M3 | Riemann sums and trapezoids | Displacement, impulse, energy accumulation | Windows, folds, numerical APIs | `crates/numerics/src/integration.rs` |
| 15 | Release a constant-acceleration simulator | M3 | Kinematic equations and parameter sensitivity | Model assumptions and sign conventions | Crate boundaries, CLI, CSV, integration tests | `apps/motion-cli` + `scenarios/` |
| 16 | Graduate to Vec3 | M4 | 3-D dot, cross, norm, orientation | Planes, torque, angular momentum | Operator traits, robust errors, approx equality | `crates/math/src/vec3.rs` |
| 17 | Use projection and work | M4 | Dot product as scalar projection | Mechanical work and signed energy transfer | Semantic wrappers and methods | `crates/mechanics/src/work.rs` |
| 18 | Rotate coordinates | M4 | Rotation matrices and invariants | Frame transformation without stretching | Fixed arrays, sin_cos, matrix-vector multiply | `crates/frames/src/rotation2.rs` |
| 19 | Compose transformations | M4 | Noncommutativity and function composition | Frame chains and reference points | API design for ordered operations | `crates/frames/src/transform2.rs` |
| 20 | Be honest about floating point | M4 | Representation, absolute and relative error | Tolerance tied to measurement and requirement | f64, finite checks, approximate comparison | `crates/math/src/approx.rs` |
| 21 | Translate a free-body diagram | M5 | Vector sums and proportionality | Newton's second law and system boundaries | Domain modeling and pure dynamics functions | `crates/mechanics/src/dynamics.rs` |
| 22 | Implement inverse-square gravity | M5 | Inverse powers, vectors, singularities | Central gravity and geocentric radius | Constants, normalization, validated domains | `crates/orbit/src/gravity.rs` |
| 23 | Use conservation as an oracle | M5 | Invariants and diagnostic functions | Energy and angular momentum in two-body motion | Diagnostics, observability, property tests | `crates/orbit/src/diagnostics.rs` |
| 24 | Connect impulse and momentum | M5 | Integral of force and state update | Impulse, momentum, delta-v, resource cost | State updates and sign conventions | `crates/mechanics/src/impulse.rs` |
| 25 | Write a state derivative | M5 | ODE state-space form | Instantaneous change vs time advancement | State structs, derivative APIs, traits | `crates/numerics/src/dynamics.rs` |
| 26 | Take the first numerical step | M6 | Explicit Euler recurrence | Approximating continuous change | Immutable state updates and step functions | `crates/numerics/src/euler.rs` |
| 27 | Implement midpoint before RK4 | M6 | Second-order approximation and intermediate state | Sampling the vector field inside a step | Function composition and generic steppers | `crates/numerics/src/midpoint.rs` |
| 28 | Run a convergence study | M6 | Global error, observed order, logarithmic reasoning | Evidence that the method behaves as claimed | Experiment harnesses, deterministic output, CSV | `experiments/convergence/` |
| 29 | Test properties, not only examples | M6 | Invariants and metamorphic relations | Structural laws across an input domain | Property testing, reproducible seeds, generators | `crates/*/tests/properties.rs` |
| 30 | Ship a verified mechanics vertical slice | M6 | Model, numerics, uncertainty, evidence | Declared operating domain and limitations | Workspace architecture, CI, documentation, release | v0.1 mechanics release |

---

## 11. Session Structure: Attempt Page + Debrief Page

The Master Edition redesigns every session into a **two-page structure**. This replaces the current single BRIEF.md format.

### Attempt Page (you work here first)

Each attempt page has five sections:

1. **Three-column header** — Mathematics | Physical Meaning | Rust/Engineering
2. **Integrated Build** — The concrete thing you build (e.g., "Compute distance travelled by light in a measured interval and print both SI scales")
3. **By-Hand Practice** — 2-3 manual exercises before touching code (e.g., "Estimate the order of magnitude before calculating", "Convert milliseconds to seconds in a separate line", "Write the unit cancellation explicitly")
4. **Prediction Before Code** — A structured checklist you MUST fill in before coding:
   - Expected sign and order of magnitude
   - Units and coordinate frame
   - Accepted input domain
   - One likely failure
   - API signature and test names
5. **Independent Rust Drill** — A language-fluency exercise SEPARATE from the physics build (e.g., "From a blank file, write a pure multiply function, a named constant, formatted output, and two assertions")
6. **Tests Written First** — Specific test cases named before implementation
7. **Gate:** "DO NOT OPEN THE DEBRIEF UNTIL: hand result exists / API is sketched / tests are named / first implementation attempt compiles or has a diagnosed error"

### Debrief Page (review after your attempt)

Each debrief page has:

1. **Hint Ladder** — 3 progressive hints (e.g., Hint 1: milli means 10^-3. Hint 2: d = vt. Hint 3: name conversions instead of hiding them)
2. **Failure Campaign** — A specific way to break the code and what to observe (e.g., "Remove the millisecond conversion and explain the 1000x error")
3. **Repository Destination** — Where this code migrates in the workspace (e.g., `crates/foundation/src/units.rs`)
4. **Python / Independent Check** — How to cross-validate (e.g., "Recompute in a one-line Python script only after the Rust result is predicted")
5. **Reference Shape** — A minimal code skeleton to compare against your attempt — only after you've tried
6. **Mastery Claim** — A single sentence claim you must be able to defend (e.g., "Explain why compiling successfully does not prove physical correctness")
7. **Delayed Gate** — Complete after at least one week: recreate API from memory, solve a changed case by hand, explain the failure experiment, reproduce from a clean clone

---

## 12. The Four Knowledge Spines

The full curriculum is a dependency graph across four spines. Each module has a core capability, why it matters, build evidence, a practice pattern, and a module gate.

### Mathematics (M0-M10)

**The dependency chain:** Algebra + functions → Calculus + linear algebra → ODEs + probability + numerics → Advanced branches

| Module | Core Capability | Build Evidence |
|--------|----------------|----------------|
| **M0** Diagnostic and repair | Arithmetic, signs, fractions, scientific notation, unit conversion, graph reading | 25-question diagnostic + 3 coding checks |
| **M1** Algebra and functions | Equations, inequalities, exponents, logarithms, systems, composition, inverse functions, asymptotics | Equation evaluator, unit-aware scaling lab, growth/decay simulator |
| **M2** Geometry, trigonometry, vectors | Radians, unit circle, components, projections, coordinate systems, rotations | Vec2/Vec3 toolkit, frame drawing notebook, rotation test suite |
| **M3** Calculus I | Limits, derivatives, optimization, integrals, Fundamental Theorem | Finite-difference lab, numerical accumulation report |
| **M4** Calculus II | Integration methods, improper integrals, sequences, convergence, power/Taylor series, polar/parametric curves | Taylor approximation lab, convergence visualizer |
| **M5** Linear algebra | Vector spaces, transformations, basis, rank, orthogonality, least squares, eigenstructure, conditioning | Small matrix library, least-squares fit, conditioning experiment |
| **M6** Multivariable and vector calculus | Partial derivatives, gradients, Jacobians, multiple integrals, divergence, curl | Gradient checker, field visualizer |
| **M7** Differential equations and dynamical systems | First/second order ODEs, systems, phase space, stability, Laplace methods | Integrator library, oscillator phase portrait, stability experiments |
| **M8** Probability, statistics, and uncertainty | Distributions, expectation, covariance, Bayes, regression, uncertainty propagation | Sensor-noise lab, least-squares fit, Monte Carlo report |
| **M9** Numerical mathematics | Floating point, roots, interpolation, linear systems, ODEs, optimization, convergence, conditioning | Verified numerical toolkit with reference comparisons |
| **M10** Advanced branches | PDEs, Fourier analysis, complex analysis, tensors, stochastic processes, optimization, differential geometry | Specialization-specific research replication |

### Physics and Engineering (P0-P8)

**Principle:** Do not learn space as "orbital mechanics plus software." Astronautical practice also requires space environment, attitude determination and control, telecommunications, structures, propulsion, modeling, simulation, computing, testing, and design.

| Module | Core Capability | Build Evidence |
|--------|----------------|----------------|
| **P0** Measurement and experimental practice | Units, calibration, uncertainty budgets, sensors, sampling, bias, reproducibility | Pendulum or IMU experiment with model-vs-data comparison |
| **P1** Mechanics and rigid-body dynamics | Kinematics, forces, energy, momentum, rotation, gravitation, non-inertial frames | Mechanics simulator + physical validation |
| **P2** Oscillations, waves, and signals | SHM, damping, resonance, Fourier thinking, sampling, filters | Vibration signal lab + spectral analysis |
| **P3** Electricity, magnetism, circuits, electronics | Fields, potential, circuits, capacitance, inductance, sensors, ADC/DAC, grounding | Instrumented sensor with noise characterization |
| **P4** Thermodynamics and heat transfer | Energy, entropy, conduction, convection, radiation, transient thermal networks | Spacecraft thermal-node simulator + balance test |
| **P5** Materials and structures | Statics, stress/strain, beams, torsion, buckling, fatigue, fracture, composites | Beam deflection test + FEA comparison |
| **P6** Fluids and compressible flow | Conservation laws, viscosity, boundary layers, nozzles, shocks, dimensional analysis | Pipe/nozzle model + CFD literacy lab |
| **P7** Propulsion and power conversion | Rocket equation, thermochemistry, nozzle flow, feed systems, electric propulsion | Propulsion trade study with performance and constraints |
| **P8** Space environment | Radiation, charging, plasma, thermal cycles, debris, dust, atomic oxygen, contamination | Environment threat matrix + mitigation design |

### Programming and Systems (C1-C9)

**Principle:** Language use and language study are different. Using Rust to implement an equation teaches application. Dedicated practice is still required for ownership, library contracts, code reading, debugging, architecture, concurrency, build systems, and real repositories.

| Module | Core Capability | Build Evidence |
|--------|----------------|----------------|
| **C1** Rust language fluency | Syntax retrieval, ownership, borrowing, structs, enums, Option/Result, iterators, modules, tests | Daily handwritten API + implementation + compiler explanation |
| **C2** Rust abstraction and architecture | Traits, generics, associated types, conversions, domain modeling, workspace design | Refactor foundation repo into reusable crates |
| **C3** Algorithms and data structures | Complexity, arrays, hash maps, trees, graphs, queues, numerical layouts | Implement, benchmark, and explain trade-offs |
| **C4** Linux, debugging, and developer tools | Shell, Git, processes, files, build tools, debugger, profiler, sanitizers, CI | Reproduce and minimize failures from a clean environment |
| **C5** Computer systems and concurrency | CPU/cache, stack/heap, OS, threads, channels, atomics, networking, observability | Memory and scheduling experiments |
| **C6** Python scientific ecosystem | Packaging, NumPy shapes, broadcasting, views/copies, SciPy, plotting, testing | Independent reference implementations and analysis |
| **C7** C and C++ ecosystem | C ABI, RAII, STL, templates, CMake, sanitizers, interoperability | Rust/C++ bridge and comparison report |
| **C8** Embedded and real-time | no_std, interrupts, peripherals, RT scheduling, deterministic state machines, HIL | QEMU or microcontroller telemetry component |
| **C9** Software assurance and security | Requirements, reviews, fuzzing, formal methods, supply chain, threat modeling | Assurance case for a safety-critical component |

### Space Systems (S1-S9)

**Principle:** Design backward from mission responsibility. Systems engineering is not paperwork — it is the disciplined reasoning that connects mission intent, technical decisions, interfaces, evidence, and lifecycle risk.

| Module | Core Capability | Build Evidence |
|--------|----------------|----------------|
| **S1** Systems engineering and mission architecture | Stakeholders, ConOps, requirements, interfaces, trade studies, risk, V&V, reviews | Mission concept package with requirements matrix |
| **S2** Orbital mechanics and mission analysis | Two-body motion, elements, frames/time, maneuvers, Lambert, ephemerides, perturbations, uncertainty | Validated cislunar or Earth-orbit trade study |
| **S3** Attitude, guidance, navigation, control (GNC) | Rigid-body dynamics, quaternions, sensors, actuators, control, estimation, guidance | CubeSat ADCS simulation with faults |
| **S4** Spacecraft subsystems | Power, thermal, structures, communications, propulsion, avionics, payloads | Subsystem budgets + coupled trade study |
| **S5** Flight software and avionics | Command/telemetry, buses, scheduling, fault management, cFS/F Prime concepts, HIL | Flight-like component with telemetry, safe modes, fault injection |
| **S6** Ground systems and operations | Tracking, commanding, mission planning, contact windows, anomaly response, configuration | Operations rehearsal + anomaly playbook |
| **S7** Reliability, safety, and qualification | FMEA/FTA, redundancy, environmental test, acceptance, qualification, human factors | Verification plan + evidence package |
| **S8** AI, autonomy, and robotics | Perception, planning, SLAM, RL, anomaly detection, edge inference, assurance, fallback | Physics baseline + ML hybrid with uncertainty and safe fallback |
| **S9** Human spaceflight and habitats | ECLSS, radiation health, habitats, logistics, human factors, planetary surface systems | Closed-loop habitat resource simulation |

---

## 13. Specialization Tracks and Evidence Ladder

Choose depth only after exposure. The manual defines seven specialization tracks:

| Track | Foundation Emphasis | Strong First Capstone |
|-------|-------------------|----------------------|
| Simulation / computational physics | Numerics, mechanics, PDEs, performance | Validated multiphysics simulator |
| GNC and estimation | Linear algebra, probability, dynamics, controls | ADCS or navigation estimator with residual analysis |
| Flight software / embedded | Rust/C/C++, OS, real time, interfaces, assurance | Flight-like component with HIL and faults |
| Mission analysis / astrodynamics | Dynamics, optimization, frames/time, uncertainty | Cislunar trade study validated against independent tools |
| Thermal / propulsion / structures | Thermo, fluids, materials, PDEs, experimental methods | Subsystem design with test or reference correlation |
| Scientific AI / autonomy | Probability, optimization, software, controls, assurance | Physics baseline + hybrid model + uncertainty + fallback |
| Human systems / habitats | Thermal, fluids, life science, reliability, logistics | Closed-loop habitat resource and fault simulation |

### Evidence Ladder

| Level | Artifact | What It Proves |
|:-----:|----------|----------------|
| 1 | Small verified crate with math-to-code mapping, tests, documentation | You can map math to clean Rust |
| 2 | Validated simulator with convergence, independent comparison, declared domain | You distinguish model, numerical, and software correctness |
| 3 | Flight-like component with telemetry, faults, replay, operational behavior | You can design for operations and failure |
| 4 | Cross-language or embedded integration: ABI, hardware, timing, toolchain | You understand real ecosystems and constraints |
| 5 | Scientific AI hybrid with baseline, uncertainty, OOD behavior, safe fallback | You can use ML without surrendering physical judgment |
| 6 | External contribution or research replication surviving unfamiliar code and review | Your work survives independent comparison |
| 7 | Mission capstone with requirements, architecture, subsystem trade-offs, V&V, defense | You can integrate everything |

---

## 14. Repository Transformation Plan

The manual's most important structural directive: **do not discard the original 30 sessions. Preserve them as evidence of growth, then migrate stable concepts into domain crates.**

### Target Architecture

```
delta-v/
├── Cargo.toml                  # Rust workspace root
├── README.md                   # mission, quickstart, evidence map
├── rust-toolchain.toml
├── .github/workflows/ci.yml
├── docs/
│   ├── architecture.md
│   ├── learning-log/
│   ├── adr/                    # architecture decision records
│   └── reviews/
├── crates/
│   ├── units/                  # quantities, angles, frames
│   ├── math/                   # Vec2, Vec3, matrices, approx
│   ├── numerics/               # differentiation, integration, ODEs
│   ├── mechanics/              # motion, forces, energy, oscillators
│   ├── frames/                 # tagged states and transforms
│   ├── orbit/                  # gravity, propagation, diagnostics
│   ├── estimation/             # later: least squares, filters
│   ├── control/                # later: PID, state space
│   └── telemetry/              # later: packets, logs, replay
├── apps/
│   ├── frontier-cli/
│   └── scenario-runner/
├── python/
│   ├── pyproject.toml
│   ├── frontier_validation/
│   └── notebooks/
├── scenarios/
├── experiments/
├── reports/
└── legacy-30/                  # preserved original attempts
```

**Architecture principle:** Concepts graduate from session experiments into stable crates only after their API, tests, units, and operating domain are understood.

### Migration Plan (7 Steps)

| Step | Action |
|------|--------|
| 1 | Create a protected tag and branch for the current state |
| 2 | Add a workspace root without moving code yet |
| 3 | Create units, math, numerics, and mechanics crates |
| 4 | Move one concept at a time with tests intact; never a giant rewrite |
| 5 | Preserve original attempts in legacy-30 and link each to the upgraded implementation |
| 6 | Add Python validation as an independent package, not loose notebooks only |
| 7 | Create scenarios, reports, ADRs, and CI after the first migrated vertical slice |

### Migration Acceptance Checklist

| Check | Evidence |
|-------|----------|
| No behavior silently changed | Old and new tests run against the same cases |
| No duplicate foundational types | One canonical Vec3, Angle, and quantity policy |
| Public API has a physical contract | Units, frame, domain, errors, examples |
| History remains inspectable | Links from legacy session to migrated implementation |
| Clean clone is reproducible | README command and CI artifact |

### Repository Rules

| Rule | Why |
|------|-----|
| One concept per commit until composition is necessary | Creates a readable reasoning trail |
| Write tests and physical predictions before implementation | Prevents tests from merely blessing the code |
| No hidden units, frames, or time scales | Many aerospace failures are context failures |
| Separate model, numerics, I/O, and presentation | Allows replacement and independent testing |
| Every experiment is deterministic or logs its seed | Failure must be reproducible |
| Every release states what is NOT validated | Honest limits are an engineering deliverable |

### Commit Message Language

**Good:**
- `feat(units): prevent degree/radian swaps`
- `test(gravity): add inverse-square property`
- `fix(integrator): land exactly on final time`

**Weak:**
- `update stuff`
- `finished day 12`
- `AI changes`

---

## 15. Quality Gates and CI

### Local Finish Command

```bash
cargo fmt --all
cargo clippy --workspace --all-targets -- -D warnings
cargo test --workspace
cargo doc --workspace --no-deps
python -m pytest python
```

### Definition of Done

- Known result and edge case
- Structural property or invariant
- Independent comparison where available
- Failure experiment and operating domain
- README command from clean clone
- Engineering log and review date

### Starter CI

```yaml
name: ci
on: [push, pull_request]
jobs:
  rust:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: dtolnay/rust-toolchain@stable
        with: { components: rustfmt, clippy }
      - run: cargo fmt --all -- --check
      - run: cargo clippy --workspace --all-targets -- -D warnings
      - run: cargo test --workspace
      - run: cargo doc --workspace --no-deps
  python:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.12' }
      - run: pip install -e 'python[dev]'
      - run: pytest python
```

**Do not add tooling ceremonially.** CI exists to preserve evidence and catch regression; benchmarks exist only after a performance requirement; abstractions exist only after repeated behavior.

---

## 16. Resource Directory

Use one primary anchor and one practice source per module. Resource collecting is not progress.

### Mathematics
- MIT OCW: Single Variable Calculus, Linear Algebra, Differential Equations, Probability and Statistics
- OpenStax: Calculus (Vol. 1-3), University Physics

### Physics and Aerospace
- MIT OCW: Classical Mechanics, Electricity and Magnetism, Vibrations and Waves, Unified Engineering
- NASA: Systems Engineering Handbook, Software Engineering Handbook, Technical Standards System

### Programming
- The Rust Programming Language (The Book)
- Rustlings (small exercises)
- Rust by Example (concise recall)
- Rust standard documentation (contracts, not recipes)
- Python Packaging User Guide, NumPy user guide, SciPy docs, Matplotlib tutorials

### How to Practice Each Knowledge Type

| Knowledge Type | Best Practice | Weak Substitute |
|---------------|---------------|-----------------|
| Algebra/calculus procedures | Mixed hand problems with delayed retrieval and explanation | Watching worked solutions |
| Physical intuition | Prediction, diagrams, scale, limiting cases, experiment | Memorizing formula lists |
| Rust syntax | Blank-file retrieval and compiler-guided correction | Copying examples |
| Ownership and architecture | Trace data, refactor, read real code, explain rejected designs | Adding clones until it compiles |
| Libraries | Read contracts, build tiny example, inspect types, test edge behavior | Searching for snippets only |
| Numerical methods | Convergence, invariants, independent tools, failure sweeps | One visually plausible plot |
| Systems engineering | Requirements, interfaces, trade study, V&V plan, review | Architecture diagrams without decisions |
| Research papers | Reproduce one claim and document deviations | Summarizing abstracts |

---

## 17. Engineering Opinion: Where This Repo Should Deviate

The sections above are faithful to the PDF. This section is engineering judgment on how to actually get there. The manual is excellent but parts of it are aspirational scaffolding — implementing it literally would create empty directories and stub crates that violate the "zero vaporware" principle.

### What the current repo already does well
- The 7-step loop is fully documented in `docs/method.md`
- 30 session scaffolds exist with BRIEF.md, Cargo.toml, and src/main.rs
- Supporting docs (formula reference, concept map, predict practice) are solid
- The session generator script handles lifecycle management

### What needs to change, in priority order

**Phase 1: Structural foundation (do this now, no code changes needed)**
1. Add a root `Cargo.toml` workspace file. Do NOT add first_30/ to the workspace yet — the PDF says "add workspace root without moving code" as step 2. The sessions stay independent until concepts graduate.
2. Create the `crates/` directory structure with empty crate stubs (Cargo.toml + src/lib.rs with a doc comment only). These are landing zones, not implementations.
3. Create `python/` with a minimal `pyproject.toml` and empty `frontier_validation/` package.
4. Create `scenarios/`, `experiments/`, `reports/` as empty directories (with .gitkeep).
5. Add `.github/workflows/ci.yml` with the starter CI from section 15.
6. Add `rust-toolchain.toml` pinning the stable toolchain.
7. Create `docs/adr/` (Architecture Decision Records directory) with a README template.
8. Create `docs/learning-log/` and `docs/reviews/`.

**Phase 2: Session format upgrade (do this as you work through sessions, not all at once)**
9. The BRIEF.md format should be upgraded to the two-page Attempt + Debrief structure. But do NOT rewrite all 30 at once. Upgrade them as you reach each session. The session generator script should be updated to produce the new format for new sessions.
10. Add the "Repository Destination" field to each BRIEF.md so sessions know where their code will eventually migrate.

**Phase 3: Concept graduation (happens naturally as you learn)**
11. As you complete sessions, migrate stable, well-tested concepts into their target crates. The first graduation target is Session 01's unit conversion → `crates/units/`. This is the "one concept at a time with tests intact" rule.
12. When a session's code graduates, keep the original in `first_30/` (or rename to `legacy-30/` at the first migration) and add a link comment pointing to the crate.

**Phase 4: Python validation layer**
13. After the first 3-4 Rust concepts are in crates, add Python reference implementations in `python/frontier_validation/` that cross-check Rust output. Start with the simple ones: unit conversion, distance computation, vector operations.

### Where I disagree with the manual

1. **The 104-unit/13-stage curriculum vs the 40-module graph.** The manual defines both but they don't map cleanly. The repo's `docs/curriculum.md` has 104 units in 13 stages. The manual has M0-M10 (11 modules), P0-P8 (9 modules), C1-C9 (9 modules), S1-S9 (9 modules) = 38 modules. My recommendation: keep the 104-unit map as the session-level execution plan, and add the 40-module graph as the knowledge-level map. They serve different purposes — sessions are what you DO, modules are what you KNOW.

2. **Don't rename first_30/ to legacy-30/ yet.** The PDF says to preserve originals in legacy-30/, but renaming before any migration happens creates confusion (broken links, broken relative paths in BRIEF.md files). Keep `first_30/` until the first concept actually graduates to a crate, then rename with a proper redirect file.

3. **The daily study system (3hr25min blocks) is a guide, not a rule.** The 75-minute minimum viable day is the real floor. Documenting the full system is useful, but trying to force a rigid schedule on self-paced study defeats the purpose. The structure should serve the learner, not the other way around.

4. **Don't create all 9 crate stubs upfront.** The manual lists units, math, numerics, mechanics, frames, orbit, estimation, control, telemetry. Only the first 6 are reached by Session 30. estimation, control, and telemetry are "later" — creating empty stubs for them now is vaporware. Create stubs only for crates that will be populated within the first 30 sessions: units, math, numerics, mechanics, frames, orbit. Add the rest when you reach them.

5. **The 6-mission grouping should be added to CATALOG.md.** This is a high-value, low-effort change. The missions give structure to the 30 sessions and each has a clear release target.

### What I would NOT do

- Do not try to scaffold all 40 knowledge modules (M/P/C/S) as directories. They are learning goals, not code directories. Document them in the field manual, track progress separately.
- Do not create empty Python notebooks. The Python layer earns its place when there's Rust output to validate.
- Do not set up benchmarks until a performance requirement exists.
- Do not add formal methods tooling (TLA+, Kani) until Stage 9.

---

## Closing Principle

> **Build evidence that survives challenge.**
>
> Prediction before calculation. Derivation before implementation. Tests before confidence. Failure before trust. Explanation before advancement.

---

*This document is maintained alongside the codebase. When the PDF is updated, this file should be reconciled. When the repository structure changes, sections 14-17 should be updated to reflect reality.*
