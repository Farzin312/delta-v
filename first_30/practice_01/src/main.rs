//! Session 01: Make an equation executable
//! Units, multiplication, and scientific notation
//!
//! This is the BINARY file (main.rs). It is the program's entry point.
//! It calls functions from lib.rs, prints results, and handles errors.
//!
//! When you run `cargo run`, Rust looks for `fn main()` in this file.
//! That is the only entry point. There is no other way into the program.
//!
//! ====================================================================
//! KEY CONCEPT: THE BINARY/LIBRARY SPLIT
//! ====================================================================
//! - lib.rs  = pure logic, no I/O, fully testable. "The brain."
//! - main.rs = I/O, user interaction, error display. "The mouth."
//! - main.rs imports from lib.rs using `use` and the crate name.
//!
//! The crate name comes from Cargo.toml: [package] name = "practice_01".
//! So we import as `use practice_01::...` or just `practice_01::...`.

// ------------------------------------------------------------------
// IMPORTS
// ------------------------------------------------------------------

// `use` brings items from another module into scope so we don't have to
// type the full path every time.
//
// `practice_01` is the name of our own crate (defined in Cargo.toml).
// When you have both lib.rs and main.rs, Rust automatically lets main.rs
// access the library by its crate name.
//
// We import specific items inside `{}` rather than the whole crate with `*`.
// This makes it explicit what we depend on — no hidden imports.
use practice_01::{
    DistanceUnit, SPEED_OF_LIGHT_MPS, TimeUnit, convert_distance, convert_time, distance_traveled,
};

// ------------------------------------------------------------------
// MAIN FUNCTION
// ------------------------------------------------------------------

/// The program's entry point. Returns the unit type `()` (void in other languages).
///
/// `fn main()` has no return type annotation because `()` is the default.
/// If we wanted to return an exit code to the OS, we would write
/// `fn main() -> Result<(), Box<dyn std::error::Error>>` and use `?`.
fn main() {
    println!("=== Session 01: Signal Distance Calculator ===");
    println!();

    // ------------------------------------------------------------------
    // DEMO 1: The Session 01 problem — light traveling for 12.5 ms
    // ------------------------------------------------------------------
    println!("--- Demo 1: Light traveling for 12.5 ms ---");

    // Call the library function. It returns Result<f64, String>.
    // We handle the Result with a match — success prints the answer,
    // failure prints the error and exits gracefully.
    match distance_traveled(SPEED_OF_LIGHT_MPS, 12.5, TimeUnit::Milliseconds) {
        Ok(meters) => {
            // Convert meters to kilometers for display.
            // unwrap() here is safe because we know the value is valid.
            let km =
                convert_distance(meters, DistanceUnit::Meters, DistanceUnit::Kilometers).unwrap();

            // {:.4} formats f64 to 4 decimal places.
            // {:e} would give scientific notation (e.g. 3.7474e6).
            println!("Distance (meters):     {:>14.4} m", meters);
            println!("Distance (kilometers): {:>14.4} km", km);
            println!();
        }
        Err(e) => {
            eprintln!("Error: {e}");
            return;
        }
    }

    // ------------------------------------------------------------------
    // DEMO 2: Various unit conversions
    // ------------------------------------------------------------------
    println!("--- Demo 2: Unit conversions ---");

    print_conversion("12.5 ms -> seconds", || {
        convert_time(12.5, TimeUnit::Milliseconds, TimeUnit::Seconds)
    });
    print_conversion("5 minutes -> seconds", || {
        convert_time(5.0, TimeUnit::Minutes, TimeUnit::Seconds)
    });
    print_conversion("10000 m -> km", || {
        convert_distance(10_000.0, DistanceUnit::Meters, DistanceUnit::Kilometers)
    });
    print_conversion("1 hour -> seconds", || {
        convert_time(1.0, TimeUnit::Hours, TimeUnit::Seconds)
    });
    println!();

    // ------------------------------------------------------------------
    // DEMO 3: Fail-fast validation (invalid inputs)
    // ------------------------------------------------------------------
    println!("--- Demo 3: Invalid input handling ---");

    print_conversion("NaN ms -> seconds", || {
        convert_time(f64::NAN, TimeUnit::Milliseconds, TimeUnit::Seconds)
    });
    print_conversion("-5 s -> ms (negative time)", || {
        distance_traveled(SPEED_OF_LIGHT_MPS, -5.0, TimeUnit::Seconds)
    });
    print_conversion("inf s -> ms", || {
        convert_time(f64::INFINITY, TimeUnit::Seconds, TimeUnit::Milliseconds)
    });
}

// ------------------------------------------------------------------
// HELPER: Print a conversion result or its error
// ------------------------------------------------------------------

/// Call a conversion function and print the result or error.
///
/// This takes a CLOSURE (anonymous function) as its second argument.
/// `Fn() -> Result<f64, String>` means "something callable that takes
/// no arguments and returns Result<f64, String>."
///
/// WHY A CLOSURE?
/// Each conversion function has a different signature (different arguments).
/// Instead of writing the print logic three times, we pass the call as a
/// closure and this function handles the printing once.
///
/// The closure is `Fn` (not `FnMut` or `FnOnce`) because we only call it once
/// and it does not mutate external state.
fn print_conversion(label: &str, converter: impl Fn() -> Result<f64, String>) {
    // `impl Fn()` is shorthand for "accept any type that implements Fn()."
    // This is a generic parameter, but Rust infers the concrete type.
    match converter() {
        Ok(value) => println!("  {label:<40} => {value:.6}"),
        Err(e) => println!("  {label:<40} => ERROR: {e}"),
    }
}
