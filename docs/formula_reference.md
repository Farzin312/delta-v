# Formula Reference

Every equation in the first 30 sessions, organized by topic. Use this as your single-stop lookup. Each entry shows the formula, what it means, units, which sessions use it, and where it breaks.

All formulas use plain text (no LaTeX). Notation: `*` = multiply, `^` = power, `sqrt()` = square root, `pi` = 3.14159...

---

## Table of Contents

1. [Units and Constants](#1-units-and-constants)
2. [Algebra and Notation](#2-algebra-and-notation)
3. [Trigonometry](#3-trigonometry)
4. [Vectors](#4-vectors)
5. [Calculus](#5-calculus)
6. [Kinematics](#6-kinematics)
7. [Forces, Work, Energy, Momentum](#7-forces-work-energy-momentum)
8. [Gravitation and Orbits](#8-gravitation-and-orbits)
9. [Numerical Methods](#9-numerical-methods)
10. [Floating Point](#10-floating-point)

---

## 1. Units and Constants

### Base SI Units

| Quantity | Unit | Symbol | Sessions |
|----------|------|--------|----------|
| Distance | meter | m | 01, 02, 07, 15, ... |
| Time | second | s | 01, 02, 07, 15, ... |
| Velocity | m/s | -- | 02, 07, 13, 15, ... |
| Acceleration | m/s^2 | -- | 13, 15, 21, 25, ... |
| Force | Newton (N) | N | 17, 21, 24 |
| Mass | kilogram | kg | 21, 24, 25 |
| Energy | Joule (J) | J | 17, 23 |
| Angle | radian | rad | 06 |

### Key Constants

```
g (Earth surface gravity)  = 9.81 m/s^2   (approx 10 for estimation)
G (gravitational constant) = 6.674e-11 m^3 kg^-1 s^-2
mu (Earth GM)              = 398600.4418 km^3/s^2   = 3.986e14 m^3/s^2
R_earth                    = 6371 km   (mean radius)
c (speed of light)         = 299,792,458 m/s   (~3e8 m/s)
pi                         = 3.14159265...
```

### Session 01: Unit Conversion

**Distance from speed and time**
```
Formula:  d = v * t
Units:    m = (m/s) * s  ->  OK
Used in:  Session 01, 02, 07
Limit:    Requires constant velocity. No acceleration.
```

**Scientific notation**
```
12.5 ms = 12.5e-3 s = 0.0125 s
299,792,458 m/s = 2.99792458e8 m/s
```

---

## 2. Algebra and Notation

### Session 02: Rearranging equations

**Average speed**
```
Formula:  v = d / t      (also rearranged:  d = v * t,  t = d / v)
Where:    v = speed (m/s), d = distance (m), t = time (s)
Units:    (m/s) = m / s  ->  OK
Used in:  Session 02
Limit:    t = 0 is division by zero (handled via Result in Session 03).
```

### Session 03: Valid domains

```
Valid domain:  t > 0   (time must be strictly positive)
If t <= 0, the function must return Err, not silently return 0 or infinity.
```

### Session 04: Dimensional analysis via types

```
Meters(f64)        and Seconds(f64)  are distinct types.
MetersPerSecond    = Meters / Seconds
The type system prevents passing Seconds where Meters is expected.
```

### Scientific notation (powers of 10)

```
10^0  = 1
10^1  = 10
10^3  = 1,000      (kilo)
10^6  = 1,000,000  (mega)
10^-3 = 0.001      (milli)
10^-6 = 0.000001   (micro)

3.16 rule: sqrt(10) ~ 3.16 is the log-scale midpoint.
```

---

## 3. Trigonometry

### Session 06: Radians and unit vectors

**Degree to radian conversion**
```
Formula:  rad = deg * (pi / 180)
Where:    rad = angle in radians, deg = angle in degrees
Units:    dimensionless -> dimensionless. OK.
Used in:  Session 06, 17
Example:  30 deg = 30 * (pi/180) = pi/6 rad ~ 0.5236 rad
```

**Unit direction vector from angle**
```
Formula:  u = (cos(rad), sin(rad))
Where:    rad = angle in radians from x-axis
          u is a unit vector (|u| = 1)
Units:    dimensionless
Used in:  Session 06
```

---

## 4. Vectors

### Session 05: Vec2

**Magnitude**
```
Formula:  |v| = sqrt(v.x^2 + v.y^2)
Units:    same as v components (e.g., meters)
Used in:  Session 05, 16
Example:  v = (3, 4) -> |v| = sqrt(9+16) = sqrt(25) = 5
```

**Addition**
```
Formula:  a + b = (a.x + b.x, a.y + b.y)
Units:    same as components
Used in:  Session 05
```

### Session 09, 16: Dot product

**Dot product (2D and 3D)**
```
Formula:  a . b = a.x*b.x + a.y*b.y + a.z*b.z
Where:    a, b are vectors of equal dimension
Units:    product of component units (e.g., m*m = m^2)
Used in:  Session 09, 16, 17
Properties:
  - a . b = |a| * |b| * cos(theta)   (theta = angle between them)
  - a . a = |a|^2
  - If a . b = 0, vectors are orthogonal (perpendicular)
Limit:    Vectors must be same dimension (rejected at runtime in Session 09).
```

### Session 16: Cross product

**Cross product (3D)**
```
Formula:  a x b = (a.y*b.z - a.z*b.y,
                   a.z*b.x - a.x*b.z,
                   a.x*b.y - a.y*b.x)
Units:    product of component units (e.g., m*m = m^2)
Used in:  Session 16
Properties:
  - |a x b| = |a| * |b| * sin(theta)
  - Direction: perpendicular to both a and b (right-hand rule)
  - x_hat x y_hat = z_hat
  - a x a = 0 (zero vector)
```

### Session 16: Norm and normalize

```
Norm:        |v| = sqrt(v.x^2 + v.y^2 + v.z^2)
Normalize:   v_hat = v / |v|    (gives a unit vector)
Limit:       |v| = 0 -> division by zero (return Err).
```

---

## 5. Calculus

### Session 12: Numerical derivative

**Forward difference**
```
Formula:  f'(x) ~ ( f(x+h) - f(x) ) / h
Error:    O(h) - first order accurate
Used in:  Session 12
Limit:    h too large -> inaccurate. h too small -> floating point cancellation.
```

**Central difference**
```
Formula:  f'(x) ~ ( f(x+h) - f(x-h) ) / (2*h)
Error:    O(h^2) - second order accurate (much better than forward)
Used in:  Session 12, 13
Example:  d/dt(t^2) at t=3: true derivative = 2*3 = 6.
          Central diff with h=0.1: (3.1^2 - 2.9^2) / 0.2 = (9.61 - 8.41) / 0.2 = 6.0
```

### Session 14: Trapezoid integration

**Trapezoid rule**
```
Formula:  integral f(t) dt ~ sum of 0.5 * (f[i] + f[i+1]) * dt
Where:    dt is the spacing between samples
          f[i], f[i+1] are consecutive function values
Units:    [f] * [t]  (e.g., m/s * s = m for integrating velocity)
Used in:  Session 14
Example:  integral v(t)=2t from 0 to 3 with dt=1:
          samples: v(0)=0, v(1)=2, v(2)=4, v(3)=6
          trapezoids: 0.5*(0+2)*1 + 0.5*(2+4)*1 + 0.5*(4+6)*1
                    = 1 + 3 + 5 = 9
          Exact: integral 2t dt = t^2 |0..3 = 9. Matches.
Limit:    Accuracy improves as dt decreases. Trapezoid is O(dt^2).
```

---

## 6. Kinematics

### Session 15: Constant acceleration equations

**Position under constant acceleration**
```
Formula:  x(t) = x0 + v0*t + (1/2)*a*t^2
Where:    x0 = initial position (m)
          v0 = initial velocity (m/s)
          a  = constant acceleration (m/s^2)
          t  = time (s)
Units:    m = m + (m/s)*s + (m/s^2)*s^2 = m + m + m. OK.
Used in:  Session 13, 15
Limit:    Only valid when a is truly constant. Variable a requires integration.
```

**Velocity under constant acceleration**
```
Formula:  v(t) = v0 + a*t
Units:    m/s = m/s + (m/s^2)*s = m/s + m/s. OK.
Used in:  Session 13, 15
```

**Velocity-displacement (no time)**
```
Formula:  v_f^2 = v0^2 + 2*a*d
Where:    d = displacement
Used in:  Session 15, predict_practice Example 2
Derived:  Eliminate t from position and velocity equations.
Limit:    Only for constant a.
```

**Fall time from height (predict_practice Example 1)**
```
Formula:  t = sqrt(2h / g)
Where:    h = height (m), g = gravity (m/s^2)
Used in:  predict_practice Example 1
```

**Stopping distance (predict_practice Example 2)**
```
Formula:  d = v_i^2 / (2 * a_brake)
Where:    v_i = initial speed, a_brake = deceleration magnitude
Used in:  predict_practice Example 2
```

---

## 7. Forces, Work, Energy, Momentum

### Session 17: Work (dot product application)

**Work done by a force**
```
Formula:  W = F . d = |F| * |d| * cos(theta)
Where:    F = force vector (N), d = displacement vector (m)
          theta = angle between force and displacement
Units:    N * m = Joule (J)
Used in:  Session 17
Example:  F=10 N at 60 deg to d=5 m:
          W = 10 * 5 * cos(60 deg) = 10 * 5 * 0.5 = 25 J
Limit:    Force perpendicular to motion (theta=90) does zero work.
```

### Session 21: Newton's Second Law

**Force = mass * acceleration**
```
Formula:  F = m * a
Units:    N = kg * m/s^2. OK.
Rearranged:  a = F / m
Used in:  Session 21
Example:  750 kg spacecraft, 3 N thrust:
          a = 3 / 750 = 0.004 m/s^2
Limit:    Valid for non-relativistic speeds (v << c).
```

**Velocity update under constant thrust**
```
Formula:  v(t) = v0 + (F/m)*t
Used in:  Session 21
Example:  v0=0, F=3N, m=750kg, t=20s:
          v = 0 + (3/750)*20 = 0.08 m/s
```

### Session 23: Energy conservation

**Kinetic energy**
```
Formula:  KE = (1/2) * m * v^2
Units:    J = kg * (m/s)^2 = kg*m^2/s^2. OK.
Used in:  Session 23
```

**Gravitational potential energy**
```
Formula:  PE = -G*M*m / r
Where:    G = gravitational constant, M = central body mass,
          m = object mass, r = distance from center
Units:    J = (m^3 kg^-1 s^-2) * kg * kg / m = kg*m^2/s^2. OK.
Used in:  Session 23
Note:     PE is negative (zero at infinity, negative closer to body).
```

**Specific orbital energy**
```
Formula:  epsilon = v^2/2 - mu/r
Where:    mu = G*M (gravitational parameter)
          v = velocity, r = orbital radius
Units:    (m/s)^2 - m^3/s^2/m = m^2/s^2. OK. (J/kg)
Used in:  Session 23
Values:   epsilon < 0  ->  bound orbit (ellipse/circle)
          epsilon = 0  ->  parabolic (escape)
          epsilon > 0  ->  hyperbolic (escape)
```

**Circular orbital speed**
```
Formula:  v_circ = sqrt(mu / r)
Units:    sqrt( (m^3/s^2) / m ) = sqrt(m^2/s^2) = m/s. OK.
Used in:  Session 23, 29
Limit:    Only valid for circular orbits. r=0 is singular.
```

### Session 24: Impulse and momentum

**Impulse**
```
Formula:  J = F * dt
Where:    F = force (N), dt = duration (s)
Units:    N * s = kg*m/s. OK.
Used in:  Session 24
```

**Impulse-momentum theorem**
```
Formula:  J = m * delta-v
Rearranged:  delta-v = F * dt / m
Used in:  Session 24
Example:  200 N thruster, 20 s, 1000 kg spacecraft:
          delta-v = 200 * 20 / 1000 = 4.0 m/s
```

---

## 8. Gravitation and Orbits

### Session 22: Inverse-square gravity

**Gravitational acceleration magnitude**
```
Formula:  a = mu / r^2
Where:    mu = gravitational parameter (m^3/s^2)
          r  = distance from center of body (m)
Units:    (m^3/s^2) / m^2 = m/s^2. OK.
Used in:  Session 22, 29
Example:  r = 7000 km = 7e6 m, mu = 3.986e14:
          a = 3.986e14 / (7e6)^2 = 3.986e14 / 4.9e13 ~ 8.13 m/s^2
Limit:    r = 0 is a singularity (infinite acceleration).
```

**Gravitational acceleration vector**
```
Formula:  a_vec = -(mu / r^3) * r_vec
Where:    r_vec = position vector from body center
          r = |r_vec|
          Direction: toward the center of the body (negative sign)
Used in:  Session 22
Limit:    r = 0 singular. Near other massive bodies, third-body perturbations apply.
```

### Orbital period (predict_practice Example 3)

```
Formula:  T = 2*pi*R / v
Where:    R = orbital radius (R_earth + h), v = orbital velocity
Used in:  predict_practice Example 3
```

### Kepler's Third Law (cross-check reference)

```
Formula:  T^2 = 4*pi^2 * R^3 / mu
Used in:  predict_practice Example 3 (independent reference test)
```

---

## 9. Numerical Methods

### Session 25: ODE state-space form

**First-order ODE system**
```
State:    y = [x, v]   (position and velocity)
Deriv:    y' = [v, a]   (velocity and acceleration)
Used in:  Session 25
Example:  Spring system:  a = -k*x/m
          y = [x, v],  y' = [v, -k*x/m]
```

### Session 26: Euler integration

**Forward Euler step**
```
Formula:  y_next = y + h * f(t, y)
Where:    y = current state, h = step size, f = derivative function
Error:    O(h) per step, O(h) global (first order)
Used in:  Session 26
Limit:    Energy grows unboundedly for oscillatory systems.
          Not suitable for long-duration orbital propagation.
```

### Session 27: Midpoint method

**Midpoint (RK2) step**
```
Formula:  k1 = f(t, y)
          k2 = f(t + h/2, y + h/2 * k1)
          y_next = y + h * k2
Error:    O(h^2) per step, O(h^2) global (second order)
Used in:  Session 27
Advantage: Much better energy conservation than Euler for same step size.
```

### Session 28: Convergence study

**Observed order of accuracy**
```
Formula:  p = log(E1 / E2) / log(h1 / h2)
Where:    E1, E2 = errors at step sizes h1, h2
          p should match the theoretical order (1 for Euler, 2 for midpoint)
Used in:  Session 28
Example:  Euler: p ~ 1. Midpoint: p ~ 2. RK4: p ~ 4.
```

### Session 29: Structural property tests

**Inverse-square scaling test**
```
Property: a(r1) / a(r2) = (r2 / r1)^2
Used in:  Session 29
Example:  a(7000) / a(14000) = (14000/7000)^2 = 4
          Gravity at 7000 km should be 4x stronger than at 14000 km.
```

**Direction test**
```
Property: dot(a_vec, r_vec) < 0
          Acceleration vector always points toward origin (opposite to r).
Used in:  Session 29
```

---

## 10. Floating Point

### Session 20: Comparing floats

**Absolute tolerance**
```
Formula:  |a - b| < eps_abs
Used in:  Session 20
Limit:    Fails for very large numbers where eps_abs is relatively tiny.
```

**Relative tolerance**
```
Formula:  |a - b| / max(|a|, |b|) < eps_rel
Used in:  Session 20
Limit:    Fails when both a and b are near zero.
```

**Combined tolerance (recommended)**
```
Formula:  |a - b| <= eps_abs + eps_rel * max(|a|, |b|)
Used in:  Session 20
Where:    eps_abs ~ 1e-9, eps_rel ~ 1e-9 (typical for f64)
Handles both near-zero and large values.
```

**Machine epsilon (f64)**
```
f64::EPSILON = 2.220446049250313e-16
This is the smallest value where 1.0 + EPS != 1.0
```

**Why 0.1 + 0.2 != 0.3**
```
0.1 in binary is a repeating fraction (like 1/3 in decimal).
0.1_f64 + 0.2_f64 = 0.30000000000000004
This is why exact equality on floats is always wrong.
Always use tolerance-based comparison.
```

---

## Quick Lookup: Formula by Session

| Session | Key Formula | Concept |
|:-------:|-------------|---------|
| 01 | d = v * t | Distance from speed and time |
| 02 | v = d / t | Rearranging algebra |
| 03 | t > 0 (Result type) | Valid domains and errors |
| 04 | Meters / Seconds types | Dimensional analysis via types |
| 05 | |v| = sqrt(x^2 + y^2) | Vec2 magnitude |
| 06 | rad = deg * pi/180 | Radian conversion |
| 07 | x(t) = x0 + v*t | Sampling continuous motion |
| 08 | Frame tags (Inertial, EarthFixed) | Coordinate frames |
| 09 | a.b = sum(a[i]*b[i]) | Dot product |
| 10 | (library structure) | Crate organization |
| 11 | f(t) = 2t^2 - 3t + 1 | Functions, slopes |
| 12 | f'(x) ~ (f(x+h)-f(x-h))/(2h) | Numerical derivative |
| 13 | v ~ dx/dt, a ~ dv/dt | Position -> velocity -> acceleration |
| 14 | integral ~ trapezoid sum | Numerical integration |
| 15 | x = x0 + v0*t + 0.5*a*t^2 | Kinematic equations |
| 16 | a x b = cross product | Vec3 operations |
| 17 | W = F.d = |F||d|cos(theta) | Work as dot product |
| 18 | R(theta) rotation matrix | 2D rotation |
| 19 | T_composed = T2 * T1 | Matrix composition |
| 20 | |a-b| <= eps_abs + eps_rel*max(|a|,|b|) | Float comparison |
| 21 | F = m*a, a = F/m | Newton's second law |
| 22 | a = mu/r^2, a_vec = -(mu/r^3)*r_vec | Inverse-square gravity |
| 23 | epsilon = v^2/2 - mu/r, v_circ = sqrt(mu/r) | Orbital energy |
| 24 | delta-v = F*dt/m | Impulse and momentum |
| 25 | y=[x,v], y'=[v,a] | ODE state-space |
| 26 | y_next = y + h*f(t,y) | Euler integration |
| 27 | y_next = y + h*f(t+h/2, y+h/2*k1) | Midpoint method |
| 28 | p = log(E1/E2)/log(h1/h2) | Convergence order |
| 29 | a(r1)/a(r2) = (r2/r1)^2 | Property tests (scaling) |
| 30 | (full system) | Vertical slice release |

---

[<- Back to INDEX](INDEX.md)
