//! Orbital mechanics: gravity, propagation, and orbit diagnostics.
//!
//! # Purpose
//! Central gravity models, orbit propagation, and conservation-law
//! diagnostics (energy, angular momentum). The foundation for mission
//! analysis (Stage 3+).
//!
//! # What lives here (eventually)
//! - `gravity` (Session 22): `GravityModel` trait, point-mass acceleration
//! - `diagnostics` (Session 23): specific energy, angular momentum, circular speed
//!
//! # Sessions that feed into this crate
//! | Session | Concept              | Target module     |
//! |---------|----------------------|-------------------|
//! | 22      | Inverse-square gravity| `gravity.rs`     |
//! | 23      | Conservation diagnostics| `diagnostics.rs`|
//!
//! # Status
//! Stub. Populated when Session 22 graduates gravity here.

#![allow(dead_code)]
