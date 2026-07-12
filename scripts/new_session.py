#!/usr/bin/env python3
"""
delta-v session generator and lifecycle manager

Creates practice session directories with the standard structure:
  - BRIEF.md           (7-step loop template, optionally blank)
  - Language files     (depends on profile: Rust / C++ / Python)
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

  python scripts/new_session.py new \
    --title "Compute orbital period" \
    --problem "Given semi-major axis 7000 km, find the period" \
    --math "Kepler's third law" \
    --lang "Constants, f64, functions" \
    --difficulty 3

  python scripts/new_session.py new --profile cpp --dir stage_07 \
    --title "FFI bridge" --problem "Call Rust from C via FFI"

  python scripts/new_session.py blank --name orbital_review

  python scripts/new_session.py doctor

  python scripts/new_session.py regenerate --dir first_30 --session practice_05
  python scripts/new_session.py regenerate --all
"""

import argparse
import os
import sys
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


# ======================================================================
# Profile definitions
# ======================================================================
#
# Each profile defines:
#   lang_name       -- display name ("Rust", "C++", "Python")
#   required_files  -- files every session of this profile must have
#   user_editable   -- files regenerate will NOT overwrite without --force
#   marker_file     -- file whose presence identifies this profile
#   source_file     -- the primary source code path
#   gitignore       -- .gitignore content
#   io_example      -- the I/O call to avoid in pure functions
#   checklist_items -- language-specific lines for the BRIEF checklist
#   templates       -- dict: filename -> template string (with .format fields)
#
# Templates use Python .format(). Literal braces in code must be doubled ({{ }}).

PROFILES = {}
PROFILE_NAMES = ["rust", "cpp", "python"]
PROFILE_DEFAULT = "rust"


# --- BRIEF template (shared across profiles, parameterized) -------------

_BRIEF_TEMPLATE = """# {title}

> Stage {stage} | Difficulty: {d_bars} | Status: NOT STARTED

## The Problem

{problem}

## What This Teaches

| Dimension | Focus |
|-----------|-------|
| Math / Physics | {math} |
| {lang_name} / Engineering | {lang} |

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

Write the smallest pure {lang_name} function that matches your derivation.

Rules:
- One concept per function
- No hidden I/O (no {io_example} inside a pure math function)
- No premature abstraction (no framework, no complex type hierarchy)
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
{checklist_items}
- [ ] At least one known-value test passes
- [ ] At least one boundary test passes
- [ ] At least one property or independent-reference test
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


def _register_profile(
    name, lang_name, required_files, user_editable, marker_file,
    source_file, gitignore, io_example, checklist_items, templates,
):
    PROFILES[name] = {
        "lang_name": lang_name,
        "required_files": required_files,
        "user_editable": user_editable,
        "marker_file": marker_file,
        "source_file": source_file,
        "gitignore": gitignore,
        "io_example": io_example,
        "checklist_items": checklist_items,
        "templates": templates,
    }


# --- Rust profile -------------------------------------------------------

_RUST_BRIEF_ITEMS = """- [ ] Implementation compiles with `cargo build`
- [ ] `cargo fmt` clean
- [ ] `cargo clippy -- -D warnings` clean"""

_RUST_MAIN = """//! {title}
//! {math}
//!
//! Rust skills: {lang}
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

_RUST_CARGO = """[package]
name = "{crate_name}"
version = "0.1.0"
edition = "2024"

[dependencies]
"""

_register_profile(
    name="rust",
    lang_name="Rust",
    required_files=["BRIEF.md", "Cargo.toml", "src/main.rs", ".gitignore"],
    user_editable={"src/main.rs"},
    marker_file="Cargo.toml",
    source_file="src/main.rs",
    gitignore="/target\n",
    io_example="`println!`",
    checklist_items=_RUST_BRIEF_ITEMS,
    templates={
        "Cargo.toml": _RUST_CARGO,
        "src/main.rs": _RUST_MAIN,
    },
)


# --- C++ profile --------------------------------------------------------

_CPP_BRIEF_ITEMS = """- [ ] Implementation compiles with `cmake --build build`
- [ ] `clang-format` clean
- [ ] No compiler warnings (`-Wall -Wextra -Wpedantic`)"""

