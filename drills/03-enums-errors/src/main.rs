//! Drill 03: Enums, Match, Result, and the ? Operator
//!
//! Concepts: algebraic data types, pattern matching, error handling
//! Time target: under 15 minutes from a blank file
//!
//! INSTRUCTIONS:
//! From scratch, write:
//!
//! 1. An error enum with at least three variants:
//!    enum ParseError {
//!        Empty,
//!        InvalidCharacter,
//!        OutOfRange,
//!    }
//!
//! 2. A parser function that takes a &str and returns Result<i32, ParseError>:
//!    fn parse_score(input: &str) -> Result<i32, ParseError>
//!    Rules:
//!    - Empty string -> Err(Empty)
//!    - Contains non-digit chars -> Err(InvalidCharacter)
//!    - Number is < 0 or > 100 -> Err(OutOfRange)
//!    - Otherwise -> Ok(the number)
//!    (Hint: use input.parse::<i32>() for the actual parsing)
//!
//! 3. A helper function that uses the ? operator to chain the parse:
//!    fn validate_and_double(input: &str) -> Result<i32, ParseError>
//!    It should call parse_score, double the result, and return it.
//!    Any error from parse_score should propagate via ?.
//!
//! 4. Tests for each error path and the success path.
//!
//! CONSTRAINTS:
//! - Use match, not if/else, for error checking where possible
//! - No wildcard _ => arms in match on ParseError (handle each variant explicitly)
//! - Derive Debug and PartialEq on ParseError
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
    // TODO: demonstrate your parser with valid and invalid inputs
}
