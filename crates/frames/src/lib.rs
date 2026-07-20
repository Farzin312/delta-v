//! Coordinate frames and frame transformations.
//!
//! # Purpose
//! Three numbers are not a complete physical quantity — they need a frame
//! label. This crate tags vectors with their frame and rejects operations
//! across mismatched frames at compile time or runtime.
//!
//! # What lives here (eventually)
//! - `Frame` enum: `Inertial`, `EarthFixed`, `Body` (Session 08)
//! - `TaggedVec3`: value + frame tag (Session 08)
//! - `require_same_frame`: validation for same-frame operations (Session 08)
//! - `Rotation2`: 2-D rotation (graduates from math, Session 18)
//! - `Transform2`: rotation + translation (Session 19)
//!
//! # Sessions that feed into this crate
//! | Session | Concept              | Target module  |
//! |---------|----------------------|----------------|
//! | 08      | Frame tagging        | `lib.rs`       |
//! | 18      | 2-D rotation         | `rotation2.rs` |
//! | 19      | Transform composition| `transform2.rs`|
//!
//! # Status
//! Stub. Populated when Session 08 graduates frame tagging here.

#![allow(dead_code)]
