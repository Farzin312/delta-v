# The Complete Curriculum

This repository implements the **Frontier Engineer Field Manual**: a dependency-driven, 104-unit path from high-school algebra to mission-grade computational space systems engineering. Unit numbers indicate prerequisite depth and rising difficulty -- never calendar time. You may spend two days on one unit, or a month. Advance only when the mastery gate is met.

---

## Quick Reference: All 13 Stages

| Stage | Focus | Units | One-line purpose |
|:-----:|-------|:-----:|------------------|
| 1 | Rust + Mathematical Language | 1-8 | Make equations executable from Day 1 |
| 2 | Calculus + Numerical Mechanics | 9-16 | Rates, accumulation, ODEs, forces, energy |
| 3 | Orbital Mechanics Core | 17-24 | Two-body dynamics, elements, frames, time |
| 4 | Mission Analysis | 25-32 | Transfers, Lambert, optimization, validation |
| 5 | Attitude + Control | 33-40 | Quaternions, sensors, actuators, feedback, LQR |
| 6 | Estimation + Signals | 41-48 | Probability, Kalman filtering, FFTs, fusion |
| 7 | Systems + Embedded | 49-56 | Memory, OS, C/C++ bridges, real-time, hardware |
| 8 | Flight Software Architecture | 57-64 | Telemetry/command, protocols, cFS/F Prime, FDIR |
| 9 | Verification + Security | 65-72 | V&V, fuzzing, formal methods, threat modeling |
| 10 | Scientific AI | 73-80 | ML, physics-informed models, uncertainty, assurance |
| 11 | Robotics + Autonomy | 81-88 | Perception, SLAM, planning, multi-agent systems |
| 12 | Multiphysics Space Systems | 89-96 | Thermal, fluids, structures, power, comms, EDL |
| 13 | Specialization + Public Evidence | 97-104 | Research replication, capstone, public contribution |

---

## Stage 1: Rust + Mathematical Language (Units 1-8)

> **Prerequisite:** None beyond algebra and willingness to practice.
> **Goal:** Every equation becomes executable Rust from the first session.

| Unit | Math / Computing | Physical Meaning | Rust / Engineering | Build Evidence |
|:----:|-------------------|------------------|---------------------|----------------|
| 1 | Toolchain, units, variables | Unit conversion and equations | Bindings, f64, cargo, println! | Unit-safe conversion CLI |
| 2 | Algebra as equation control | Scale, sign, dimensional checks | Functions, tests, Result | Equation evaluator with validation |
| 3 | Radians and trigonometry | Components and periodic motion | Structs, methods, ownership | 2-D vector and angle toolkit |
| 4 | Functions and graphs | Position, velocity, sampling | Loops, iterators, CSV | Motion-table generator |
| 5 | Limits and derivatives | Instantaneous rate | Slices, closures, tolerances | Finite-difference laboratory |
| 6 | Integrals and accumulation | Area, impulse, distance | Folds, accumulators, errors | Trapezoid integrator |
| 7 | Vectors and matrices | Frames and rotations | Arrays, traits, modules | Vec3 + rotation library |
| 8 | Measurement and probability | Noise, bias, uncertainty | Enums, parsing, test fixtures | Sensor-summary tool |

**Stage Gate:** Defend the capstone without AI-generated explanations. Show requirements, derivations, API decisions, automated tests, a failure case, an independent comparison, and a reproducible release.

---

## Stage 2: Calculus + Numerical Mechanics (Units 9-16)

> **Prerequisite:** Mastery of Stage 1.

