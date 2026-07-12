#!/usr/bin/env python3
"""
delta-v session generator and lifecycle manager

Creates practice session directories with the standard structure:
  - BRIEF.md    (7-step loop template, optionally blank)
  - Cargo.toml  (independent project)
  - src/main.rs (scaffold with prediction/derivation/code/test sections)
  - .gitignore

Commands:
  new         Create a new numbered session with problem statement and metadata
  blank       Create a blank template folder for self-directed practice
  list        List all sessions in a directory with status
  doctor      Check every session for missing/broken files
  regenerate  Restore missing template files in existing sessions
  help        Show usage

Usage:
  python scripts/new_session.py new
    (interactive: prompts for title, problem, concepts, difficulty)

  python scripts/new_session.py new \\
    --title "Compute orbital period" \\
    --problem "Given semi-major axis 7000 km, find the period" \\
    --math "Kepler's third law" \\
    --rust "Constants, f64, functions" \\
    --difficulty 3

  python scripts/new_session.py blank --name orbital_review

  python scripts/new_session.py doctor
  python scripts/new_session.py regenerate --dir first_30 --session practice_05
  python scripts/new_session.py regenerate --all

  python scripts/new_session.py list
  python scripts/new_session.py list --dir stage_03
"""

import argparse
import os
import sys
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


# ======================================================================
# Template strings
# ======================================================================

BRIEF_TEMPLATE = """# {title}

> Stage {stage} | Difficulty: {d_bars} | Status: NOT STARTED

## The Problem

{problem}

## What This Teaches

| Dimension | Focus |
|-----------|-------|
| Math / Physics | {math} |
| Rust / Engineering | {rust} |

---

## The Learning Loop

Follow all seven steps. Do not skip. Each step catches a failure the others miss. See [docs/method.md](../../docs/method.md) for the full explanation of why each step exists.

### Step 1: PREDICT

Write your prediction BEFORE any calculation or code. No AI. No hints.

Fill in:

```
Sign:         (positive / negative / zero?)
Scale:        (order of magnitude)
Direction:    (which way? increasing / decreasing?)
Units:        (what units should the answer have?)
Failure case: (what input would break this?)
```

### Step 2: EXPLAIN

Draw the physical story in 5 sentences or less. Name:

- System boundary (what is inside / outside the model?)
- Coordinate frame (which axis points where?)
- Assumptions (what are you simplifying away?)
- Inputs (what values go in?)
- Outputs (what comes out?)

### Step 3: DERIVE

Write the equation from definitions. Show dimensional analysis.

```
Equation:
  (write it here)

Dimensional check:
  (do the units match on both sides?)

Limiting cases:
  t = 0:    (what happens?)
  t -> inf: (what happens?)
  a = 0:    (what happens?)
```

### Step 4: IMPLEMENT

Write the smallest pure Rust function that matches your derivation.

Rules:
- One concept per function
- No hidden I/O (no println! inside a pure math function)
- No premature abstraction (no framework, no trait hierarchy)
- Explicit units in variable names (e.g. `time_s` not `t`)

### Step 5: TEST

Write tests in this order. Each catches a different class of error:

1. **Known value** - a textbook or hand-calculated result
2. **Boundary** - zero, empty, maximum, or degenerate input
3. **Property** - a structural invariant (symmetry, conservation, monotonicity)
4. **Independent reference** - cross-check with a different formula or tool (if available)

### Step 6: FALSIFY

Deliberately break your code. Try:

- Extreme values (very large, very small)
- Invalid inputs (negative, NaN, infinity)
- Wrong units (pass seconds where meters expected)
- Model violations (what if acceleration is not constant?)

For each failure, classify it:

- **Bug** - your code is wrong. Fix it.
- **Numerical limit** - your math is right but the computer cannot represent it. Document it.
- **Model limitation** - your equation is correct for its assumptions but they no longer hold. Declare the valid domain.

### Step 7: TEACH

Write what you learned in the Notes section below. Explain:

- What surprised you (where did prediction differ from reality?)
- What you trust and why
- Where the code fails and what the valid domain is
- What concept this unlocks next

---

## Checklist

- [ ] Prediction written before any code
- [ ] Derivation includes dimensional check
- [ ] Implementation compiles with `cargo build`
- [ ] At least one known-value test passes
- [ ] At least one boundary test passes
- [ ] At least one property or independent-reference test
- [ ] `cargo fmt` clean
- [ ] `cargo clippy -- -D warnings` clean
- [ ] At least one failure case identified and classified (bug / numerical / model)
- [ ] Operating domain declared in comments or docs
- [ ] Engineering log entry written
- [ ] Notes section filled in below

## Notes

_Write your discoveries, surprises, and remaining questions here as you work._

- **What surprised me:**
- **What I trust:**
- **Where it fails:**
- **What this unlocks:**
- **Last practiced:** (date)
- **Mastery gate passed:** [ ] yes [ ] not yet
"""

