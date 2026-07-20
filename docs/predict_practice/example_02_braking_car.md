# Example 2: Stopping Distance of a Braking Car

In this example, we will walk through a kinematics problem involving deceleration and show how the stopping distance scales with the initial velocity.

**Problem**: A car is driving on a highway at 30 m/s (about 67 mph). The driver slams on the brakes, causing a constant deceleration of 5 m/s^2. Predict the distance the car travels before coming to a complete stop.

---

## Step 1: PREDICT

Write your prediction BEFORE any calculation or code. Do not use AI or calculators.

### How to reason about this:
- **Sign**: We are predicting **distance**. The car moves forward as it brakes. The distance must be **positive**.
- **Scale**: How far does a highway car take to stop? 
  - 1 meter (10^0)? No, way too short.
  - 10 meters (10^1)? A car length is about 4.5 m. Highway stops take much longer than 2 car lengths.
  - 1000 meters (10^3)? No, that is a whole kilometer. A highway car does not take a kilometer to stop under hard braking.
  - Therefore, it must be on the scale of a few dozen or a hundred meters. Let's guess around 50 to 150 meters. Using the 3.16 rule, any value between 31.6 and 316 has a scale of 10^2. Scale = **10^2 m**.
- **Direction**: If initial speed increases, stopping distance **increases**. If deceleration rate increases (braking harder), stopping distance **decreases**.
- **Units**: Distance should be in **meters (m)**.
- **Failure case**: What breaks this?
  - Initial speed is negative (v_i < 0, backing up).
  - Deceleration is zero or negative (a <= 0, the car never stops or actually speeds up).

### Filled Predict Block:
```
Sign:         Positive
Scale:        10^2 m (hundreds of meters)
Direction:    Increasing with initial speed, decreasing with deceleration rate
Units:        Meters (m)
Failure case: initial_speed < 0, deceleration <= 0
```

---

## Step 2: EXPLAIN

Draw the physical story in 5 sentences or less. Name system boundary, coordinate frame, assumptions, inputs, and outputs.

### Physical Story:
```
  x = 0                          x = d
  [Car] ===> (v = 30 m/s)        [Car] (v = 0)
  ===========================================
  <--- Deceleration (a = -5 m/s2)
```
- **System boundary**: The car, its tires, and the road surface. We represent the car as a point mass.
- **Coordinate frame**: 1D horizontal axis. Let x = 0 be the point where the driver hits the brakes, pointing in the direction of travel as positive.
- **Assumptions**: Deceleration is constant (a = -5 m/s^2). The car stops completely (v_f = 0). No reaction time delay is modeled.
- **Inputs**: Initial speed v_i = 30 m/s, deceleration rate a_brake = 5 m/s^2.
- **Outputs**: Stopping distance d (m).

---

## Step 3: DERIVE

Move from physical definitions to the final equation. Check dimensions and limiting cases.

### Derivation:
We start with the constant acceleration equation relating velocities, acceleration, and displacement:

    v_f^2 = v_i^2 + 2*a*d

Apply our coordinate system and boundary values:
- Final velocity v_f = 0 (complete stop)
- Acceleration a = -a_brake (acting opposite to the positive direction of travel)
- Displacement d

Substitute these in:

    0 = v_i^2 - 2*a_brake*d

Solve for stopping distance d:

    2*a_brake*d = v_i^2
    d = v_i^2 / (2*a_brake)

### Dimensional Check:
Check if the dimensions on both sides balance:

    Units of d = meters (m)

    Units of v_i^2 / a_brake = (m/s)^2 / (m/s^2)
                              = (m^2/s^2) / (m/s^2)
                              = m^2/s^2 * s^2/m
                              = m

*The dimensions balance!*

### Limiting Cases:
- **Zero Initial Speed (v_i = 0)**: d = 0. If the car is already stopped, stopping distance is zero. (Correct).
- **Infinite Initial Speed (v_i -> inf)**: d -> inf. (Correct).
- **Zero Deceleration (a_brake -> 0)**: d -> inf. If the brakes do not work, the car never stops. (Correct).

