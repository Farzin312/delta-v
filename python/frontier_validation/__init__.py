"""Independent Python reference implementations for cross-checking Rust output.

The Python layer exists for ONE reason: to provide an independent check
that Rust code produces correct results. It is NOT the primary implementation
— Rust is. Python here is the "trusted second opinion."

When to add here:
- After a Rust concept graduates to a crate (crates/units, crates/math, etc.)
- When you need to cross-check numerical output (e.g., NumPy dot product
  vs your hand-rolled Rust implementation)
- When you need to plot results for a convergence study or validation report

Naming convention:
    frontier_validation/<crate_name>_ref.py

    e.g., frontier_validation/units_ref.py      — unit conversion checks
         frontier_validation/math_ref.py        — vector math checks
         frontier_validation/numerics_ref.py    — integration checks

Each reference module provides functions that take the same inputs as the
Rust implementation and return the expected result. Tests compare Rust
output (via subprocess or CSV) against these Python results.
"""

__version__ = "0.0.1"