| Unit | Math / Computing | Physical Meaning | Rust / Engineering | Build Evidence |
|:----:|-------------------|------------------|---------------------|----------------|
| 9 | Newton's laws | Free-body models | Domain types, API contracts | Force-to-state simulator |
| 10 | Work, energy, momentum | Conservation diagnostics | Error enums, invariants | Energy audit report |
| 11 | Oscillation | Springs, damping, resonance | State machines, configuration | Damped oscillator simulator |
| 12 | Projectile and drag | Model fidelity and assumptions | Modules, docs, golden tests | Drag-model comparison |
| 13 | ODE initial-value problems | State and derivatives | Traits, generic dynamics | Euler and midpoint integrators |
| 14 | Runge-Kutta methods | Local/global error | Generics, reusable steppers | Verified RK4 |
| 15 | Stability and geometric methods | Step size and conserved structure | Benchmarks, property tests | Integrator showdown |
| 16 | Mechanics capstone | Reproducible simulation evidence | Crate organization, CI | Released mechanics engine |

---

## Stage 3: Orbital Mechanics Core (Units 17-24)

> **Prerequisite:** Mastery of Stage 2.

| Unit | Math / Computing | Physical Meaning | Rust / Engineering | Build Evidence |
|:----:|-------------------|------------------|---------------------|----------------|
| 17 | 3-D kinematics | Relative motion and frames | Newtypes, frame tags | Frame-aware state vectors |
| 18 | Universal gravitation | Inverse square and mu | Precision, constants, units | Gravity model |
| 19 | Two-body dynamics | Circular/elliptic motion | Composition, diagnostics | Orbit propagator v1 |
| 20 | Conics and elements | Energy, angular momentum, geometry | Robust angle handling | State/element converter |
| 21 | Kepler equation | Root finding and anomalies | Iterators, convergence Result | Kepler solver |
| 22 | Time and reference frames | UTC/TAI/TT, ECI/ECEF | Serialization, provenance | Time/frame service |
| 23 | Perturbation architecture | J2, drag, third body | Trait objects vs generics | Composable acceleration models |
| 24 | Orbit engine capstone | Validation against references | Versioned scenarios, reports | Orbit engine v1 release |

---

## Stage 4: Mission Analysis (Units 25-32)

> **Prerequisite:** Mastery of Stage 3.

| Unit | Math / Computing | Physical Meaning | Rust / Engineering | Build Evidence |
|:----:|-------------------|------------------|---------------------|----------------|
| 25 | Impulsive maneuvers | Delta-v and local frames | Command pattern, events | Maneuver sequencer |
| 26 | Hohmann, bi-elliptic, plane change | Trade studies | Parameter sweeps, Rayon | Transfer trade explorer |
| 27 | Lambert problem | Boundary-value thinking | Root bracketing, solver APIs | Lambert test harness |
| 28 | Optimization | Constraints and objectives | FFI to solver/reference tools | Launch-window search |
| 29 | SPICE ephemerides | Kernel, frame, time provenance | C FFI and safe wrappers | SPICE query CLI |
| 30 | GMAT independent truth | Cross-tool validation | Golden files, tolerances | GMAT comparison report |
| 31 | Monte Carlo uncertainty | Sensitivity and distributions | Deterministic RNG, parallel runs | Dispersion study |
| 32 | Mission analysis capstone | Requirements-to-evidence | Architecture decision records | Cislunar trade study |

---

## Stage 5: Attitude + Control (Units 33-40)

> **Prerequisite:** Mastery of Stage 4.

| Unit | Math / Computing | Physical Meaning | Rust / Engineering | Build Evidence |
|:----:|-------------------|------------------|---------------------|----------------|
| 33 | Rigid-body kinematics | Angular velocity and inertia | Matrix/quaternion types | Attitude state library |
| 34 | Quaternions | Composition and normalization | Invariants, numerical tests | Quaternion test suite |
| 35 | Rigid-body dynamics | Euler equations | Coupled ODE state | Torque-free rotation |
| 36 | Attitude sensors | Gyro, sun/star sensors | Interfaces, mocks, noise | Sensor simulator |
| 37 | Actuators | Wheels, thrusters, saturation | State machines, limits | Actuator allocator |
| 38 | Feedback and PID | Stability and tuning | Controller traits, telemetry | Closed-loop pointing demo |
| 39 | State-space and LQR | Linearization and eigenstructure | Linear algebra backend | LQR controller |
| 40 | ADCS capstone | Safe modes and fault cases | Scenario runner, fault injection | CubeSat ADCS simulator |

