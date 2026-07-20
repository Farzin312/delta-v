# Knowledge Spine Tracker

> Tracks progress across the four knowledge spines from the Field Manual.
> Sessions (first_30/) are the EXECUTION plan - what you DO.
> Modules below are the KNOWLEDGE map - what you KNOW.

---

## How to Read This File

Each module lists:
- **Core capability** - what you should be able to do
- **Status** - NOT STARTED / DIAGNOSED / IN PROGRESS / WORKING / SPECIALIZED
- **Sessions** - which first_30 sessions exercise this module
- **Evidence** - what artifact proves you own this

Update the status after each session and after each diagnostic.

---

## Mathematics (M0-M10)

| Module | Core Capability | Status | Sessions | Evidence |
|--------|----------------|--------|----------|----------|
| **M0** Diagnostic | Arithmetic, signs, fractions, scientific notation, unit conversion | NOT STARTED | 01 | 25-question diagnostic score |
| **M1** Algebra and functions | Equations, inequalities, exponents, logarithms, systems, composition, inverses, asymptotics | NOT STARTED | 01, 02, 03 | Equation evaluator |
| **M2** Geometry, trig, vectors | Radians, unit circle, components, projections, coordinate systems, rotations | NOT STARTED | 05, 06, 08, 09, 16, 17, 18, 19 | Vec2/Vec3 toolkit, rotation suite |
| **M3** Calculus I | Limits, derivatives, optimization, integrals, Fundamental Theorem | NOT STARTED | 11, 12, 13, 14 | Finite-difference lab |
| **M4** Calculus II | Integration methods, improper integrals, sequences, convergence, Taylor series, polar/parametric | NOT STARTED | 28 | Taylor approx lab, convergence visualizer |
| **M5** Linear algebra | Vector spaces, transformations, basis, rank, orthogonality, least squares, eigenstructure, conditioning | NOT STARTED | (Stage 3+) | Matrix library, least-squares fit |
| **M6** Multivariable and vector calculus | Partials, gradients, Jacobians, multiple integrals, divergence, curl | NOT STARTED | (Stage 5+) | Gradient checker, field visualizer |
| **M7** Differential equations | First/second order ODEs, systems, phase space, stability, Laplace | NOT STARTED | 25, 26, 27 | Integrator library, phase portrait |
| **M8** Probability and statistics | Distributions, expectation, covariance, Bayes, regression, uncertainty propagation | NOT STARTED | (Stage 6) | Sensor-noise lab, Monte Carlo report |
| **M9** Numerical mathematics | Floating point, roots, interpolation, linear systems, ODEs, optimization, convergence, conditioning | NOT STARTED | 20, 25, 26, 27, 28, 29 | Verified numerical toolkit |
| **M10** Advanced branches | PDEs, Fourier analysis, complex analysis, tensors, stochastic processes, optimization, differential geometry | NOT STARTED | (Stage 12+) | Specialization-specific replication |

---

## Physics and Engineering (P0-P8)

| Module | Core Capability | Status | Sessions | Evidence |
|--------|----------------|--------|----------|----------|
| **P0** Measurement and experimental practice | Units, calibration, uncertainty budgets, sensors, sampling, bias, reproducibility | NOT STARTED | 01, 04, 20 | Pendulum or IMU experiment |
| **P1** Mechanics and rigid-body dynamics | Kinematics, forces, energy, momentum, rotation, gravitation, non-inertial frames | NOT STARTED | 02, 05, 15, 21, 22, 23, 24 | Mechanics simulator + validation |
| **P2** Oscillations, waves, signals | SHM, damping, resonance, Fourier thinking, sampling, filters | NOT STARTED | (Stage 2+) | Vibration signal lab |
| **P3** Electricity, magnetism, circuits | Fields, potential, circuits, capacitance, inductance, sensors, ADC/DAC, grounding | NOT STARTED | (Stage 7+) | Instrumented sensor |
| **P4** Thermodynamics and heat transfer | Energy, entropy, conduction, convection, radiation, transient thermal networks | NOT STARTED | (Stage 12) | Thermal-node simulator |
| **P5** Materials and structures | Statics, stress/strain, beams, torsion, buckling, fatigue, fracture, composites | NOT STARTED | (Stage 12) | Beam deflection test |
| **P6** Fluids and compressible flow | Conservation laws, viscosity, boundary layers, nozzles, shocks, dimensional analysis | NOT STARTED | (Stage 12) | Pipe/nozzle model |
| **P7** Propulsion and power conversion | Rocket equation, thermochemistry, nozzle flow, feed systems, electric propulsion | NOT STARTED | (Stage 12) | Propulsion trade study |
| **P8** Space environment | Radiation, charging, plasma, thermal cycles, debris, dust, atomic oxygen, contamination | NOT STARTED | (Stage 12) | Environment threat matrix |

