//! Vector types, matrices, and approximate equality for physics code.
//!
//! # Purpose
//! One canonical `Vec2` and `Vec3` with operator traits, cross product,
//! normalization, and approximate comparison. Every other crate depends
//! on these — there must be exactly one definition.
//!
//! # What lives here (eventually)
//! - `Vec2` (Session 05): addition, scaling, norm via hypot, safe normalization
//! - `Vec3` (Session 16): dot, cross, norm, unit vector, operator traits
//! - `Rotation2` (Session 18): 2-D rotation with norm preservation
//! - `Transform2` (Session 19): rotation + translation composition
//! - `approx_eq` (Session 20): scale-aware approximate comparison
//! - `dot` (Session 09): dimension-checked dot product over slices
//!
//! # Sessions that feed into this crate
//! | Session | Concept              | Target module     |
//! |---------|----------------------|-------------------|
//! | 05      | Vec2                 | `vec2.rs`         |
//! | 09      | Dot product          | `dot.rs`          |
//! | 16      | Vec3                 | `vec3.rs`         |
//! | 18      | Rotation2            | `rotation2.rs`    |
//! | 19      | Transform2           | `transform2.rs`   |
//! | 20      | Approximate equality | `approx.rs`       |
//!
//! # Status
//! Stub. Populated when Session 05 graduates Vec2 here.

#![allow(dead_code)]