---

## Stage 6: Estimation + Signals (Units 41-48)

> **Prerequisite:** Mastery of Stage 5.

| Unit | Math / Computing | Physical Meaning | Rust / Engineering | Build Evidence |
|:----:|-------------------|------------------|---------------------|----------------|
| 41 | Probability foundations | Random variables and covariance | Distribution sampling | Uncertainty notebook + Rust core |
| 42 | Least squares | Residuals and identifiability | Matrix decompositions | Orbit fit from noisy data |
| 43 | Bayesian updating | Prior, likelihood, posterior | Typed distributions | Scalar Bayes filter |
| 44 | Kalman filtering | Recursive estimation | Generic filter traits | Kalman filter implementation |
| 45 | Extended/unscented variants | Nonlinear estimation | Trait composition | EKF/UKF comparison |
| 46 | Frequency-domain analysis | Spectra, filtering, windows | FFT interfaces | Vibration spectrum analyzer |
| 47 | Sensor fusion | Complementary/Kalman fusion | Multi-sensor pipelines | IMU + star tracker fusion |
| 48 | Estimation capstone | Real-data validation | Reproducible pipeline | Navigation filter on real data |

---

## Stage 7: Systems + Embedded (Units 49-56)

> **Prerequisite:** Mastery of Stage 6.

| Unit | Math / Computing | Physical Meaning | Rust / Engineering | Build Evidence |
|:----:|-------------------|------------------|---------------------|----------------|
| 49 | Computer architecture | CPU, memory, caches, representation | Layout, stack/heap, unsafe boundary | Memory experiment suite |
| 50 | Operating systems | Processes, threads, syscalls | Files, sockets, timing | Linux systems lab |
| 51 | C and C++ bridge | ABI, ownership across boundaries | bindgen/cxx, sanitizers | Rust/C++ dynamics bridge |
| 52 | Bare-metal foundations | Registers and peripherals | no_std, HAL concepts | QEMU microcontroller lab |
| 53 | Interrupts and timers | Latency and determinism | Critical sections, atomics | Timer-driven task |
| 54 | Real-time systems | Deadlines and scheduling | Queues, bounded memory | Mini scheduler simulation |
| 55 | Concurrency | Race freedom and backpressure | Threads, channels, async tradeoffs | Concurrent telemetry pipeline |
| 56 | Embedded capstone | Resource budgets and failure | Cross compilation, HIL plan | Flight-computer prototype |

---

## Stage 8: Flight Software Architecture (Units 57-64)

> **Prerequisite:** Mastery of Stage 7.

| Unit | Math / Computing | Physical Meaning | Rust / Engineering | Build Evidence |
|:----:|-------------------|------------------|---------------------|----------------|
| 57 | Networking fundamentals | Packets, latency, loss | TCP/UDP, serialization | Ground-link simulator |
| 58 | Space data protocols | Telemetry, command, framing | Binary formats, CRC | Packet encoder/decoder |
| 59 | cFS architecture | Executive, bus, OS abstraction | Read C, build an app | cFS integration note |
| 60 | F Prime architecture | Components, ports, topology | Read C++, FPP models | F Prime component |
| 61 | Fault detection/isolation/recovery | Hazards and safe modes | Watchdogs, state machines | FDIR demo |
| 62 | Reliability and redundancy | Voting, failover, degraded modes | Determinism, restartability | Redundant service simulator |
| 63 | Software/hardware-in-loop | Models, mocks, instrumentation | Test harness orchestration | HIL test plan |
| 64 | Flight software capstone | Operations and anomaly response | Release/config management | Mission operations rehearsal |

---

## Stage 9: Verification + Security (Units 65-72)

