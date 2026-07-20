//! Session 01: Make an equation executable
//!
//! This is the LIBRARY file (lib.rs). It contains PURE LOGIC:
//! unit conversions, physics calculations, and input validation.
//!
//! There is NO printing (println!), NO user interaction, NO side effects here.
//! All of that lives in main.rs. This separation lets us test the logic
//! independently of how it is displayed.
//!
//! ====================================================================
//! KEY CONCEPT: WHY SPLIT lib.rs AND main.rs?
//! ====================================================================
//! - lib.rs is the "brain": pure math, no I/O, fully testable.
//! - main.rs is the "mouth": calls lib functions, prints results, handles errors.
//! - Tests import from lib.rs. You cannot easily test code that does println!.
//! - Another program could use your lib.rs without any of your printing code.

// ------------------------------------------------------------------
// CONSTANTS
// ------------------------------------------------------------------

/// Speed of light in vacuum, in meters per second (exact, by SI definition).
///
/// `const` means a compile-time constant. The compiler inlines it wherever used.
/// For immutable scientific constants, always use `const` (not `static` or `let`).
///
/// The underscores in the number are visual separators. Rust ignores them.
/// 299_792_458 is identical to 299792458. They make large numbers readable.
pub const SPEED_OF_LIGHT_MPS: f64 = 299_792_458.0;

// ------------------------------------------------------------------
// ENUMS: Representing units as closed sets
// ------------------------------------------------------------------

/// All supported time units.
///
/// WHY AN ENUM INSTEAD OF A STRING?
/// A string lets the user pass "banana" as a unit. An enum makes that impossible
/// at compile time. The compiler also forces every `match` to handle all variants.
/// If you add a new unit later, the compiler will refuse to build until you handle it.
///
/// WHY `#[derive(...)]`?
/// These are traits (interfaces). Deriving them gives us free implementations:
/// - `Debug`: allows printing with {:?} — needed for error messages and debugging.
/// - `Clone`: allows creating a copy via `.clone()`.
/// - `Copy`: allows bitwise copy on assignment instead of moving the value.
///   Without Copy, passing the enum to a function would consume it.
///   For small enums (no heap data), Copy is always correct and efficient.
/// - `PartialEq`: allows comparison with == and !=, which we need in tests.
/// - `Eq`: marks this type as having full equality (no edge cases like NaN).
///   Enums are always Eq because every variant is a distinct exact value.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum TimeUnit {
    Milliseconds,
    Seconds,
    Minutes,
    Hours,
}

/// All supported distance units. Same derive rationale as TimeUnit.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum DistanceUnit {
    Millimeters,
    Centimeters,
    Meters,
    Kilometers,
}

// ------------------------------------------------------------------
// PRIVATE HELPERS: Base-unit conversion
// ------------------------------------------------------------------
// These functions are PRIVATE (no `pub`). Only other functions in this file
// can call them. External code goes through the public API below.
//
// DESIGN PATTERN: "Convert to base, then from base."
// Instead of writing N*N direct conversion functions (ms->s, ms->min, s->ms, ...),
// we write 2*N functions: "anything to base" and "base to anything."
// For 4 time units that is 8 functions instead of 16. Adding a 5th unit adds
// only 2 functions, not 9. This scales.

/// Convert any time value into seconds (the SI base unit for time).
///
/// `match` is Rust's pattern matching. It is like a switch statement, but:
/// 1. It must be EXHAUSTIVE — every enum variant must be handled.
/// 2. There is no implicit fallthrough (unlike C's switch).
/// 3. It returns a value (the whole match expression evaluates to something).
///
/// Parameters use `unit: TimeUnit` not `unit: &TimeUnit`.
/// Because TimeUnit derives Copy, passing by value is free (bitwise copy).
/// No need for references on small Copy types.
fn time_to_seconds(value: f64, unit: TimeUnit) -> f64 {
    match unit {
        TimeUnit::Milliseconds => value * 1e-3, // 1 ms = 0.001 s
        TimeUnit::Seconds => value,             // already in seconds, identity
        TimeUnit::Minutes => value * 60.0,      // 1 min = 60 s
        TimeUnit::Hours => value * 3600.0,      // 1 hr = 3600 s
                                                 // No `_ =>` wildcard. If we add TimeUnit::Days later and forget it here,
                                                 // the compiler will error: "non-exhaustive patterns." That is the safety net.
    }
}

/// Convert a value in seconds into a target time unit.
fn seconds_to_time(seconds: f64, target: TimeUnit) -> f64 {
    match target {
        TimeUnit::Milliseconds => seconds * 1e3, // 1 s = 1000 ms
        TimeUnit::Seconds => seconds,            // identity
        TimeUnit::Minutes => seconds / 60.0,     // 1 s = 1/60 min
        TimeUnit::Hours => seconds / 3600.0,     // 1 s = 1/3600 hr
    }
}

