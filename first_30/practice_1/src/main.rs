//! Practice 1: Make an equation executable
//!
//! Session 01 of the Frontier Engineer Field Manual.
//! The very first step: turn a physics equation into running, tested Rust.
//!
//! TODO: Implement kinematic equations and a minimal 2D vector type.
//! Every function below has a doc comment describing what it should do.
//! Replace `todo!()` with your implementation, then make the tests pass.

fn main() {
    // TODO: Implement your demo here once the functions below are working.
    //
    // Suggested output format:
    //   Print kinematic results for a ball thrown upward at 10 m/s
    //   under gravity (-9.81 m/s^2) at t = 2.0 s.
    //
    //   Then demonstrate Vec2: create (3, 4) and (1, 0),
    //   print magnitude and dot product.
    //
    // Un-comment the lines below and fill in your function calls:
    //
    // println!("=== Practice 1: Make an Equation Executable ===\n");
    // println!("[Kinematics]");
    // ...
    // println!("\n[Vectors]");
    // ...
    println!("Implement the functions below, then fill in main().");
}

// ---------- Kinematics ----------
// Physical model: constant-acceleration motion.
//
//   x(t) = x0 + v0*t + 0.5*a*t^2   (position)
//   v(t) = v0 + a*t                 (velocity)

/// Position under constant acceleration: x(t) = x0 + v0*t + 0.5*a*t^2
///
/// Parameters:
///   x0 - initial position (m)
///   v0 - initial velocity (m/s)
///   a  - constant acceleration (m/s^2)
///   t  - time elapsed (s)
fn position_at_time(x0: f64, v0: f64, a: f64, t: f64) -> f64 {
    todo!("Implement: x0 + v0*t + 0.5*a*t^2")
}

/// Velocity under constant acceleration: v(t) = v0 + a*t
fn velocity_at_time(v0: f64, a: f64, t: f64) -> f64 {
    todo!("Implement: v0 + a*t")
}

// ---------- Vectors ----------
// A minimal 2D vector to practice struct definition, methods, and ownership.
//
// TODO: Define a struct called Vec2 with two f64 fields (x and y).
// Then implement:
//   - new(x, y) constructor
//   - magnitude(&self) -> f64     (sqrt(x^2 + y^2))
//   - dot(&self, &Vec2) -> f64     (x1*x2 + y1*y2)
//
// Hint: derive Debug, Clone, Copy, PartialEq for easy testing.

// struct Vec2 { ... }
//
// impl Vec2 {
//     fn new(x: f64, y: f64) -> Self { ... }
//     fn magnitude(&self) -> f64 { ... }
//     fn dot(&self, other: &Vec2) -> f64 { ... }
// }

// ---------- Tests ----------
// These tests describe the expected behavior.
// Uncomment them after you implement the functions and struct above.
// All tests must pass before this session is complete.

#[cfg(test)]
mod tests {
    // use super::*;

    // #[test]
    // fn test_position_rest() {
    //     Object at rest at origin with no acceleration stays at origin.
    //     assert_eq!(position_at_time(0.0, 0.0, 0.0, 5.0), 0.0);
    // }

    // #[test]
    // fn test_position_constant_velocity() {
    //     No acceleration: position = x0 + v0*t
    //     assert!((position_at_time(0.0, 10.0, 0.0, 3.0) - 30.0).abs() < 1e-12);
    // }

    // #[test]
    // fn test_velocity_linear() {
    //     v = v0 + a*t
    //     assert!((velocity_at_time(10.0, -9.81, 2.0) - (10.0 - 19.62)).abs() < 1e-12);
    // }

    // #[test]
    // fn test_vec2_magnitude() {
    //     Classic 3-4-5 triangle
    //     let v = Vec2::new(3.0, 4.0);
    //     assert!((v.magnitude() - 5.0).abs() < 1e-12);
    // }

    // #[test]
    // fn test_vec2_dot_orthogonal() {
    //     Perpendicular vectors have zero dot product.
    //     let v = Vec2::new(1.0, 0.0);
    //     let w = Vec2::new(0.0, 1.0);
    //     assert!(v.dot(&w).abs() < 1e-12);
    // }

    // #[test]
    // fn test_vec2_dot_known() {
    //     let v = Vec2::new(3.0, 4.0);
    //     let w = Vec2::new(1.0, 2.0);
    //     3*1 + 4*2 = 11
    //     assert!((v.dot(&w) - 11.0).abs() < 1e-12);
    // }
}