_CPP_MAIN = """//! {title}
//! {math}
//!
//! C++ skills: {lang}
//!
//! TODO: Implement the solution following the 7-step loop.
//! 1. PREDICT - write your prediction as a comment below
//! 2. EXPLAIN - draw/narrate the physical story
//! 3. DERIVE - write the equation with dimensional checks
//! 4. IMPLEMENT - replace the TODO with your code
//! 5. TEST - run tests with assertions or GoogleTest
//! 6. FALSIFY - find where it breaks
//! 7. TEACH - write what you learned in the BRIEF.md notes

#include <cmath>
#include <cassert>
#include <iostream>

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
// Write your functions here.

// === TESTS ===
// Use assert() for simple checks. For larger test suites, consider GoogleTest.
// Example:
// void test_known_value() {{
//     // assert(actual == expected);
// }}

int main() {{
    std::cout << "{title}" << std::endl;
    std::cout << "Implement the functions above, then fill in main()." << std::endl;

    // Run tests
    // test_known_value();

    return 0;
}}
"""

_CPP_CMAKE = """cmake_minimum_required(VERSION 3.16)
project({crate_name} CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

add_executable({crate_name} src/main.cpp)

target_compile_options({crate_name} PRIVATE -Wall -Wextra -Wpedantic)
"""

_register_profile(
    name="cpp",
    lang_name="C++",
    required_files=["BRIEF.md", "CMakeLists.txt", "src/main.cpp", ".gitignore"],
    user_editable={"src/main.cpp"},
    marker_file="CMakeLists.txt",
    source_file="src/main.cpp",
    gitignore="/build\n",
    io_example="`std::cout`",
    checklist_items=_CPP_BRIEF_ITEMS,
    templates={
        "CMakeLists.txt": _CPP_CMAKE,
        "src/main.cpp": _CPP_MAIN,
    },
)


# --- Python profile -----------------------------------------------------

_PY_BRIEF_ITEMS = """- [ ] Implementation runs without errors (`python main.py`)
- [ ] `ruff format` clean
- [ ] `ruff check` clean
- [ ] `pytest` passes"""

_PY_MAIN = '''"""{title}

{math}

Python skills: {lang}

TODO: Implement the solution following the 7-step loop.
1. PREDICT - write your prediction as a comment below
2. EXPLAIN - draw/narrate the physical story
3. DERIVE - write the equation with dimensional checks
4. IMPLEMENT - replace the TODO with your code
5. TEST - run tests with `pytest`
6. FALSIFY - find where it breaks
7. TEACH - write what you learned in the BRIEF.md notes
"""

# === PREDICTION ===
# Write your prediction here before coding:
# Sign:
# Scale:
# Direction:
# Expected failure case:

# === DERIVATION ===
# Equation:
# Dimensional check:
# Limiting cases:

# === IMPLEMENTATION ===
# Write your functions here.

# === TESTS ===
# Write your tests here. Run with: pytest main.py
# import pytest
#
# def test_known_value():
#     ...

if __name__ == "__main__":
    print("{title}")
    print("Implement the functions above, then fill in main().")
'''

_PY_PROJECT = """[project]
name = "{crate_name}"
version = "0.1.0"
requires-python = ">=3.10"
dependencies = []

[project.optional-dependencies]
dev = ["pytest", "ruff"]

[tool.pytest.ini_options]
testpaths = ["."]
"""

