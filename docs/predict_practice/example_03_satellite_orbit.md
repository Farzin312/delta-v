# Example 3: Orbital Period of a Satellite

In this example, we will scale up to a planetary-scale problem involving circular orbits and gravity, showing how to predict values using dimensional matchmaking and orders of magnitude.

**Problem**: The International Space Station (ISS) orbits the Earth at an altitude of approximately 400 km above the surface (Earth radius is about 6,400 km). The orbital velocity is about 7,660 m/s (about 17,100 mph). Predict the time (in seconds) it takes the ISS to complete one full orbit around the Earth.

---

## Step 1: PREDICT

Write your prediction BEFORE any calculation or code. Do not use AI or calculators.

### How to reason about this:
- **Sign**: Time is positive. Sign = **Positive**.
- **Scale**: The ISS travels around the Earth.
  - Does it take 10 seconds (10^1)? No, the Earth is huge.
  - Does it take 100,000 seconds (10^5, about 28 hours)? No, low Earth orbits are fast. A typical orbit takes about 1.5 hours.
  - Let's convert 1.5 hours to seconds:

        1.5 hours ~ 90 minutes = 5,400 seconds

  - 5,400 seconds is in the thousands. Using the 3.16 rule: 5,400 > 3,160, so it rounds to the higher power: 10^4 s? Wait! Let's check:
    - 10^3 = 1,000
    - 10^4 = 10,000
    - The log midpoint between 10^3 and 10^4 is sqrt(10^7) ~ 3,162.
    - Since 5,400 is greater than 3,162, its scale is **10^4 s** (about 10,000 seconds / 2.7 hours).
- **Direction**: If the orbital altitude (radius) increases, the time to complete an orbit should **increase** (since the path length is longer). If the orbital velocity increases, the time should **decrease**.
- **Units**: Time should be in **seconds (s)**.
- **Failure case**: What breaks this?
  - Velocity is zero or negative (v <= 0, it is not moving or falling straight down).
  - Orbit radius is less than or equal to the Earth's radius (it would collide with the Earth).

### Filled Predict Block:
```
Sign:         Positive
Scale:        10^4 s (tens of thousands of seconds, ~1.5 to 3 hours)
Direction:    Increasing with orbital radius, decreasing with orbital velocity
Units:        Seconds (s)
Failure case: velocity <= 0, orbital_radius <= Earth_radius
```

---

## Step 2: EXPLAIN

Draw the physical story in 5 sentences or less. Name system boundary, coordinate frame, assumptions, inputs, and outputs.

### Physical Story:
```
                . - ~ - .
            .               .
          .    .--------.     .   <- Circular Orbit (Radius R = R_earth + h)
         .    /  Earth   \     .
        .    |  Radius R_e|=====> [ISS] (Orbital speed v)
         .    \          /     .
          .    '--------'     .
            .               .
                ' - _ - '
```
- **System boundary**: The ISS and the Earth.
- **Coordinate frame**: 2D polar coordinate system centered on the Earth.
- **Assumptions**: The orbit is a perfect circle. The orbital velocity is constant. We neglect atmospheric drag at this altitude.
- **Inputs**: Earth radius R_e = 6,400,000 m, altitude h = 400,000 m, orbital velocity v = 7,660 m/s.
- **Outputs**: Orbital period T (s).

---

## Step 3: DERIVE

Move from physical definitions to the final equation. Check dimensions and limiting cases.

### Derivation:
The total distance traveled in one full circular orbit is the circumference of the orbit circle:

    Distance = 2 * pi * R

The orbital radius R is the sum of the Earth's radius and the altitude:

    R = R_e + h

Since velocity v is constant, the orbital period T (time for one orbit) is simply distance divided by velocity:

    T = 2 * pi * (R_e + h) / v

### Dimensional Check:
Check if the dimensions on both sides balance:

    Units of T = seconds (s)

    Units of (R_e + h) / v = m / (m/s)
                           = m * (s/m)
                           = s

*The dimensions balance!*

### Limiting Cases:
- **Zero Orbit Radius (R_e + h = 0)**: T = 0. (Physically impossible, but mathematically consistent).
- **Infinite Velocity (v -> inf)**: T -> 0. If you travel infinitely fast, it takes no time to orbit. (Correct).
- **Zero Velocity (v -> 0)**: T -> inf. If you do not move, you never finish the orbit. (Correct).

---

## Step 4: IMPLEMENT

Write the smallest, pure Rust function that matches your derivation.