CARGO_TEMPLATE = """[package]
name = "{crate_name}"
version = "0.1.0"
edition = "2024"

[dependencies]
"""

MAIN_TEMPLATE = """//! {title}
//! {math}
//!
//! Rust skills: {rust}
//!
//! TODO: Implement the solution following the 7-step loop.
//! 1. PREDICT - write your prediction as a comment below
//! 2. EXPLAIN - draw/narrate the physical story
//! 3. DERIVE - write the equation with dimensional checks
//! 4. IMPLEMENT - replace todo!() with your code
//! 5. TEST - uncomment and pass the tests
//! 6. FALSIFY - find where it breaks
//! 7. TEACH - write what you learned in the BRIEF.md notes

fn main() {{
    println!("{title}");
    println!("Implement the functions below, then fill in main().");
}}

// === PREDICTION ===
// Write your prediction here before coding:
// Sign:
// Scale:
// Direction:
// Expected failure case:

// === DERIVATION ===
// Equation:
// Dimensional check:
// Limiting cases:

// === IMPLEMENTATION ===
// Write your functions and types here.

// === TESTS ===
// Write your tests here. Uncomment the module when ready.
// #[cfg(test)]
// mod tests {{
//     use super::*;
//
//     #[test]
//     fn test_known_value() {{
//         // TODO: test against a known value
//     }}
// }}
"""

GITIGNORE = "/target\n"

# Required files for every session
REQUIRED_FILES = ["BRIEF.md", "Cargo.toml", "src/main.rs", ".gitignore"]

# Files that should NOT be overwritten during regenerate (user may have edited them)
USER_EDITABLE = {"src/main.rs"}


# ======================================================================
# Utility functions
# ======================================================================

def display_path(path: Path) -> str:
    """Get a display string for a path, relative to repo root if possible."""
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def find_next_number(directory: Path) -> int:
    """Find the highest practice_NN number in a directory, return next."""
    if not directory.exists():
        return 1
    pattern = re.compile(r"(?:practice|unit)_(\d+)")
    highest = 0
    for item in directory.iterdir():
        if item.is_dir():
            m = pattern.match(item.name)
            if m:
                highest = max(highest, int(m.group(1)))
    return highest + 1


def is_session_dir(path: Path) -> bool:
    """Check if a directory looks like a session.
    A session has BRIEF.md OR Cargo.toml OR src/main.rs OR matches practice_/unit_ naming."""
    if not path.is_dir():
        return False
    if (path / "Cargo.toml").exists():
        return True
    if (path / "BRIEF.md").exists():
        return True
    if (path / "src" / "main.rs").exists():
        return True
    if re.match(r"(?:practice|unit)_\d+", path.name):
        return True
    return False


def parse_brief(brief_path: Path) -> dict:
    """Extract metadata from a BRIEF.md file."""
    info = {"title": "?", "status": "?", "stage": "?", "difficulty": "?"}
    if not brief_path.exists():
        return info
    text = brief_path.read_text()

    title_m = re.search(r"^# (.+)$", text, re.MULTILINE)
    if title_m:
        info["title"] = title_m.group(1).strip()

    status_m = re.search(r"Status:\s*(.+?)(?:\n|$)", text)
    if status_m:
        info["status"] = status_m.group(1).strip()

    stage_m = re.search(r"Stage\s+(\S+)", text)
    if stage_m:
        info["stage"] = stage_m.group(1).strip()

    diff_m = re.search(r"Difficulty:\s*(\|+)", text)
    if diff_m:
        info["difficulty"] = str(len(diff_m.group(1)))

    return info


# ======================================================================
# Core creation logic
# ======================================================================