---

## Step 4: IMPLEMENT

Write the smallest, pure Rust function that matches your derivation.

### Rust Code:
```rust
/// Calculates the stopping distance (in meters) of a braking car.
///
/// # Operating Domain
/// - `initial_speed_m_s`: Must be >= 0.0
/// - `deceleration_m_s2`: Must be > 0.0
pub fn stopping_distance_meters(initial_speed_m_s: f64, deceleration_m_s2: f64) -> Result<f64, String> {
    if initial_speed_m_s < 0.0 {
        return Err("Initial speed cannot be negative".to_string());
    }
    if deceleration_m_s2 <= 0.0 {
        return Err("Deceleration must be positive and non-zero".to_string());
    }
    
    Ok((initial_speed_m_s * initial_speed_m_s) / (2.0 * deceleration_m_s2))
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
    // v_i = 30m/s, a = 5m/s^2 -> d = 30^2 / (2 * 5) = 900 / 10 = 90.0m
    #[test]
    fn test_known_value() {
        let result = stopping_distance_meters(30.0, 5.0).unwrap();
        assert!((result - 90.0).abs() < 1e-9);
    }

    // 2. Boundary test
    #[test]
    fn test_boundary_zero_speed() {
        let result = stopping_distance_meters(0.0, 5.0).unwrap();
        assert_eq!(result, 0.0);
    }

    // 3. Property test (Quadratic scaling: double speed -> quadruple distance)
    #[test]
    fn test_quadratic_scaling() {
        let d_10 = stopping_distance_meters(10.0, 5.0).unwrap();
        let d_20 = stopping_distance_meters(20.0, 5.0).unwrap();
        
        // Double the speed should result in 4x the stopping distance
        assert!((d_20 - 4.0 * d_10).abs() < 1e-9);
    }

    // 4. Independent Reference test (Cross-check with time-based integration)
    // Alternate formula: d = v_i * t + 0.5 * a * t^2, where t = v_i / a_brake
    #[test]
    fn test_against_time_based_calculation() {
        let vi = 30.0;
        let a = 5.0;
        let t = vi / a;
        let d_ref = vi * t - 0.5 * a * t * t;
        
        let d_calc = stopping_distance_meters(vi, a).unwrap();
        assert!((d_calc - d_ref).abs() < 1e-9);
    }
}
```

---

## Step 6: FALSIFY

Deliberately try to break your model and code, classify the failures, and declare the operating domain.

### Failures Identified:
1. **Model Limitation (Physical)**: At speeds near the speed of light, classical physics breaks down and relativistic effects must be considered.
2. **Model Limitation (Physical)**: If the road friction limit is exceeded, the deceleration rate is limited by friction (mu * g). If the brakes are slammed harder, the tires skid but deceleration cannot exceed this limit.
3. **Model Limitation (Math)**: Deceleration a = 0 divides by zero. The code catches this and returns an `Err`.

### Declared Operating Domain:
- `initial_speed_m_s`: [0.0, 100.0] (speeds up to 360 km/h, realistic for terrestrial vehicles).
- `deceleration_m_s2`: [0.1, 20.0] (firm braking to extreme race car deceleration).

---

## Step 7: TEACH

Summarize the loop, record surprises, and track what you learned.

- **What surprised me**: The stopping distance scales with the *square* of the velocity (v^2). This means driving at 60 m/s (double speed) requires 4 times the distance to stop, not 2 times. This is why highway speeding is so dangerous.
- **What I trust**: The derivation is standard physics. The quadratic property test confirms the implementation is mathematically correct.
- **Where it fails**: Fails if braking forces fade (like brake pad overheating) or if road conditions change (wet/icy roads reduce mu and thus reduce deceleration).

---

[<- Back to README](README.md)
