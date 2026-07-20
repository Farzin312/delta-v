//! Numerical methods: differentiation, integration, and ODE solvers.
//!
//! # Purpose
//! The computational engine that turns physical laws into evolving states.
//! Every method here has a convergence study or property test proving it
//! behaves as claimed.
//!
//! # What lives here (eventually)
//! - `sample` (Session 11): generic function sampling with nonfinite rejection
//! - `differentiation` (Session 12): forward and central differences
//! - `finite_data` (Session 13): velocity/acceleration from timestamped data
//! - `integration` (Session 14): trapezoid rule, left/right/midpoint
//! - `dynamics` (Session 25): `Dynamics<S>` trait, state-derivative API
//! - `euler` (Session 26): explicit Euler step
//! - `midpoint` (Session 27): second-order midpoint method
//!
//! # Sessions that feed into this crate
//! | Session | Concept              | Target module        |
//! |---------|----------------------|----------------------|
//! | 11      | Graph sampling       | `sample.rs`          |
//! | 12      | Numerical derivative | `differentiation.rs` |
//! | 13      | Finite data rates    | `finite_data.rs`     |
//! | 14      | Trapezoid integral   | `integration.rs`     |
//! | 25      | Dynamics trait       | `dynamics.rs`        |
//! | 26      | Euler integrator     | `euler.rs`           |
//! | 27      | Midpoint integrator  | `midpoint.rs`        |
//!
//! # Status
//! Stub. Populated when Session 11 graduates sampling here.

#![allow(dead_code)]
