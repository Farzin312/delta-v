# Concept Map: What Each Session Teaches

This document shows the learning dependency chain. Each session builds on previous ones and unlocks the next. Use this for retention review: if you can explain each link in the chain from memory, you own the foundation.

The left column is the MATH/PHYSICS concept. The right column is the RUST/ENGINEERING concept. The arrow shows what it unlocks next.

---

## How to Read This Map

```
Session NN
  Math:     [the physical concept you learn]
  Rust:     [the programming skill you practice]
  Unlocks:  -> Session NN+1 [what becomes possible because you learned this]
```

If you get stuck on Session N, come back here and trace backward. Your blocker is usually in a prerequisite session, not the current one.

---

## Stage 1: Rust + Mathematical Language (Sessions 01-15)

### Session 01 - Make an equation executable
```
Math:     Units, multiplication, scientific notation (ms -> s, m/s * s -> m)
Rust:     cargo, bindings, f64, functions, println!, assertions
Unlocks:  -> 02 [You can write a function that computes a physical quantity.
                   Next: make it return errors instead of crashing.]
```

### Session 02 - Turn algebra into a tested function
```
Math:     Rearranging v = d/t into d = v*t and t = d/v; unit consistency
Rust:     functions with parameters and return values, #[test] attribute
Unlocks:  -> 03 [You can rearrange and test equations.
                   Next: handle invalid inputs gracefully.]
```

### Session 03 - Represent failure honestly
```
Math:     Valid domains (t > 0), inequalities as constraints
Rust:     Result<T, E>, enums, pattern matching, ? operator
Unlocks:  -> 04 [You can express "this input is invalid" in code.
                   Next: prevent invalid inputs at the type level.]
```

### Session 04 - Make units visible in types
```
Math:     Dimensional analysis as a compile-time check
Rust:     Tuple structs, impl blocks, Copy, newtype pattern
Unlocks:  -> 05 [You cannot accidentally mix Meters and Seconds.
                   Next: build a 2D vector type using the same struct patterns.]
```

### Session 05 - Own a small vector type
```
Math:     Coordinate pairs, magnitude via Pythagorean theorem (3-4-5)
Rust:     Structs with methods, references, derive(Debug, Clone, Copy)
Unlocks:  -> 06 [You can represent 2D quantities with magnitude.
                   Next: add angles and trigonometry.]
```

### Session 06 - Radians before trigonometry
```
Math:     Angles, radians vs degrees, sin/cos, unit direction vectors
Rust:     Associated functions (constants), constructors, f64::consts
Unlocks:  -> 07 [You can represent directions, not just magnitudes.
                   Next: sample how position changes over time.]
```

### Session 07 - Sample a changing state
```
Math:     Discrete samples of continuous motion, x(t) = x0 + v*t
Rust:     for loops, ranges, Vec, iterators
Unlocks:  -> 08 [You can produce a time series of positions.
                   Next: tag each sample with its coordinate frame.]
```

### Session 08 - Model context with enums
```
Math:     Coordinates require a reference frame to be meaningful
Rust:     Enums, match, exhaustive handling
Unlocks:  -> 09 [You know that numbers alone are ambiguous without context.
                   Next: work with arbitrary-length vectors via slices.]
```

### Session 09 - Compute dot products from slices
```
Math:     Projection, angle between vectors, orthogonality
Rust:     Arrays, slices, iterators, zip
Unlocks:  -> 10 [You can measure alignment between vectors.
                   Next: organize your growing codebase into a proper crate.]
```

### Session 10 - Build a maintainable crate
```
Math:     Separation of concerns (pure math vs I/O vs presentation)
Rust:     Modules, pub, lib.rs vs main.rs, rustdoc
Unlocks:  -> 11 [Your code is now reusable, not just a script.
                   Next: use it to study function behavior.]
```

### Session 11 - Treat a graph as behavior
```
Math:     Functions, slope, rising/falling, intercepts
Rust:     Closures, function parameters (fn pointers), sampling
Unlocks:  -> 12 [You can sample and visualize function behavior.
                   Next: compute the slope numerically (the derivative).]
```