def write_session_files(
    session_dir: Path,
    title: str,
    problem: str,
    math: str,
    rust: str,
    difficulty: int,
    stage: int,
    crate_name: str = "",
):
    """Write all template files into a session directory."""
    session_dir.mkdir(parents=True, exist_ok=True)
    (session_dir / "src").mkdir(exist_ok=True)

    if not crate_name:
        crate_name = session_dir.name.replace("-", "_")

    d_bars = "|" * difficulty

    (session_dir / "BRIEF.md").write_text(
        BRIEF_TEMPLATE.format(
            title=title, problem=problem, math=math, rust=rust,
            d_bars=d_bars, stage=stage,
        )
    )
    (session_dir / "Cargo.toml").write_text(
        CARGO_TEMPLATE.format(crate_name=crate_name)
    )
    (session_dir / "src" / "main.rs").write_text(
        MAIN_TEMPLATE.format(title=title, math=math, rust=rust)
    )
    (session_dir / ".gitignore").write_text(GITIGNORE)


def create_session(
    directory: Path,
    name: str,
    title: str,
    problem: str,
    math: str,
    rust: str,
    difficulty: int,
    stage: int = 1,
):
    """Create a full session directory with all files."""
    session_dir = directory / name
    if session_dir.exists():
        print(f"  ERROR: {display_path(session_dir)} already exists.")
        sys.exit(1)

    write_session_files(
        session_dir, title, problem, math, rust, difficulty, stage
    )

    print(f"\n  Created: {display_path(session_dir)}/")
    print(f"    BRIEF.md       (7-step loop, checklist, notes)")
    print(f"    Cargo.toml     (independent project)")
    print(f"    src/main.rs    (scaffold)")
    print(f"    .gitignore")
    print(f"\n  Next: cd {session_dir} && cargo run")


# ======================================================================
# Commands
# ======================================================================

def resolve_dir(dir_str: str) -> Path:
    """Resolve a --dir argument to an absolute Path."""
    if dir_str.startswith("/"):
        return Path(dir_str)
    return REPO_ROOT / dir_str


def cmd_new(args):
    """Create a new numbered session."""
    directory = resolve_dir(args.dir)
    directory.mkdir(parents=True, exist_ok=True)

    next_num = find_next_number(directory)
    name = f"practice_{next_num:02d}" if args.pad else f"practice_{next_num}"

    if not args.title:
        print(f"\n  Creating session {name} in {args.dir}/\n")
        title = input("  Title (e.g. 'Compute orbital period'): ").strip()
        if not title:
            print("  Title is required. Aborting.")
            sys.exit(1)
        problem = input("  Problem statement: ").strip()
        if not problem:
            print("  Problem is required. Aborting.")
            sys.exit(1)
        math = input("  Math/physics concepts: ").strip() or "TODO"
        rust = input("  Rust skills: ").strip() or "TODO"
        difficulty_str = input("  Difficulty (1-6) [1]: ").strip() or "1"
        difficulty = int(difficulty_str) if difficulty_str.isdigit() else 1
        print()
    else:
        title = args.title
        problem = args.problem or "TODO: Write the problem statement."
        math = args.math or "TODO"
        rust = args.rust or "TODO"
        difficulty = args.difficulty or 1

    create_session(
        directory=directory, name=name, title=title, problem=problem,
        math=math, rust=rust, difficulty=difficulty, stage=args.stage,
    )


def cmd_blank(args):
    """Create a blank self-directed practice folder."""
    directory = resolve_dir(args.dir)
    directory.mkdir(parents=True, exist_ok=True)

    name = args.name
    if not re.match(r"^[a-z0-9_]+$", name):
        print("  ERROR: --name must be lowercase letters, numbers, underscores only.")
        sys.exit(1)

    title = name.replace("_", " ").title()
    create_session(
        directory=directory, name=name, title=title,
        problem="Self-directed practice. Define your own problem here.",
        math="Your choice", rust="Your choice", difficulty=1, stage=0,
    )
    print("  (Blank template - fill in your own problem and concepts)")


def cmd_list(args):
    """List all sessions in a directory."""
    directory = resolve_dir(args.dir)
    if not directory.exists():
        print(f"  Directory not found: {display_path(directory)}")
        return

    sessions = sorted(
        d for d in directory.iterdir() if is_session_dir(d)
    )
    if not sessions:
        print(f"  No sessions found in {display_path(directory)}")
        return

    print(f"\n  Sessions in {display_path(directory)}/\n")
    print(f"  {'Name':<20} {'Title':<50} {'Stage':<6} {'Diff':<5} {'Status'}")
    print(f"  {'-'*20} {'-'*50} {'-'*6} {'-'*5} {'-'*15}")
    for s in sessions:
        info = parse_brief(s / "BRIEF.md")
        print(
            f"  {s.name:<20} {info['title'][:50]:<50} "
            f"{info['stage']:<6} {info['difficulty']:<5} {info['status']}"
        )
    print()


