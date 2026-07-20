# Example 1: Dropping a Rock from a Cliff

In this example, we will walk through a simple classical mechanics problem step-by-step using the full 7-step Frontier Engineer loop.

**Problem**: How long does it take for a rock dropped from the top of a 20 m cliff to hit the ground? (Assume gravity g ~ 10 m/s^2).

---

## Step 1: PREDICT

Write your prediction BEFORE any calculation or code. Do not use AI or calculators.

### How to reason about this:
- **Sign**: We are predicting **time**. Time starts at 0 and goes forward. It must be **positive**.
- **Scale**: The cliff is 20 m high (about a 6-story building). If you drop a rock, it will take more than 0.1 s (10^-1), but definitely less than 10 s (10^1). It feels like a few seconds. Using the 3.16 rule, any value between 0.316 and 3.16 has a scale of 10^0. Let's guess the time is around 1 to 3 seconds. Scale = **10^0 s**.
- **Direction**: If we make the cliff taller (increase height), the rock has to travel further, so the fall time should **increase**. If we drop it on a heavier planet (increase gravity), it will pull the rock down faster, so the fall time should **decrease**.
- **Units**: Time should be in **seconds (s)**.
- **Failure case**: What breaks this?
  - Height is negative (h < 0, the rock is already underground).
  - Gravity is zero or negative (g <= 0, the rock floats forever or falls upwards).

### Filled Predict Block:
```
Sign:         Positive
Scale:        10^0 s (single-digit seconds)
Direction:    Increasing with height, decreasing with gravity
Units:        Seconds (s)
Failure case: height < 0, gravity <= 0
```

---

## Step 2: EXPLAIN

Draw the physical story in 5 sentences or less. Name system boundary, coordinate frame, assumptions, inputs, and outputs.

### Physical Story:
```
   y = 0  o (Rock dropped, v0 = 0)
          |
          |  |
          |  | positive direction (y points down)
          v  v
          |
   y = h === (Ground)
```
- **System boundary**: The rock and the Earth. We neglect air resistance (drag) for this simple model.
- **Coordinate frame**: 1D vertical axis. Let y = 0 be the top of the cliff, pointing downwards as positive.
- **Assumptions**: Gravity is constant (g = 10 m/s^2). The rock starts from rest (v0 = 0). Air resistance is neglected.
- **Inputs**: Height h = 20 m, acceleration due to gravity g = 10 m/s^2.
- **Outputs**: Time to impact t (s).

---

## Step 3: DERIVE

Move from physical definitions to the final equation. Check dimensions and limiting cases.

### Derivation:
We start with the constant acceleration kinematics equation for position:

    y(t) = y0 + v0*t + (1/2)*a*t^2

Applying our coordinate system:
- Start position y0 = 0
- Start velocity v0 = 0 (dropped from rest)
- Acceleration a = g (gravity pointing down, which is positive in our frame)
- End position y(t) = h at impact time t

Substitute these in:

    h = (1/2)*g*t^2

Now solve for time t:

    t^2 = 2h / g
    t = sqrt(2h / g)

### Dimensional Check:
Check if the dimensions on both sides balance:

    Units of t = seconds (s)

    Units of sqrt(2h / g) = sqrt( m / (m/s^2) )
                          = sqrt( m * s^2/m )
                          = sqrt( s^2 )
                          = s

*The dimensions balance!*

### Limiting Cases:
- **Zero Height (h = 0)**: t = sqrt(0) = 0. Takes no time to fall zero distance. (Correct).
- **Infinite Height (h -> inf)**: t -> inf. It falls forever. (Correct).
- **Zero Gravity (g -> 0)**: t -> inf. Without gravity pulling it down, it floats forever. (Correct).

---

## Step 4: IMPLEMENT

Write the smallest, pure Rust function that matches your derivation.

### Rust Code:
```rust
/// Calculates the time (in seconds) for an object to fall from a given height
/// under constant gravity, neglecting air resistance.
///
/// # Operating Domain
/// - `height_m`: Must be >= 0.0
/// - `gravity_m_s2`: Must be > 0.0
pub fn fall_time_seconds(height_m: f64, gravity_m_s2: f64) -> Result<f64, String> {
    if height_m < 0.0 {
        return Err("Height cannot be negative".to_string());
    }
    if gravity_m_s2 <= 0.0 {
        return Err("Gravity must be positive and non-zero".to_string());
    }
    
    Ok((2.0 * height_m / gravity_m_s2).sqrt())
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

    // 1. Known value test (Textbook hand calculation)
    // h = 20m, g = 10m/s^2 -> t = sqrt(2 * 20 / 10) = sqrt(4) = 2.0s
    #[test]
    fn test_known_value() {
        let result = fall_time_seconds(20.0, 10.0).unwrap();
        assert!((result - 2.0).abs() < 1e-9);
    }

    // 2. Boundary test (Extreme/zero cases)
    #[test]
    fn test_boundary_zero_height() {
        let result = fall_time_seconds(0.0, 9.81).unwrap();
        assert_eq!(result, 0.0);
    }

    // 3. Property test (Structural invariants like monotonicity)
    #[test]
    fn test_monotonicity() {
        // If height increases, fall time must increase
        let t1 = fall_time_seconds(10.0, 9.81).unwrap();
        let t2 = fall_time_seconds(20.0, 9.81).unwrap();
        assert!(t2 > t1);
    }

    // 4. Independent Reference test (Cross-check with velocity equation)
    // Alternate formula: t = v / g, where v = sqrt(2 * g * h)
    #[test]
    fn test_against_alternative_formula() {
        let h = 50.0;
        let g = 9.81;
        let v = (2.0 * g * h).sqrt();
        let t_ref = v / g;
        
        let t_calc = fall_time_seconds(h, g).unwrap();
        assert!((t_calc - t_ref).abs() < 1e-9);
    }
}
```

---

## Step 6: FALSIFY

Deliberately try to break your model and code, classify the failures, and declare the operating domain.

### Failures Identified:
1. **Model Limitation (Physical)**: If we drop the rock from 100,000 m (space), gravity is no longer constant (g decreases with altitude) and air resistance is highly variable. The constant gravity assumption is violated.
2. **Model Limitation (Math)**: If g = 0, our equation would divide by zero. Our Rust code catches this explicitly and returns an `Err` rather than letting the division occur and returning `infinity` or crashing.
3. **Numerical Limit (Floating point)**: If height is set to 10^300 meters, the calculation overflows the limits of `f64` and returns `infinity`.

### Declared Operating Domain:
- `height_m`: [0.0, 1000.0] (cliff heights where constant gravity holds and air resistance is minor).
- `gravity_m_s2`: [0.1, 100.0] (positive gravity values).

---

## Step 7: TEACH

Summarize the loop, record surprises, and track what you learned.

- **What surprised me**: My prediction in Step 1 was a scale of 10^0 s (between 0.316 and 3.16 seconds). The actual calculation gave 2.0 s. My physical intuition was correct!
- **What I trust**: The calculation matches the constant acceleration kinematics model exactly. I trust it for dense, heavy objects falling small distances.
- **Where it fails**: Fails for light objects (like feathers) due to drag, and fails for high altitudes where gravity changes.
- **What concept this unlocks next**: Incorporating aerodynamic drag (which will require numerical integration).

---

[<- Back to README](README.md)
