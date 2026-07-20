//! Classical mechanics: kinematics, forces, energy, impulse.
//!
//! # Purpose
//! Newton's laws, energy conservation, and momentum transfer as tested,
//! validated Rust. The physics layer that the orbit and control crates
//! build on.
//!
//! # What lives here (eventually)
//! - `kinematics` (Session 02): speed, distance, constant-velocity motion
//! - `sampling` (Session 07): sample continuous motion at discrete times
//! - `work` (Session 17): mechanical work from force and displacement
//! - `dynamics` (Session 21): acceleration from net force and mass
//! - `impulse` (Session 24): impulse, momentum change, ideal delta-v
//!
//! # Sessions that feed into this crate
//! | Session | Concept              | Target module  |
//! |---------|----------------------|----------------|
//! | 02      | Kinematics           | `kinematics.rs`|
//! | 07      | Motion sampling      | `sampling.rs`  |
//! | 17      | Work                 | `work.rs`      |
//! | 21      | Dynamics (F=ma)      | `dynamics.rs`  |
//! | 24      | Impulse / delta-v    | `impulse.rs`   |
//!
//! # Status
//! Stub. Populated when Session 02 graduates kinematics here.

#![allow(dead_code)]