def cmd_doctor(args):
    """Check every session for missing or broken files."""
    directory = resolve_dir(args.dir)
    if not directory.exists():
        print(f"  Directory not found: {display_path(directory)}")
        return

    sessions = sorted(
        d for d in directory.iterdir() if is_session_dir(d)
    )
    if not sessions:
        print(f"  No sessions found in {display_path(directory)}")
        return

    print(f"\n  Health check: {display_path(directory)}/\n")

    all_healthy = True
    for s in sessions:
        issues = []
        for f in REQUIRED_FILES:
            fpath = s / f
            if not fpath.exists():
                issues.append(f"MISSING: {f}")
            elif fpath.stat().st_size == 0:
                issues.append(f"EMPTY: {f}")

        # Check Cargo.toml has valid structure
        cargo = s / "Cargo.toml"
        if cargo.exists() and cargo.stat().st_size > 0:
            cargo_text = cargo.read_text()
            if "[package]" not in cargo_text:
                issues.append("BROKEN: Cargo.toml missing [package] section")

        # Check main.rs has the scaffold structure
        main_rs = s / "src" / "main.rs"
        if main_rs.exists() and main_rs.stat().st_size > 0:
            main_text = main_rs.read_text()
            if "fn main()" not in main_text:
                issues.append("BROKEN: src/main.rs missing fn main()")

        if issues:
            all_healthy = False
            print(f"  {s.name}:")
            for issue in issues:
                print(f"    [!] {issue}")
        else:
            print(f"  {s.name}: OK")

    print()
    if all_healthy:
        print("  All sessions healthy.\n")
    else:
        print("  Issues found. Run 'regenerate' to restore missing template files.\n")


def cmd_regenerate(args):
    """Restore missing template files in existing sessions."""
    # --dir can be relative to repo root or absolute
    if args.dir.startswith("/"):
        directory = Path(args.dir)
    else:
        directory = REPO_ROOT / args.dir

    # Handle --all flag: scan all stage/practice directories in repo
    if args.all:
        dirs_to_check = []
        scan_root = REPO_ROOT
        for d in scan_root.iterdir():
            if d.is_dir() and not d.name.startswith(".") and d.name not in ("docs", "assets", "scripts"):
                if any(is_session_dir(sub) for sub in d.iterdir() if sub.is_dir()):
                    dirs_to_check.append(d)
        # Also handle external test dirs
        if str(directory.parent) != str(REPO_ROOT) and directory.exists():
            dirs_to_check.insert(0, directory.parent)
        if not dirs_to_check:
            print("  No session directories found anywhere in the repo.")
            return
    else:
        dirs_to_check = [directory]

    total_fixed = 0

    for directory in dirs_to_check:
        if not directory.exists():
            if not args.all:
                print(f"  Directory not found: {display_path(directory)}")
            continue

        sessions = sorted(
            d for d in directory.iterdir() if is_session_dir(d)
        )
        if not sessions:
            continue

        for s in sessions:
            # If --session specified, only process that one
            if args.session and s.name != args.session:
                continue

            info = parse_brief(s / "BRIEF.md")
            title = info["title"] if info["title"] != "?" else s.name
            problem = "TODO: Restore problem statement."
            math = "TODO"
            rust = "TODO"
            difficulty = int(info["difficulty"]) if info["difficulty"].isdigit() else 1
            stage = int(info["stage"]) if str(info["stage"]).isdigit() else 1

            # Read existing BRIEF.md to extract problem if it exists
            brief = s / "BRIEF.md"
            if brief.exists() and brief.stat().st_size > 0:
                text = brief.read_text()
                # Try to extract problem from the existing brief
                prob_m = re.search(
                    r"## The Problem\s*\n\n(.+?)(?:\n## |\Z)", text, re.DOTALL
                )
                if prob_m:
                    problem = prob_m.group(1).strip()
                math_m = re.search(r"Math / Physics \| (.+?) \|", text)
                if math_m:
                    math = math_m.group(1).strip()
                rust_m = re.search(r"Rust / Engineering \| (.+?) \|", text)
                if rust_m:
                    rust = rust_m.group(1).strip()

            fixed = []
            for f in REQUIRED_FILES:
                fpath = s / f
                needs_write = False

                if not fpath.exists():
                    needs_write = True
                elif fpath.stat().st_size == 0:
                    needs_write = True
                elif f in USER_EDITABLE:
                    # Don't overwrite user code in main.rs unless --force
                    if not args.force:
                        continue
                    needs_write = True

                # Don't overwrite BRIEF.md if it has content unless --force
                if f == "BRIEF.md" and fpath.exists() and fpath.stat().st_size > 100:
                    if not args.force:
                        continue
                    needs_write = True

                if needs_write:
                    crate_name = s.name.replace("-", "_")
                    d_bars = "|" * difficulty

                    if f == "BRIEF.md":
                        fpath.write_text(
                            BRIEF_TEMPLATE.format(
                                title=title, problem=problem, math=math,
                                rust=rust, d_bars=d_bars, stage=stage,
                            )
                        )
                    elif f == "Cargo.toml":
                        fpath.write_text(
                            CARGO_TEMPLATE.format(crate_name=crate_name)
                        )
                    elif f == "src/main.rs":
                        (s / "src").mkdir(exist_ok=True)
                        fpath.write_text(
                            MAIN_TEMPLATE.format(title=title, math=math, rust=rust)
                        )
                    elif f == ".gitignore":
                        fpath.write_text(GITIGNORE)

                    fixed.append(f)

            if fixed:
                total_fixed += len(fixed)
                print(f"  {s.name}: restored {', '.join(fixed)}")

    if total_fixed == 0:
        print("  Nothing to regenerate. All files present.")
        if not args.force:
            print("  (Use --force to overwrite existing BRIEF.md or main.rs)")
    else:
        print(f"\n  Restored {total_fixed} file(s).")