> **Prerequisite:** Mastery of Stage 8.

| Unit | Math / Computing | Physical Meaning | Rust / Engineering | Build Evidence |
|:----:|-------------------|------------------|---------------------|----------------|
| 65 | Scientific verification | Correct equation vs code vs use | Oracle hierarchy, convergence | V&V dossier |
| 66 | Testing depth | Unit/property/metamorphic/fuzz | proptest, cargo-fuzz, Miri | Adversarial test campaign |
| 67 | Formal methods | Invariants and state exploration | TLA+/Kani concepts | Verify a command state machine |
| 68 | Safety engineering | Hazards, controls, assurance cases | Traceability, reviews | Mini safety case |
| 69 | Space threat modeling | Assets, trust boundaries, attack paths | Least privilege, secure parsing | Threat model |
| 70 | Cryptography and PQC | Integrity, identity, key lifecycle | Use libraries; no custom crypto | Signed command prototype |
| 71 | Supply chain and secure build | Dependencies and provenance | SBOM, lockfiles, CI policy | Reproducible secure build |
| 72 | MBSE and standards | Requirements, interfaces, CCSDS | Schemas and trace links | Digital thread package |

---

## Stage 10: Scientific AI (Units 73-80)

> **Prerequisite:** Mastery of Stage 9.

| Unit | Math / Computing | Physical Meaning | Rust / Engineering | Build Evidence |
|:----:|-------------------|------------------|---------------------|----------------|
| 73 | Python as scientific partner | Exploration vs production | PyO3/maturin, NumPy | Python/Rust reference pair |
| 74 | Statistics and experimental design | Splits, leakage, baselines | Data pipelines, manifests | Reproducible experiment |
| 75 | Classical ML | Regression/classification | Feature pipelines, evaluation | Telemetry classifier |
| 76 | Neural networks | Optimization and representation | PyTorch training, Rust inference | Small inference service |
| 77 | Physics-informed ML | Constraints and residual losses | Hybrid model interfaces | Residual-correction model |
| 78 | Anomaly detection | Novelty, drift, false alarms | Streaming metrics | Spacecraft anomaly detector |
| 79 | Uncertainty and calibration | Confidence vs correctness | Calibration tests, OOD checks | AI assurance report |
| 80 | AI capstone | Human authority and safe envelopes | Fallbacks, monitoring | Guarded autonomy demo |

---

## Stage 11: Robotics + Autonomy (Units 81-88)

> **Prerequisite:** Mastery of Stage 10.

| Unit | Math / Computing | Physical Meaning | Rust / Engineering | Build Evidence |
|:----:|-------------------|------------------|---------------------|----------------|
| 81 | Robot geometry | Transforms and kinematic chains | Graph and transform types | Arm/rover kinematics |
| 82 | Perception | Camera/lidar models | Image buffers, FFI | Terrain feature pipeline |
| 83 | Localization and SLAM | Pose, landmarks, uncertainty | Sparse data structures | 2-D localization demo |
| 84 | Path planning | Graphs, A*, sampling | Priority queues, heuristics | Lunar path planner |
| 85 | Motion planning and control | Dynamics and constraints | Trajectory interfaces | Rover tracking controller |
| 86 | Planning and scheduling | Resources and temporal constraints | Search, constraint models | Mission scheduler |
| 87 | Multi-agent autonomy | Coordination and communications | Distributed state, partitions | Robot team simulator |
| 88 | Autonomy capstone | Intent, explainability, recovery | Decision logs, replay | Lunar operations challenge |

---

## Stage 12: Multiphysics Space Systems (Units 89-96)

> **Prerequisite:** Mastery of Stage 11.