### Session 12 - Approximate a derivative
```
Math:     Difference quotient, forward vs central difference, error vs step size
Rust:     Higher-order functions, numerical experiment design
Unlocks:  -> 13 [You can compute instantaneous rate of change.
                   Next: chain position -> velocity -> acceleration.]
```

### Session 13 - Connect position, velocity, acceleration
```
Math:     First derivative (velocity) and second derivative (acceleration)
Rust:     Data windows, Option, boundary handling for endpoints
Unlocks:  -> 14 [You understand that velocity is the derivative of position,
                   and acceleration is the derivative of velocity.
                   Next: go backward - integrate velocity to get distance.]
```

### Session 14 - Accumulate change
```
Math:     Riemann sums, trapezoid rule, integration as area
Rust:     windows(), iterators, numerical API design
Unlocks:  -> 15 [You can reverse the derivative (integrate).
                   Next: package the full kinematics equations into a release.]
```

### Session 15 - Release a constant-acceleration simulator
```
Math:     Full kinematic equations: x(t), v(t), v^2 = v0^2 + 2ad
Rust:     Crate boundaries, CLI, CSV output, integration tests
Unlocks:  -> 16 [Stage 1 complete for kinematics.
                   Next: extend from 2D to 3D vectors.]
```

---

## Stage 2: Calculus + Numerical Mechanics (Sessions 16-30)

### Session 16 - Graduate to Vec3
```
Math:     3D vector algebra, cross product, right-hand rule
Rust:     Operator overloading (Add, Sub via traits), normalization, robust errors
Unlocks:  -> 17 [You can work in 3 dimensions.
                   Next: use the dot product to compute physical work.]
```

### Session 17 - Use projection and work
```
Math:     Dot product as alignment, work = F.d = |F||d|cos(theta)
Rust:     Methods, semantic wrappers (Force, Displacement types)
Unlocks:  -> 18 [You can compute energy transfer via vector projection.
                   Next: rotate vectors using matrices.]
```

### Session 18 - Rotate coordinates
```
Math:     2D rotation matrices, length preservation, inverse rotation
Rust:     Fixed arrays [[f64; 2]; 2], matrix-vector multiplication
Unlocks:  -> 19 [You can transform coordinate frames.
                   Next: chain multiple transformations.]
```

### Session 19 - Compose transformations
```
Math:     Matrix multiplication is order-dependent (rotation then translate
          is NOT the same as translate then rotate)
Rust:     Matrix composition, API design decisions
Unlocks:  -> 20 [You understand that transformation order matters.
                   Next: confront the limits of floating-point representation.]
```

### Session 20 - Be honest about floating point
```
Math:     IEEE 754 representation, absolute vs relative error, cancellation
Rust:     f64::EPSILON, approximate comparison functions
Unlocks:  -> 21 [You know why 0.1 + 0.2 != 0.3 and how to compare safely.
                   Next: apply physics (Newton's laws) using safe numerics.]
```

### Session 21 - Translate a free-body diagram
```
Math:     F = ma, force diagrams, acceleration from net force
Rust:     Data modeling, pure dynamics functions
Unlocks:  -> 22 [You can simulate motion under force.
                   Next: add the most important force in space - gravity.]
```

### Session 22 - Implement inverse-square gravity
```
Math:     Universal gravitation, a = mu/r^2, vector form a_vec = -(mu/r^3)*r_vec
Rust:     Vector normalization, physical constants, singularity handling
Unlocks:  -> 23 [You can compute gravitational acceleration anywhere.
                   Next: use energy conservation to validate orbits.]
```

### Session 23 - Use conservation as an oracle
```
Math:     KE = 0.5*m*v^2, PE = -mu*m/r, specific orbital energy, v_circ = sqrt(mu/r)
Rust:     Diagnostic functions, invariant checking
Unlocks:  -> 24 [You can check if an orbit is valid using energy.
                   Next: connect force over time (impulse) to velocity change.]
```

