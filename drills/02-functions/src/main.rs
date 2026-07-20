//! Drill 02: Functions, Parameters, Return Values
//!
//! Concepts: function signatures, expressions vs statements, unit tests
//! Time target: under 10 minutes from a blank file
//!
//! INSTRUCTIONS:
//! From scratch, write:
//!
//! 1. fn double(x: f64) -> f64
//! 2. fn halve(x: f64) -> f64
//! 3. fn celsius_to_fahrenheit(c: f64) -> f64    (formula: F = C * 9/5 + 32)
//! 4. fn fahrenheit_to_celsius(f: f64) -> f64    (inverse of the above)
//!
//! Then in a #[test] module, write tests that prove:
//! - double(halve(42.0)) == 42.0          (round-trip property)
//! - fahrenheit_to_celsius(celsius_to_fahrenheit(25.0)) is approximately 25.0
//! - celsius_to_fahrenheit(0.0) == 32.0   (known value: freezing point)
//! - celsius_to_fahrenheit(100.0) == 212.0 (known value: boiling point)
//!
//! CONSTRAINTS:
//! - Each function is one expression (no intermediate variables needed)
//! - For the approximate equality test, use a tolerance of 1e-9
//!   (hint: assert!((actual - expected).abs() < 1e-9))
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
    // TODO: call your functions and print results
}