| Unit | Math / Computing | Physical Meaning | Rust / Engineering | Build Evidence |
|:----:|-------------------|------------------|---------------------|----------------|
| 89 | Thermodynamics | Energy, entropy, cycles | Unit-safe models | Habitat heat balance |
| 90 | Fluid mechanics | Conservation and dimensionless groups | Finite-volume concepts | 1-D nozzle/pipe model |
| 91 | CFD foundations | PDE discretization, stability | Grids, sparse solvers | Advection-diffusion solver |
| 92 | Structures and vibration | Stress, modes, resonance | Eigen analysis | Structural mode study |
| 93 | Thermal systems | Conduction, radiation, control | Network models | Spacecraft thermal network |
| 94 | Power systems | Generation, storage, loads | Schedulers, constraints | Lunar power budget |
| 95 | Communications | Link budgets and coding | Signal/noise calculations | Deep-space link tool |
| 96 | Entry, descent, landing | Atmosphere, heating, GNC integration | 6-DOF architecture | EDL trade study |

---

## Stage 13: Specialization + Public Evidence (Units 97-104)

> **Prerequisite:** Mastery of Stage 12.

| Unit | Math / Computing | Physical Meaning | Rust / Engineering | Build Evidence |
|:----:|-------------------|------------------|---------------------|----------------|
| 97 | Choose specialization | Problem/mission fit | Repository and research plan | Capstone proposal |
| 98 | Literature replication | Paper-to-equations-to-tests | Reproducible workflow | Replication report |
| 99 | Open-source reconnaissance | Architecture and issue selection | Code review and contribution | First upstream PR |
| 100 | Capstone architecture | Requirements and interfaces | ADRs, threat/V&V plans | PDR package |
| 101 | Capstone implementation I | Correct baseline | Small reviewed increments | Vertical slice |
| 102 | Capstone implementation II | Fidelity and performance | Profiling, fault cases | Integrated system |
| 103 | Independent validation | Reference tools and reviewers | Release candidate, audit | CDR/V&V package |
| 104 | Capstone defense | Engineering judgment | Public release, presentation | Defended capstone |

---

## Portfolio Evidence Ladder

Progress isn't measured in units completed -- it's measured in artifacts that other engineers can reproduce, challenge, and extend.

| Level | Artifact | What it proves |
|:-----:|----------|----------------|
| 1 | Small crate + tests + derivation note | You can map math to clean Rust |
| 2 | Validated simulator + convergence report | You distinguish model, numerical, and software correctness |
| 3 | Flight-like component + faults + telemetry | You can design for operations and failure |
| 4 | Cross-language/embedded integration | You understand real ecosystems, ABI, hardware, and constraints |
| 5 | Scientific AI hybrid + uncertainty + baseline | You can use ML without surrendering physical judgment |
| 6 | External contribution or research replication | Your work survives unfamiliar code, review, and independent comparison |
| 7 | Mission capstone + PDR/CDR-style evidence | You can integrate requirements, architecture, physics, software, safety, and communication |

---

## Competitive Positioning

The goal is not to be "better at everything." It is to own the rare overlap most candidates leave empty.

| Candidate Profile | Typical Strength | Typical Gap | Your Counter-Position |
|--------------------|------------------|-------------|----------------------|
| General software engineer | Product delivery, APIs, cloud | Weak physics, numerics, embedded | Validated simulators, domain types, convergence studies, hardware interfaces |
| Physics graduate | Derivation, models, research reading | Production systems, testing depth | Ship reusable Rust/Python tools with tests, benchmarks, and independent validation |
| Aerospace/GNC graduate | Dynamics, controls, MATLAB/Python | Systems programming, real-time code | Add Rust/C++ depth, OS/embedded, flight frameworks, fuzzing, CI |
| ML engineer | Training pipelines, models, deployment | Physical constraints, uncertainty, control | Physics baselines, hybrid models, calibration, OOD tests, constrained autonomy |
| Rust specialist | Memory safety, performance, concurrency | Mission domain and scientific evidence | cFS/F Prime interop, dynamics, telemetry, estimation, mission scenarios |

---

## Back to the root

[<- README](../README.md)  |  [<- Documentation Index](INDEX.md)
