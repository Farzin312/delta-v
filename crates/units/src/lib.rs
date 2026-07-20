//! Physical quantities with visible units in the type system.
//!
//! # Purpose
//! Prevent unit swaps and scale mistakes by encoding units in types rather
//! than in comments. A `Meters` value cannot be silently passed where
//! `Seconds` is expected.
//!
//! # What lives here (eventually)
//! - `Meters`, `Seconds`, `MetersPerSecond`, `Kilograms`, `Joules` newtypes
//! - `Angle` (radians internally, degree constructors)
//! - Validated constructors that reject non-finite inputs
//! - Conversions: m <-> km, ms <-> s, deg <-> rad
//!
//! # Sessions that feed into this crate
//! | Session | Concept              | Target module     |
//! |---------|----------------------|-------------------|
//! | 01      | Unit conversion      | `units.rs`        |
//! | 04      | Newtype quantities   | `lib.rs`          |
//! | 06      | Angle type           | `angle.rs`        |
//!
//! # Status
//! Stub. Populated when Session 04 graduates its concepts here.

#![allow(dead_code)]