_register_profile(
    name="python",
    lang_name="Python",
    required_files=["BRIEF.md", "pyproject.toml", "main.py", ".gitignore"],
    user_editable={"main.py"},
    marker_file="pyproject.toml",
    source_file="main.py",
    gitignore="__pycache__/\n*.pyc\n.pytest_cache/\n*.egg-info/\n.venv/\n",
    io_example="`print()`",
    checklist_items=_PY_BRIEF_ITEMS,
    templates={
        "pyproject.toml": _PY_PROJECT,
        "main.py": _PY_MAIN,
    },
)


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
    A session has any profile marker file OR matches practice_/unit_ naming."""
    if not path.is_dir():
        return False
    for pname in PROFILE_NAMES:
        marker = PROFILES[pname]["marker_file"]
        if (path / marker).exists():
            return True
    if (path / "BRIEF.md").exists():
        return True
    if re.match(r"(?:practice|unit)_\d+", path.name):
        return True
    return False


def detect_profile(session_dir: Path) -> str:
    """Auto-detect which profile a session directory uses.
    Checks marker files first, then BRIEF.md table header, then source files.
    Falls back to 'rust' if none found."""
    # 1. Check marker files
    for pname in PROFILE_NAMES:
        marker = PROFILES[pname]["marker_file"]
        if (session_dir / marker).exists():
            return pname
    # 2. Check source files
    for pname in PROFILE_NAMES:
        src = PROFILES[pname]["source_file"]
        if (session_dir / src).exists():
            return pname
    # 3. Check BRIEF.md table header for language name
    brief = session_dir / "BRIEF.md"
    if brief.exists() and brief.stat().st_size > 0:
        text = brief.read_text()
        for pname in PROFILE_NAMES:
            ln = PROFILES[pname]["lang_name"]
            if f"{ln} / Engineering" in text:
                return pname
    return PROFILE_DEFAULT


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


def extract_brief_field(text: str, label: str) -> str:
    """Extract a concept field from a BRIEF.md table row.
    label examples: 'Math / Physics', 'Rust / Engineering',
    'C++ / Engineering', 'Python / Engineering'
    """
    # Match: | <label> | <value> |
    pattern = rf"\| {re.escape(label)} \| (.+?) \|"
    m = re.search(pattern, text)
    if m:
        return m.group(1).strip()
    return "TODO"


# ======================================================================
# Core creation logic
# ======================================================================

def write_session_files(
    session_dir: Path,
    profile: str,
    title: str,
    problem: str,
    math: str,
    lang: str,
    difficulty: int,
    stage: int,
    crate_name: str = "",
):
    """Write all template files into a session directory."""
    p = PROFILES[profile]
    session_dir.mkdir(parents=True, exist_ok=True)

    if not crate_name:
        crate_name = session_dir.name.replace("-", "_")

    d_bars = "|" * difficulty

    # BRIEF.md (shared template, profile-parameterized)
    (session_dir / "BRIEF.md").write_text(
        _BRIEF_TEMPLATE.format(
            title=title, problem=problem, math=math, lang=lang,
            d_bars=d_bars, stage=stage,
            lang_name=p["lang_name"], io_example=p["io_example"],
            checklist_items=p["checklist_items"],
        )
    )

    # .gitignore
    (session_dir / ".gitignore").write_text(p["gitignore"])

    # Profile-specific files
    for fname, template in p["templates"].items():
        fpath = session_dir / fname
        fpath.parent.mkdir(parents=True, exist_ok=True)
        fpath.write_text(template.format(
            title=title, math=math, lang=lang, crate_name=crate_name,
        ))


def create_session(
    directory: Path,
    name: str,
    profile: str,
    title: str,
    problem: str,
    math: str,
    lang: str,
    difficulty: int,
    stage: int = 1,
):
    """Create a full session directory with all files."""
    session_dir = directory / name
    if session_dir.exists():
        print(f"  ERROR: {display_path(session_dir)} already exists.")
        sys.exit(1)

    write_session_files(
        session_dir, profile, title, problem, math, lang, difficulty, stage
    )

    p = PROFILES[profile]
    print(f"\n  Created: {display_path(session_dir)}/")
    print(f"    BRIEF.md          (7-step loop, checklist, notes)")
    for fname in p["required_files"]:
        if fname in ("BRIEF.md", ".gitignore"):
            continue
        print(f"    {fname:<18} ({profile} scaffold)")
    print(f"    .gitignore")
    print(f"\n  Profile: {profile} ({p['lang_name']})")
    print(f"  Next: cd {session_dir} && {('cargo run' if profile == 'rust' else ('cmake -B build && cmake --build build && ./build/' + name if profile == 'cpp' else 'python main.py'))}")


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
        print(f"\n  Creating session {name} in {args.dir}/ (profile: {args.profile})\n")
        title = input("  Title (e.g. 'Compute orbital period'): ").strip()
        if not title:
            print("  Title is required. Aborting.")
            sys.exit(1)
        problem = input("  Problem statement: ").strip()
        if not problem:
            print("  Problem is required. Aborting.")
            sys.exit(1)
        math = input("  Math/physics concepts: ").strip() or "TODO"
        lang = input(f"  {PROFILES[args.profile]['lang_name']} skills: ").strip() or "TODO"
        difficulty_str = input("  Difficulty (1-6) [1]: ").strip() or "1"
        difficulty = int(difficulty_str) if difficulty_str.isdigit() else 1
        print()
    else:
        title = args.title
        problem = args.problem or "TODO: Write the problem statement."
        math = args.math or "TODO"
        lang = args.lang or "TODO"
        difficulty = args.difficulty or 1

    create_session(
        directory=directory, name=name, profile=args.profile, title=title,
        problem=problem, math=math, lang=lang, difficulty=difficulty,
        stage=args.stage,
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
        directory=directory, name=name, profile=args.profile, title=title,
        problem="Self-directed practice. Define your own problem here.",
        math="Your choice", lang="Your choice", difficulty=1, stage=0,
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
    print(f"  {'Name':<20} {'Title':<50} {'Stage':<6} {'Diff':<5} {'Lang':<8} {'Status'}")
    print(f"  {'-'*20} {'-'*50} {'-'*6} {'-'*5} {'-'*8} {'-'*15}")
    for s in sessions:
        info = parse_brief(s / "BRIEF.md")
        lang = detect_profile(s)
        print(
            f"  {s.name:<20} {info['title'][:50]:<50} "
            f"{info['stage']:<6} {info['difficulty']:<5} {lang:<8} {info['status']}"
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
        profile = detect_profile(s)
        p = PROFILES[profile]
        issues = []

        for f in p["required_files"]:
            fpath = s / f
            if not fpath.exists():
                issues.append(f"MISSING: {f}")
            elif fpath.stat().st_size == 0:
                issues.append(f"EMPTY: {f}")

        # Check marker file has valid structure
        marker = s / p["marker_file"]
        if marker.exists() and marker.stat().st_size > 0:
            marker_text = marker.read_text()
            if profile == "rust":
                if "[package]" not in marker_text:
                    issues.append("BROKEN: Cargo.toml missing [package] section")
            elif profile == "cpp":
                if "project(" not in marker_text:
                    issues.append("BROKEN: CMakeLists.txt missing project()")
            elif profile == "python":
                if "[project]" not in marker_text:
                    issues.append("BROKEN: pyproject.toml missing [project] section")

        # Check source file has entry point
        src = s / p["source_file"]
        if src.exists() and src.stat().st_size > 0:
            src_text = src.read_text()
            if profile == "rust":
                if "fn main()" not in src_text:
                    issues.append("BROKEN: src/main.rs missing fn main()")
            elif profile == "cpp":
                if "int main()" not in src_text:
                    issues.append("BROKEN: src/main.cpp missing int main()")
            elif profile == "python":
                if "__name__" not in src_text:
                    issues.append("BROKEN: main.py missing __name__ guard")

        if issues:
            all_healthy = False
            print(f"  {s.name} ({profile}):")
            for issue in issues:
                print(f"    [!] {issue}")
        else:
            print(f"  {s.name} ({profile}): OK")

    print()
    if all_healthy:
        print("  All sessions healthy.\n")
    else:
        print("  Issues found. Run 'regenerate' to restore missing template files.\n")


def cmd_regenerate(args):
    """Restore missing template files in existing sessions."""
    # Handle --all flag: scan all stage/practice directories in repo
    if args.all:
        dirs_to_check = []
        scan_root = REPO_ROOT
        for d in scan_root.iterdir():
            if d.is_dir() and not d.name.startswith(".") and d.name not in ("docs", "assets", "scripts"):
                if any(is_session_dir(sub) for sub in d.iterdir() if sub.is_dir()):
                    dirs_to_check.append(d)
        if not dirs_to_check:
            print("  No session directories found anywhere in the repo.")
            return
    else:
        directory = resolve_dir(args.dir)
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

            profile = detect_profile(s)
            p = PROFILES[profile]

            info = parse_brief(s / "BRIEF.md")
            title = info["title"] if info["title"] != "?" else s.name
            difficulty = int(info["difficulty"]) if info["difficulty"].isdigit() else 1
            stage = int(info["stage"]) if str(info["stage"]).isdigit() else 1

            # Read existing BRIEF.md to extract metadata if present
            brief = s / "BRIEF.md"
            problem = "TODO: Restore problem statement."
            math = "TODO"
            lang = "TODO"

            if brief.exists() and brief.stat().st_size > 0:
                text = brief.read_text()
                prob_m = re.search(
                    r"## The Problem\s*\n\n(.+?)(?:\n## |\Z)", text, re.DOTALL
                )
                if prob_m:
                    problem = prob_m.group(1).strip()
                math = extract_brief_field(text, "Math / Physics")
                # Try each profile's lang_name for the engineering column
                for pname in PROFILE_NAMES:
                    ln = PROFILES[pname]["lang_name"]
                    val = extract_brief_field(text, f"{ln} / Engineering")
                    if val != "TODO":
                        lang = val
                        break

            crate_name = s.name.replace("-", "_")
            d_bars = "|" * difficulty

            fixed = []
            for f in p["required_files"]:
                fpath = s / f
                needs_write = False

                if not fpath.exists():
                    needs_write = True
                elif fpath.stat().st_size == 0:
                    needs_write = True
                elif f in p["user_editable"]:
                    if not args.force:
                        continue
                    needs_write = True

                # Don't overwrite BRIEF.md if it has content unless --force
                if f == "BRIEF.md" and fpath.exists() and fpath.stat().st_size > 100:
                    if not args.force:
                        continue
                    needs_write = True

                if needs_write:
                    if f == "BRIEF.md":
                        fpath.write_text(
                            _BRIEF_TEMPLATE.format(
                                title=title, problem=problem, math=math,
                                lang=lang, d_bars=d_bars, stage=stage,
                                lang_name=p["lang_name"],
                                io_example=p["io_example"],
                                checklist_items=p["checklist_items"],
                            )
                        )
                    elif f == ".gitignore":
                        fpath.write_text(p["gitignore"])
                    elif f in p["templates"]:
                        fpath.parent.mkdir(parents=True, exist_ok=True)
                        fpath.write_text(
                            p["templates"][f].format(
                                title=title, math=math, lang=lang,
                                crate_name=crate_name,
                            )
                        )

                    fixed.append(f)

            if fixed:
                total_fixed += len(fixed)
                print(f"  {s.name} ({profile}): restored {', '.join(fixed)}")

    if total_fixed == 0:
        print("  Nothing to regenerate. All files present.")
        if not args.force:
            print("  (Use --force to overwrite existing BRIEF.md or source files)")
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
Profiles:
  rust      Cargo.toml + src/main.rs      (default, used by first_30)
  cpp       CMakeLists.txt + src/main.cpp (Stage 7+: Systems + Embedded)
  python    pyproject.toml + main.py      (Stage 10+: Scientific AI)

Examples:
  # Interactive: creates practice_31 in first_30/ (Rust profile)
  python scripts/new_session.py new

  # CLI: create a new Rust session with all metadata
  python scripts/new_session.py new \\
    --title "Compute orbital period" \\
    --problem "Given semi-major axis 7000 km, find the period" \\
    --math "Kepler's third law" \\
    --lang "Constants, f64, functions" \\
    --difficulty 3

  # Create a C++ session in a future stage
  python scripts/new_session.py new --profile cpp --dir stage_07 \\
    --title "FFI bridge" --problem "Call Rust from C via FFI"

  # Create a Python session
  python scripts/new_session.py new --profile python --dir stage_10 \\
    --title "Orbit fitting" --problem "Fit orbital elements from observations"

  # Blank template for self-directed practice
  python scripts/new_session.py blank --name kepler_review

  # Check all sessions for missing files
  python scripts/new_session.py doctor

  # Restore missing files in a specific session
  python scripts/new_session.py regenerate --session practice_05

  # Restore missing files across the entire repo
  python scripts/new_session.py regenerate --all

  # List all sessions (shows auto-detected language)
  python scripts/new_session.py list
""",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # --- new ---
    p_new = sub.add_parser("new", help="Create a new numbered practice session")
    p_new.add_argument("--profile", choices=PROFILE_NAMES, default=PROFILE_DEFAULT,
                       help="Language profile (default: rust)")
    p_new.add_argument("--dir", default="first_30", help="Target directory (default: first_30)")
    p_new.add_argument("--title", help="Session title (skip for interactive mode)")
    p_new.add_argument("--problem", help="Problem statement")
    p_new.add_argument("--math", help="Math/physics concepts")
    p_new.add_argument("--lang", help="Language/engineering skills")
    p_new.add_argument("--difficulty", type=int, choices=range(1, 7), help="Difficulty 1-6")
    p_new.add_argument("--stage", type=int, default=1, help="Stage number (default: 1)")
    p_new.add_argument("--no-pad", dest="pad", action="store_false", help="Do not zero-pad the number")
    p_new.set_defaults(func=cmd_new)

    # --- blank ---
    p_blank = sub.add_parser("blank", help="Create a blank self-directed practice folder")
    p_blank.add_argument("--profile", choices=PROFILE_NAMES, default=PROFILE_DEFAULT,
                         help="Language profile (default: rust)")
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
