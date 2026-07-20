//! Drill 04: Newtype Pattern, Tuple Structs, Impl, Copy
//!
//! Concepts: encoding meaning in types, compile-time unit safety
//! Time target: under 15 minutes from a blank file
//!
//! INSTRUCTIONS:
//! From scratch, write:
//!
//! 1. Three newtype wrappers around f64:
//!    struct Celsius(f64);
//!    struct Fahrenheit(f64);
//!    struct Kelvin(f64);
//!
//! 2. Derive Debug, Clone, Copy, PartialEq on each.
//!
//! 3. Constructor functions that validate:
//!    impl Celsius  { fn new(c: f64) -> Option<Self> }  // reject NaN
//!    impl Kelvin   { fn new(k: f64) -> Option<Self> }  // reject negative or NaN
//!    (Fahrenheit can skip validation for this drill)
//!
//! 4. Conversion functions:
//!    impl Celsius { fn to_kelvin(self) -> Kelvin }      // K = C + 273.15
//!    impl Kelvin  { fn to_celsius(self) -> Celsius }    // C = K - 273.15
//!
//! 5. Prove the round-trip works: celsius -> kelvin -> celsius returns the start.
//!
//! CONSTRAINTS:
//! - The inner .0 field must NOT be pub. All access goes through methods.
//! - It must be a compile error to add Celsius + Kelvin.
//! - Celsius::new(f64::NAN) must return None.
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
    // TODO: demonstrate conversions
}
