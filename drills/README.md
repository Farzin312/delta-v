# Rust Drills Library

> Language use and language study are different.
> Using Rust to implement a physics equation teaches application.
> This directory builds language FLUENCY through focused, independent practice.

These drills are SEPARATE from the session BRIEFs. Each session has a small
drill inside it, but this library gives you a systematic progression through
Rust language concepts - the same concept can be drilled from multiple angles.

---

## How to Use the Drills

1. Pick ONE drill per day (15-30 minutes)
2. Work from a BLANK FILE. No copy-paste. No AI autocomplete.
3. If you get stuck, consult the Rust Book or Rust by Example - not AI solutions
4. Run `cargo fmt` and `cargo clippy -- -D warnings` when done
5. Time yourself. Track your times in the drill's Notes section.
6. Re-do the drill 1 week later. Your time should improve.

---

## Drill Progression

The drills follow the PDF's language sequence:
The Rust Book -> Rustlings -> Rust by Example -> Standard Library docs

### Phase 1: Fundamentals (parallel to Sessions 01-05)

| Drill | Concept | What you write from a blank file | Time target |
|-------|---------|----------------------------------|-------------|
| [01-fundamentals](01-fundamentals/README.md) | Bindings, types, functions | A pure multiply fn, a named constant, formatted output, two assertions | < 10 min |
| [02-functions](02-functions/README.md) | Parameters, return values, expressions | Three inverse functions + round-trip composition test | < 10 min |
| [03-enums-errors](03-enums-errors/README.md) | Enums, match, Result, ? operator | A parser returning a custom enum with 3+ error variants | < 15 min |
| [04-newtypes](04-newtypes/README.md) | Tuple structs, impl, Copy, newtype | Three semantic f64 wrappers + one conversion between them | < 15 min |
| [05-structs-methods](05-structs-methods/README.md) | Structs, methods, self, derive | Point2 + Vec2 with different APIs, derive Debug/Clone/Copy/PartialEq | < 15 min |

### Phase 2: Ownership and Borrowing (parallel to Sessions 06-10)

| Drill | Concept | What you write from a blank file | Time target |
|-------|---------|----------------------------------|-------------|
| [06-ownership](06-ownership/README.md) | Move semantics, ownership | A function that takes ownership and returns a new value | < 15 min |
| [07-references](07-references/README.md) | Borrows, & vs &mut, lifetimes | A function borrowing a slice and returning a computed value | < 15 min |
| [08-iterators](08-iterators/README.md) | Iterator chains, collect, map, filter | Process a Vec using only iterator methods, no loops | < 20 min |
| [09-modules](09-modules/README.md) | mod, pub, use, file structure | Split a 50-line file into 3 modules with proper visibility | < 20 min |
| [10-crate-design](10-crate-design/README.md) | lib.rs vs main.rs, crate root | Refactor a one-file program into library + binary | < 25 min |

### Phase 3: Abstraction (parallel to Sessions 11-15)

| Drill | Concept | What you write from a blank file | Time target |
|-------|---------|----------------------------------|-------------|
| [11-closures](11-closures/README.md) | Fn, FnMut, FnOnce, capturing | A generic sampler accepting a closure and returning results | < 20 min |
| [12-generics](12-generics/README.md) | Generic functions, generic structs | A function and struct that work with any numeric type | < 20 min |
| [13-traits](13-traits/README.md) | Trait definitions, impl blocks, trait objects | A trait with two implementors + a function using the trait | < 25 min |
| [14-associated-types](14-associated-types/README.md) | Associated types, trait bounds | A Dynamics-style trait with an associated Derivative type | < 25 min |
| [15-operator-overload](15-operator-overload/README.md) | Add, Sub, Mul, Index traits | Implement Add and Mul for a custom numeric type | < 25 min |

### Phase 4: Testing and Robustness (parallel to Sessions 16-20)

| Drill | Concept | What you write from a blank file | Time target |
|-------|---------|----------------------------------|-------------|
| [16-unit-tests](16-unit-tests/README.md) | #[test], assert_eq, test modules | Write a function + 4 tests (known, boundary, property, error) | < 15 min |
| [17-integration-tests](17-integration-tests/README.md) | tests/ directory, external test crates | An integration test that calls a library's public API | < 20 min |
| [18-property-tests](18-property-tests/README.md) | Property testing, reproducible seeds | A property test using a deterministic loop with logged seeds | < 25 min |
| [19-error-propagation](19-error-propagation/README.md) | ?, From, custom error types | A 3-function chain that propagates errors to the caller | < 20 min |
| [20-floating-point](20-floating-point/README.md) | IEEE-754, NaN, infinity, approx_eq | A scale-aware approximate equality function + edge tests | < 20 min |

---

## Drill Structure

Each drill directory contains:

```
drills/NN-name/
  README.md      Instructions: what to write, constraints, time target
  src/main.rs    Empty scaffold (module doc comment only, no solution)
  Cargo.toml     Standalone Cargo project
```

The scaffold has NO solution. You write the code. When you're done:

```bash
cd drills/01-fundamentals
cargo test          # does your code pass your own tests?
cargo clippy -- -D warnings
cargo fmt --check
```

If you want to check your work against a reference, the Rust Book and
Rust by Example are the sources of truth - not AI.

---

## Drill Schedule

### Option A: Drills follow sessions
Do the matching drill on the same day as the session:
- Session 01 day -> Drill 01
- Session 02 day -> Drill 02
- etc.

### Option B: Dedicated drill days
On Day 2 and Day 6 of the weekly rhythm (language depth + review),
do 2-3 drills instead of a session.

### Option C: Standalone fluency practice
Before starting the sessions, do drills 01-10 to build baseline Rust
fluency. This is recommended if you are new to Rust.

---

## Timing Standards

| Skill Level | 15-min drill | 25-min drill |
|-------------|-------------|--------------|
| Beginner | Still working at time limit | Not finished |
| Developing | Done with minor issues | Mostly done |
| Working | Done and passing | Done with minor issues |
| Fluent | Done, passing, clippy clean | Done and passing |

Track your times in each drill's Notes section. If a drill takes more
than 2x the target time, re-do it the next day before moving on.

---

[<- Daily Practice Guide](../docs/daily_practice.md) | [<- Knowledge Tracker](../docs/knowledge_tracker.md)