---

## Programming and Systems (C1-C9)

| Module | Core Capability | Status | Sessions | Drills | Evidence |
|--------|----------------|--------|----------|--------|----------|
| **C1** Rust language fluency | Syntax retrieval, ownership, borrowing, structs, enums, Option/Result, iterators, modules, tests | NOT STARTED | 01-10 | drills/01-10 | Daily blank-file drill |
| **C2** Rust abstraction and architecture | Traits, generics, associated types, conversions, domain modeling, workspace design | NOT STARTED | 08-10, 25 | drills/11-15 | Crate refactor |
| **C3** Algorithms and data structures | Complexity, arrays, hash maps, trees, graphs, queues, numerical layouts | NOT STARTED | 07, 09 | drills/16-20 | Benchmark + trade-off |
| **C4** Linux, debugging, dev tools | Shell, Git, processes, files, build tools, debugger, profiler, sanitizers, CI | NOT STARTED | 10, 30 | - | Failure reproduction |
| **C5** Computer systems and concurrency | CPU/cache, stack/heap, OS, threads, channels, atomics, networking, observability | NOT STARTED | (Stage 7) | - | Memory/scheduling experiments |
| **C6** Python scientific ecosystem | Packaging, NumPy shapes, broadcasting, views/copies, SciPy, plotting, testing | NOT STARTED | 01-30 (cross-checks) | - | Reference implementations |
| **C7** C and C++ ecosystem | C ABI, RAII, STL, templates, CMake, sanitizers, interop | NOT STARTED | (Stage 7) | - | Rust/C++ bridge |
| **C8** Embedded and real-time | no_std, interrupts, peripherals, RT scheduling, deterministic state machines, HIL | NOT STARTED | (Stage 7) | - | QEMU/microcontroller component |
| **C9** Software assurance and security | Requirements, reviews, fuzzing, formal methods, supply chain, threat modeling | NOT STARTED | 29, (Stage 9) | - | Assurance case |

---

## Space Systems (S1-S9)

| Module | Core Capability | Status | Sessions | Evidence |
|--------|----------------|--------|----------|----------|
| **S1** Systems engineering and mission architecture | Stakeholders, ConOps, requirements, interfaces, trade studies, risk, V&V, reviews | NOT STARTED | 30 | Mission concept package |
| **S2** Orbital mechanics and mission analysis | Two-body motion, elements, frames/time, maneuvers, Lambert, ephemerides, perturbations | NOT STARTED | 22, 23, (Stage 3-4) | Cislunar/Earth-orbit trade study |
| **S3** Attitude, guidance, navigation, control (GNC) | Rigid-body dynamics, quaternions, sensors, actuators, control, estimation, guidance | NOT STARTED | (Stage 5) | CubeSat ADCS simulation |
| **S4** Spacecraft subsystems | Power, thermal, structures, comms, propulsion, avionics, payloads | NOT STARTED | (Stage 12) | Subsystem budgets |
| **S5** Flight software and avionics | Command/telemetry, buses, scheduling, fault management, cFS/F Prime, HIL | NOT STARTED | (Stage 8) | Flight-like component |
| **S6** Ground systems and operations | Tracking, commanding, mission planning, contact windows, anomaly response | NOT STARTED | (Stage 8) | Operations rehearsal |
| **S7** Reliability, safety, qualification | FMEA/FTA, redundancy, environmental test, acceptance, qualification | NOT STARTED | (Stage 9) | Verification plan |
| **S8** AI, autonomy, robotics | Perception, planning, SLAM, RL, anomaly detection, edge inference, assurance | NOT STARTED | (Stage 10-11) | Physics + ML hybrid |
| **S9** Human spaceflight and habitats | ECLSS, radiation health, habitats, logistics, human factors | NOT STARTED | (Stage 12) | Habitat resource simulation |

---

## Coverage Summary

After completing Sessions 01-30, you reach L2 (Working Competence) in:

| Spine | Modules Covered | Depth |
|-------|----------------|-------|
| Mathematics | M0, M1, M2, M3 (partial M4, M7, M9) | L2 foundation |
| Physics | P0, P1 | L2 foundation |
| Programming | C1, C2, C3 (partial C4) | L2 foundation |
| Space Systems | S1 (partial S2) | L1 literacy |

Sessions 31-104 (not yet built) extend each spine toward L3 specialization.

---

## How to Use This Tracker

1. After completing each session, check which modules it touched
2. Update the status for those modules
3. If a module shows DIAGNOSED but not IN PROGRESS, schedule repair
4. If a module shows IN PROGRESS but sessions are done, check the evidence artifact exists
5. Only mark WORKING when the delayed gate (1-week retrieval) passes
6. Only mark SPECIALIZED after a module defense (10-min explanation)
