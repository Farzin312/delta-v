//! Drill 05: Structs, Methods, Self, Derive
//!
//! Concepts: named-field structs, impl blocks, methods vs associated functions
//! Time target: under 15 minutes from a blank file
//!
//! INSTRUCTIONS:
//! From scratch, write:
//!
//! 1. A Point2 struct: struct Point2 { x: f64, y: f64 }
//!    Derive Debug, Clone, Copy, PartialEq.
//!
//! 2. Methods on Point2:
//!    fn new(x: f64, y: f64) -> Self        // associated function (constructor)
//!    fn distance_to(self, other: Self) -> f64  // method (takes self)
//!    fn origin() -> Self                    // associated function
//!
//! 3. A Vec2 struct: struct Vec2 { x: f64, y: f64 }
//!    Derive the same traits.
//!    NOTE: Vec2 and Point2 have the same fields but are DIFFERENT TYPES.
//!    It should be a compile error to pass a Point2 where Vec2 is expected.
//!
//! 4. Methods on Vec2 (intentionally different API from Point2):
//!    fn from_point(p: Point2) -> Self       // conversion
//!    fn magnitude(self) -> f64              // use hypot
//!    fn add(self, other: Self) -> Self      // vector addition
//!    fn scale(self, factor: f64) -> Self    // scalar multiplication
//!
//! 5. Tests:
//!    - Point2::new(0.0, 0.0).distance_to(Point2::new(3.0, 4.0)) == 5.0
//!    - Vec2::from_point(Point2::new(3.0, 4.0)).magnitude() == 5.0
//!    - Vec2::new(1.0, 0.0).add(Vec2::new(0.0, 1.0)) == Vec2::new(1.0, 1.0)
//!    - Vec2::new(3.0, 4.0).scale(2.0) == Vec2::new(6.0, 8.0)
//!
//! CONSTRAINTS:
//! - Use f64::hypot for magnitude, not sqrt(x*x + y*y)
//! - Point2 and Vec2 must not be interchangeable
//!
//! WHEN DONE:
//!   cargo test
//!   cargo clippy -- -D warnings
//!
//! NOTES:
//! - Date: _________  Time: _________
//! - What was smooth:
//! - What was sticky:
//! - Re-do date: _________

fn main() {
    // TODO: demonstrate Point2 and Vec2
}