/// Convert any distance value into meters (the SI base unit for distance).
fn distance_to_meters(value: f64, unit: DistanceUnit) -> f64 {
    match unit {
        DistanceUnit::Millimeters => value * 1e-3, // 1 mm = 0.001 m
        DistanceUnit::Centimeters => value * 1e-2, // 1 cm = 0.01 m
        DistanceUnit::Meters => value,             // identity
        DistanceUnit::Kilometers => value * 1e3,   // 1 km = 1000 m
    }
}

/// Convert a value in meters into a target distance unit.
fn meters_to_distance(meters: f64, target: DistanceUnit) -> f64 {
    match target {
        DistanceUnit::Millimeters => meters * 1e3, // 1 m = 1000 mm
        DistanceUnit::Centimeters => meters * 1e2, // 1 m = 100 cm
        DistanceUnit::Meters => meters,            // identity
        DistanceUnit::Kilometers => meters * 1e-3, // 1 m = 0.001 km
    }
}

// ------------------------------------------------------------------
// VALIDATION HELPER
// ------------------------------------------------------------------

/// Check that a floating-point value is a real, finite number.
///
/// WHY VALIDATE FLOATS?
/// f64 can represent three non-values that silently corrupt calculations:
/// - NaN (Not a Number): result of 0.0/0.0. NaN poisons everything: NaN + 1 = NaN.
///   Any comparison with NaN returns false, even NaN == NaN. This breaks tests silently.
/// - Infinity: result of x/0.0 for nonzero x. Infinity propagates and hides errors.
///
/// Returning `Result<(), String>` means: success carries no data (empty tuple `()`),
/// failure carries a human-readable error message.
///
/// `&str` is a reference to a string slice. We use it for the parameter name
/// because we only read it, never modify it. `&str` is cheaper than `String`
/// (no heap allocation).
fn validate_finite(value: f64, name: &str) -> Result<(), String> {
    // GUARD CLAUSE 1: reject NaN first.
    // Early return = "fail fast." The function exits immediately on the first problem.
    // The rest of the function (the happy path) stays at zero indentation depth.
    if value.is_nan() {
        return Err(format!("{name} is NaN (not a number)"));
    }

    // GUARD CLAUSE 2: reject infinity.
    if value.is_infinite() {
        return Err(format!("{name} is infinite"));
    }

    // All guards passed. Return Ok with nothing inside (the unit type `()`).
    Ok(())
}

// ------------------------------------------------------------------
// PUBLIC API
// ------------------------------------------------------------------
// These are the functions that main.rs (and tests) are allowed to call.
// They are the "front door" — they validate inputs, then delegate to the
// private helpers above.

/// Convert a time value from one unit to another.
///
/// Returns `Ok(result)` on success, or `Err(message)` if the input is invalid.
///
/// The `pub` keyword makes this function visible outside this module.
/// Without `pub`, only code within lib.rs could call it.
///
/// `&str` in the error type means the error borrows a string — it does not
/// own heap memory. For Session 01 this is simple and correct.
pub fn convert_time(value: f64, from: TimeUnit, to: TimeUnit) -> Result<f64, String> {
    // Validate before computing. Fail fast, fail loud.
    validate_finite(value, "time value")?;

    // The `?` operator is shorthand for match:
    //
    //   validate_finite(value, "time value")?
    //
    // is equivalent to:
    //
    //   match validate_finite(value, "time value") {
    //       Ok(()) => {},                  // validation passed, continue
    //       Err(e) => return Err(e),       // validation failed, propagate error
    //   }
    //
    // The `?` operator propagates errors upward without nesting match blocks.
    // It is the idiomatic Rust pattern for error handling.

    // Convert: from-unit -> seconds -> to-unit.
    // Chain the two private helpers through the base unit.
    let seconds = time_to_seconds(value, from);
    let result = seconds_to_time(seconds, to);

    Ok(result)
}

/// Convert a distance value from one unit to another.
///
/// Same structure as convert_time: validate, then convert through base unit.
pub fn convert_distance(value: f64, from: DistanceUnit, to: DistanceUnit) -> Result<f64, String> {
    validate_finite(value, "distance value")?;

    let meters = distance_to_meters(value, from);
    let result = meters_to_distance(meters, to);

    Ok(result)
}