### Session 24 - Connect impulse and momentum
```
Math:     Impulse J = F*dt, momentum p = m*v, delta-v = J/m
Rust:     State updates, sign conventions (thrust vs drag)
Unlocks:  -> 25 [You can model maneuvers (delta-v).
                   Next: write the derivative function for an ODE.]
```

### Session 25 - Write a state derivative
```
Math:     ODE state-space form: y=[x,v], y'=[v,a]. Spring: a = -k*x/m
Rust:     Structs for state, traits for derivative APIs
Unlocks:  -> 26 [You can express continuous dynamics as a derivative function.
                   Next: step that function forward in time (integrate).]
```

### Session 26 - Take the first numerical step
```
Math:     Forward Euler: y_next = y + h*f(t,y). First-order accuracy.
Rust:     Immutable state updates, step functions
Unlocks:  -> 27 [You can propagate a system forward in time.
                   Next: improve accuracy with the midpoint method.]
```

### Session 27 - Implement midpoint before RK4
```
Math:     Midpoint (RK2): evaluate derivative at the midpoint. Second-order.
Rust:     Function composition, intermediate state computation
Unlocks:  -> 28 [You have a more accurate integrator than Euler.
                   Next: prove the accuracy improvement with a convergence study.]
```

### Session 28 - Run a convergence study
```
Math:     Global error, observed order of accuracy p = log(E1/E2)/log(h1/h2)
Rust:     Experiment harnesses, CSV output, log-log analysis
Unlocks:  -> 29 [You can prove your integrator converges at the right rate.
                   Next: test structural properties, not just examples.]
```

### Session 29 - Test properties, not only examples
```
Math:     Inverse-square scaling, direction-to-origin, energy conservation
Rust:     Property testing concepts (proptest), randomized test cases
Unlocks:  -> 30 [You can test physics invariants across a range of inputs.
                   Next: package everything into a shippable release.]
```

### Session 30 - Ship a verified mechanics vertical slice
```
Math:     Full loop: model + numerics + evidence
Rust:     Workspace design, CI, documentation, ADRs, release
Unlocks:  -> Stage 3 (Orbital Mechanics Core, Sessions 17-24 of curriculum)
```

---

## Dependency Chains (Quick Reference)

If you are stuck on a concept, trace the chain backward to find the gap:

**Integration chain:**
```
11 (functions/sampling) -> 12 (derivative) -> 13 (position/velocity/accel)
  -> 14 (integration) -> 25 (ODE state) -> 26 (Euler) -> 27 (midpoint)
  -> 28 (convergence)
```

**Vector chain:**
```
05 (Vec2) -> 09 (dot product) -> 16 (Vec3 + cross) -> 17 (work/projection)
  -> 18 (rotation) -> 19 (composition) -> 22 (gravity vector)
```

**Error handling chain:**
```
02 (functions) -> 03 (Result/Err) -> 04 (type-level units)
  -> 20 (float tolerance) -> 29 (property tests)
```

**Physics chain:**
```
15 (kinematics) -> 21 (F=ma) -> 22 (gravity) -> 23 (energy)
  -> 24 (impulse/delta-v) -> 25 (ODE) -> 30 (full simulator)
```

---

## Mastery Checkpoints

After completing these groups, you should be able to:

**After Sessions 01-08 (Foundations):**
- Write, test, and error-handle a Rust function from a physics equation
- Explain dimensional analysis and why units matter
- Work with vectors, angles, and coordinate frames

**After Sessions 09-15 (Algebra to Calculus):**
- Organize code into a library + CLI
- Compute derivatives and integrals numerically
- Build and release a kinematics simulator

**After Sessions 16-20 (Linear Algebra + Floats):**
- Do full 3D vector algebra (dot, cross, magnitude, normalize)
- Apply rotations and compose transformations
- Compare floats safely and explain IEEE 754 pitfalls

**After Sessions 21-30 (Mechanics + Numerics):**
- Compute gravitational forces and orbital energy
- Write ODEs in state-space form and integrate them
- Prove convergence rate and test physics invariants
- Ship a documented, tested, reproducible release

---

[<- Back to INDEX](INDEX.md)