# ======================================================================
# Main / argparse
# ======================================================================

def main():
    parser = argparse.ArgumentParser(
        description="delta-v session generator and lifecycle manager",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive: creates practice_31 in first_30/
  python scripts/new_session.py new

  # CLI: create a new session with all metadata
  python scripts/new_session.py new \\
    --title "Compute orbital period" \\
    --problem "Given semi-major axis 7000 km, find the period" \\
    --math "Kepler's third law" \\
    --rust "Constants, f64, functions" \\
    --difficulty 3

  # Blank template for self-directed practice
  python scripts/new_session.py blank --name kepler_review

  # Create in a future stage directory
  python scripts/new_session.py new --dir stage_03 --title "Two-body dynamics"

  # Check all sessions for missing files
  python scripts/new_session.py doctor

  # Restore missing files in a specific session
  python scripts/new_session.py regenerate --session practice_05

  # Restore missing files across the entire repo
  python scripts/new_session.py regenerate --all

  # List all sessions
  python scripts/new_session.py list
""",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # --- new ---
    p_new = sub.add_parser("new", help="Create a new numbered practice session")
    p_new.add_argument("--dir", default="first_30", help="Target directory (default: first_30)")
    p_new.add_argument("--title", help="Session title (skip for interactive mode)")
    p_new.add_argument("--problem", help="Problem statement")
    p_new.add_argument("--math", help="Math/physics concepts")
    p_new.add_argument("--rust", help="Rust skills")
    p_new.add_argument("--difficulty", type=int, choices=range(1, 7), help="Difficulty 1-6")
    p_new.add_argument("--stage", type=int, default=1, help="Stage number (default: 1)")
    p_new.add_argument("--no-pad", dest="pad", action="store_false", help="Do not zero-pad the number")
    p_new.set_defaults(func=cmd_new)

    # --- blank ---
    p_blank = sub.add_parser("blank", help="Create a blank self-directed practice folder")
    p_blank.add_argument("--dir", default="first_30", help="Target directory (default: first_30)")
    p_blank.add_argument("--name", required=True, help="Folder name (lowercase, underscores)")
    p_blank.set_defaults(func=cmd_blank)

    # --- list ---
    p_list = sub.add_parser("list", help="List all sessions in a directory")
    p_list.add_argument("--dir", default="first_30", help="Directory to list (default: first_30)")
    p_list.set_defaults(func=cmd_list)

    # --- doctor ---
    p_doc = sub.add_parser("doctor", help="Check every session for missing/broken files")
    p_doc.add_argument("--dir", default="first_30", help="Directory to check (default: first_30)")
    p_doc.set_defaults(func=cmd_doctor)

    # --- regenerate ---
    p_regen = sub.add_parser("regenerate", help="Restore missing template files in existing sessions")
    p_regen.add_argument("--dir", default="first_30", help="Target directory (default: first_30)")
    p_regen.add_argument("--session", help="Only regenerate a specific session (e.g. practice_05)")
    p_regen.add_argument("--all", action="store_true", help="Scan entire repo for sessions to repair")
    p_regen.add_argument("--force", action="store_true", help="Overwrite existing files (destructive!)")
    p_regen.set_defaults(func=cmd_regenerate)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