/// Compute the distance a signal travels at a given speed for a given duration.
///
/// This is the core physics function for Session 01: distance = speed x time.
/// It accepts time in any supported TimeUnit, converts to seconds internally,
/// and returns distance in meters.
///
/// Parameters:
/// - `speed_mps`: speed in meters per second (pass SPEED_OF_LIGHT_MPS for light)
/// - `duration`: how long the signal travels (the number, e.g. 12.5)
/// - `duration_unit`: what unit that number is in (e.g. TimeUnit::Milliseconds)
///
/// Returns: distance in meters, or an error describing what went wrong.
pub fn distance_traveled(
    speed_mps: f64,
    duration: f64,
    duration_unit: TimeUnit,
) -> Result<f64, String> {
    // GUARD: validate speed.
    // Note: we validate that speed is finite, but we do NOT reject negative speed here.
    // Why? A signed velocity is physically meaningful (direction matters in physics).
    // For Session 01 (light), speed is always positive. But keeping the function general
    // makes it reusable for later sessions (e.g., negative velocity in kinematics).
    validate_finite(speed_mps, "speed")?;

    // GUARD: validate duration.
    // Unlike speed, negative duration is physically meaningless in every context.
    // Reject it here with an actionable message.
    validate_finite(duration, "duration")?;
    if duration < 0.0 {
        return Err(format!("duration must be non-negative, got {duration}"));
    }

    // Convert duration to seconds, then compute distance = speed x time.
    let duration_seconds = time_to_seconds(duration, duration_unit);
    let distance_meters = speed_mps * duration_seconds;

    Ok(distance_meters)
}

// ==================================================================
// TESTS
// ==================================================================
// `#[cfg(test)]` means: compile this module ONLY when running `cargo test`.
// It does not bloat the release binary. Your shipped code has zero test overhead.
//
// `mod tests` creates a nested module. Rust uses modules to organize code.
// The tests live inside this module, separate from the production code above.
//
// `use super::*;` (inside the module) imports everything from the parent module
// (lib.rs). `super` means "parent module" and `*` means "everything."
// This lets tests call convert_time() directly instead of super::convert_time().

#[cfg(test)]
mod tests {
    use super::*;

    // ------------------------------------------------------------------
    // HELPER: floating-point approximate equality
    // ------------------------------------------------------------------
    // NEVER use == with f64. Floating-point arithmetic introduces tiny errors.
    // 0.1 + 0.2 does not exactly equal 0.3 in IEEE 754. Instead, check that
    // the absolute difference is below a small threshold (tolerance).
    //
    // We use 1e-6 (one millionth) as tolerance. This is tight enough to catch
    // real bugs but loose enough to tolerate rounding from unit conversions.
    fn approx_eq(actual: f64, expected: f64) -> bool {
        (actual - expected).abs() < 1e-6
    }

    // ------------------------------------------------------------------
    // convert_time tests
    // ------------------------------------------------------------------

    #[test]
    fn convert_time_known_12_5_ms_to_seconds() {
        // KNOWN VALUE: 12.5 milliseconds = 0.0125 seconds (hand-calculated).
        // This is the exact conversion from the Session 01 problem.
        let result = convert_time(12.5, TimeUnit::Milliseconds, TimeUnit::Seconds);
        assert!(result.is_ok(), "expected Ok, got Err: {:?}", result);
        assert!(
            approx_eq(result.unwrap(), 0.0125),
            "12.5 ms should be 0.0125 s"
        );
    }

    #[test]
    fn convert_time_known_1_minute_to_seconds() {
        // KNOWN VALUE: 1 minute = 60 seconds.
        let result = convert_time(1.0, TimeUnit::Minutes, TimeUnit::Seconds);
        assert!(approx_eq(result.unwrap(), 60.0));
    }

    #[test]
    fn convert_time_identity_seconds_to_seconds() {
        // BOUNDARY/PROPERTY: converting to the same unit is identity (no change).
        let result = convert_time(42.0, TimeUnit::Seconds, TimeUnit::Seconds);
        assert!(approx_eq(result.unwrap(), 42.0));
    }

    #[test]
    fn convert_time_round_trip() {
        // PROPERTY: converting ms -> s -> ms should recover the original value.
        // This tests that the forward and inverse conversions are consistent.
        // If they are not, at least one of them is wrong.
        let original = 250.0; // 250 ms
        let to_seconds = convert_time(original, TimeUnit::Milliseconds, TimeUnit::Seconds).unwrap();
        let back_to_ms =
            convert_time(to_seconds, TimeUnit::Seconds, TimeUnit::Milliseconds).unwrap();
        assert!(
            approx_eq(back_to_ms, original),
            "round-trip ms -> s -> ms should recover {original}, got {back_to_ms}"
        );
    }