### Rust Code:
```rust
use std::f64::consts::PI;

/// Calculates the orbital period (in seconds) of a satellite in a circular orbit.
///
/// # Operating Domain
/// - `earth_radius_m`: Must be > 0.0
/// - `altitude_m`: Must be >= 0.0
/// - `velocity_m_s`: Must be > 0.0
pub fn orbital_period_seconds(
    earth_radius_m: f64,
    altitude_m: f64,
    velocity_m_s: f64,
) -> Result<f64, String> {
    if earth_radius_m <= 0.0 {
        return Err("Earth radius must be positive".to_string());
    }
    if altitude_m < 0.0 {
        return Err("Altitude cannot be negative".to_string());
    }
    if velocity_m_s <= 0.0 {
        return Err("Velocity must be positive and non-zero".to_string());
    }
    
    let orbit_radius = earth_radius_m + altitude_m;
    Ok((2.0 * PI * orbit_radius) / velocity_m_s)
}
```

---

## Step 5: TEST

Write automated tests verifying known values, boundaries, properties, and independent references.

### Test Implementation:
```rust
#[cfg(test)]
mod tests {
    use super::*;

    // 1. Known value test
    // R_e = 6400km, h = 400km -> R = 6800km = 6,800,000m
    // v = 7660m/s -> T = 2 * PI * 6,800,000 / 7660 = 5577.67s
    #[test]
    fn test_known_value() {
        let result = orbital_period_seconds(6_400_000.0, 400_000.0, 7660.0).unwrap();
        assert!((result - 5577.6749).abs() < 1e-2);
    }

    // 2. Boundary test
    #[test]
    fn test_boundary_zero_altitude() {
        // Orbit right at the Earth's surface (hypothetical, ignoring atmosphere)
        let result = orbital_period_seconds(6_400_000.0, 0.0, 7900.0).unwrap();
        let expected = (2.0 * PI * 6_400_000.0) / 7900.0;
        assert!((result - expected).abs() < 1e-9);
    }

    // 3. Property test (Linear scaling: doubling radius doubles period at constant velocity)
    #[test]
    fn test_linear_radius_scaling() {
        let t1 = orbital_period_seconds(6_000_000.0, 0.0, 1000.0).unwrap();
        let t2 = orbital_period_seconds(12_000_000.0, 0.0, 1000.0).unwrap();
        
        assert!((t2 - 2.0 * t1).abs() < 1e-9);
    }

    // 4. Independent Reference test (Cross-check with Kepler's Third Law)
    // T^2 = (4 * PI^2 * R^3) / (G * M)
    // For Earth, G * M = mu = 3.986e14 m^3/s^2.
    // The velocity for a circular orbit is v = sqrt(mu / R).
    // Let's verify that the period calculated matches Kepler's period.
    #[test]
    fn test_against_kepler_third_law() {
        let r = 6_800_000.0;
        let mu = 3.986004418e14; // Earth gravitational parameter
        let v = (mu / r).sqrt(); // circular orbital speed
        
        let t_circular = orbital_period_seconds(6_400_000.0, 400_000.0, v).unwrap();
        let t_kepler = (4.0 * PI * PI * r.powi(3) / mu).sqrt();
        
        assert!((t_circular - t_kepler).abs() < 1e-5);
    }
}
```

---

## Step 6: FALSIFY

Deliberately try to break your model and code, classify the failures, and declare the operating domain.

### Failures Identified:
1. **Model Limitation (Physical)**: If the altitude is below ~100 km, atmospheric drag is extremely high. The circular orbit model fails because the satellite experiences drag, spirals downward, and burns up.
2. **Model Limitation (Physical)**: If velocity exceeds escape velocity (v >= sqrt(2) * v_orbit), the satellite escapes Earth's gravity on a parabolic/hyperbolic trajectory. It is no longer in a closed orbit, and the "orbital period" ceases to exist.
3. **Model Limitation (Math)**: Velocity is 0 or negative, which yields a division by zero. The Rust code returns an `Err`.

### Declared Operating Domain:
- `earth_radius_m`: [10^5, 10^8] (planetary scale).
- `altitude_m`: [10^5, 10^9] (from low Earth orbit to beyond lunar orbit).
- `velocity_m_s`: [10^2, 10^5] (sub-orbital speeds to ultra-fast velocities).

---

## Step 7: TEACH

Summarize the loop, record surprises, and track what you learned.

- **What surprised me**: The scale of the orbital period is 10^4 s (5,577 s ~ 93 minutes). My prediction was 10^4 s, which was correct, but I initially was tempted to guess 10^3 s since 93 minutes feels "short." This shows how log midpoints (3.16) can trick our human base-10 minds.
- **What I trust**: The circular orbit period matches Kepler's Third Law exactly.
- **Where it fails**: Fails if the orbit is eccentric (elliptical orbits require Kepler's Equation to solve for position over time, as speed is not constant).

---

[<- Back to README](README.md)