    #[test]
    fn convert_time_rejects_nan() {
        // ERROR CASE: NaN must be rejected, not silently propagated.
        // f64::NAN is the NaN constant built into the standard library.
        let result = convert_time(f64::NAN, TimeUnit::Seconds, TimeUnit::Milliseconds);
        assert!(result.is_err(), "NaN should be rejected");
        assert!(
            result.unwrap_err().contains("NaN"),
            "error message should mention NaN"
        );
    }

    #[test]
    fn convert_time_rejects_infinity() {
        // ERROR CASE: infinity must also be rejected.
        let result = convert_time(f64::INFINITY, TimeUnit::Seconds, TimeUnit::Milliseconds);
        assert!(result.is_err());
    }

    // ------------------------------------------------------------------
    // convert_distance tests
    // ------------------------------------------------------------------

    #[test]
    fn convert_distance_known_meters_to_km() {
        // KNOWN VALUE: 3747405.725 meters = 3747.405725 kilometers.
        // This is the Session 01 answer converted to km.
        let result = convert_distance(
            3_747_405.725,
            DistanceUnit::Meters,
            DistanceUnit::Kilometers,
        );
        assert!(approx_eq(result.unwrap(), 3747.405725));
    }

    #[test]
    fn convert_distance_known_km_to_meters() {
        // KNOWN VALUE: 1 km = 1000 m.
        let result = convert_distance(1.0, DistanceUnit::Kilometers, DistanceUnit::Meters);
        assert!(approx_eq(result.unwrap(), 1000.0));
    }

    #[test]
    fn convert_distance_zero_stays_zero() {
        // BOUNDARY: zero in any unit is zero in any other unit.
        let result = convert_distance(0.0, DistanceUnit::Meters, DistanceUnit::Kilometers);
        assert!(approx_eq(result.unwrap(), 0.0));
    }

    #[test]
    fn convert_distance_round_trip() {
        // PROPERTY: km -> m -> km recovers the original.
        let original = 5.5; // 5.5 km
        let to_m =
            convert_distance(original, DistanceUnit::Kilometers, DistanceUnit::Meters).unwrap();
        let back = convert_distance(to_m, DistanceUnit::Meters, DistanceUnit::Kilometers).unwrap();
        assert!(approx_eq(back, original));
    }

    // ------------------------------------------------------------------
    // distance_traveled tests
    // ------------------------------------------------------------------

    #[test]
    fn distance_traveled_known_light_12_5ms() {
        // KNOWN VALUE: the Session 01 problem.
        // c = 299,792,458 m/s, t = 12.5 ms = 0.0125 s
        // d = 299,792,458 * 0.0125 = 3,747,405.725 m
        let result = distance_traveled(SPEED_OF_LIGHT_MPS, 12.5, TimeUnit::Milliseconds);
        assert!(result.is_ok());
        let meters = result.unwrap();
        assert!(
            approx_eq(meters, 3_747_405.725),
            "expected 3747405.725 m, got {meters}"
        );

        // Cross-check: convert that to km.
        let km = convert_distance(meters, DistanceUnit::Meters, DistanceUnit::Kilometers).unwrap();
        assert!(
            approx_eq(km, 3747.405725),
            "expected 3747.405725 km, got {km}"
        );
    }

    #[test]
    fn distance_traveled_zero_speed() {
        // BOUNDARY: if speed is 0, distance is 0 regardless of time.
        let result = distance_traveled(0.0, 12.5, TimeUnit::Milliseconds);
        assert!(approx_eq(result.unwrap(), 0.0));
    }

    #[test]
    fn distance_traveled_zero_duration() {
        // BOUNDARY: if time is 0, distance is 0 regardless of speed.
        let result = distance_traveled(SPEED_OF_LIGHT_MPS, 0.0, TimeUnit::Seconds);
        assert!(approx_eq(result.unwrap(), 0.0));
    }

    #[test]
    fn distance_traveled_rejects_negative_duration() {
        // ERROR CASE: negative duration is physically meaningless.
        let result = distance_traveled(SPEED_OF_LIGHT_MPS, -1.0, TimeUnit::Seconds);
        assert!(result.is_err());
        assert!(
            result.unwrap_err().contains("non-negative"),
            "error should explain the constraint"
        );
    }

    #[test]
    fn distance_traveled_rejects_nan_speed() {
        // ERROR CASE: NaN speed must fail fast.
        let result = distance_traveled(f64::NAN, 1.0, TimeUnit::Seconds);
        assert!(result.is_err());
    }

    #[test]
    fn distance_traveled_rejects_infinity_duration() {
        // ERROR CASE: infinite duration must fail fast.
        let result = distance_traveled(SPEED_OF_LIGHT_MPS, f64::INFINITY, TimeUnit::Seconds);
        assert!(result.is_err());
    }
}
