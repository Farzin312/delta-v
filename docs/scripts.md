# delta-v Scripts

Automation tools for managing the delta-v curriculum repository.

Location: `scripts/new_session.py`
Run from: repo root (`cd delta-v`)

---

## Table of Contents

- [Quick Start](#quick-start)
- [Profiles](#profiles)
- [Commands](#commands)
  - [new](#new--create-a-new-session)
  - [blank](#blank--create-a-self-directed-practice-folder)
  - [list](#list--view-all-sessions)
  - [doctor](#doctor--health-check-all-sessions)
  - [regenerate](#regenerate--restore-deleted-template-files)
- [File Lifecycle](#file-lifecycle)
- [The Session Structure](#the-session-structure)
- [Workflows](#workflows)

---

## Quick Start

All commands are run from the repo root:

```bash
cd delta-v
python3 scripts/new_session.py <command> [options]
```

See all commands:

```bash
python3 scripts/new_session.py --help
```

---

## Profiles

The curriculum uses three languages. Each has its own scaffold (build files, source templates, checklist commands). The script auto-detects which profile a session uses based on its files and BRIEF.md header.

| Profile | Scaffold files | Language | Enters at |
|---------|---------------|----------|-----------|
| `rust` (default) | `Cargo.toml`, `src/main.rs` | Rust | Session 01 (first_30) |
| `cpp` | `CMakeLists.txt`, `src/main.cpp` | C++ | Stage 7 (Systems + Embedded) |
| `python` | `pyproject.toml`, `main.py` | Python | Stage 10 (Scientific AI) |

Every session, regardless of profile, gets a `BRIEF.md` with the same 7-step loop. Only the implementation language and checklist commands differ.

**Profile detection (used by `doctor`, `regenerate`, `list`):**

1. Marker file exists? (`Cargo.toml` -> rust, `CMakeLists.txt` -> cpp, `pyproject.toml` -> python)
2. Source file exists? (`src/main.rs`, `src/main.cpp`, `main.py`)
3. BRIEF.md table header? (reads the `{Language} / Engineering` row)
4. Falls back to `rust`

This means regenerate can restore the correct files even if the marker and source files are both deleted - the BRIEF.md alone is enough to identify the profile.

---

## Commands

### `new` - Create a new session

Creates a numbered practice directory with all template files. Auto-increments the number based on what already exists.

**Interactive mode** (recommended for first-time use):

```bash
python3 scripts/new_session.py new
```

You will be prompted for:
- Title (e.g. "Compute orbital period")
- Problem statement
- Math/physics concepts
- Rust skills
- Difficulty (1-6)

**CLI mode** (for scripting or when you know what you want):

```bash
python3 scripts/new_session.py new \
  --title "Compute orbital period" \
  --problem "Given semi-major axis 7000 km, find the orbital period using Kepler's third law." \
  --math "Kepler's third law" \
  --lang "Constants, f64, functions" \
  --difficulty 3
```

**Creating a non-Rust session** (C++ or Python):

```bash
# C++ session (Stage 7+)
python3 scripts/new_session.py new --profile cpp --dir stage_07 \
  --title "FFI bridge" \
  --problem "Call Rust from C via FFI" \
  --math "Linking, ABI" \
  --lang "pointers, extern C" \
  --difficulty 4 --stage 7

# Python session (Stage 10+)
python3 scripts/new_session.py new --profile python --dir stage_10 \
  --title "Orbit fitting" \
  --problem "Fit orbital elements from observations" \
  --math "Least squares, orbit determination" \
  --lang "numpy, scipy.optimize" \
  --difficulty 5 --stage 10
```

**Options:**

| Flag | Default | Description |
|------|---------|-------------|
| `--profile` | `rust` | Language profile: `rust`, `cpp`, or `python` |
| `--dir` | `first_30` | Target directory |
| `--title` | (prompts) | Session title |
| `--problem` | (prompts) | Problem statement |
| `--math` | (prompts) | Math/physics concepts |
| `--lang` | (prompts) | Language/engineering skills |
| `--difficulty` | (prompts) | 1-6 |
| `--stage` | `1` | Stage number |
| `--no-pad` | (padded) | Do not zero-pad (practice_3 instead of practice_03) |

---

### `blank` - Create a self-directed practice folder

Creates a practice folder with a custom name (not numbered). Perfect for review sessions, self-directed practice, or exploring topics outside the standard curriculum.

```bash
python3 scripts/new_session.py blank --name kepler_review
```

Creates `first_30/kepler_review/` with the full template scaffold. The BRIEF.md says "Self-directed practice. Define your own problem here." -- you fill in the rest.

---

### `list` - View all sessions

Shows a table of every session in a directory with title, stage, difficulty, and status.

```bash
python3 scripts/new_session.py list
```

Output:

```
Sessions in first_30/

Name                 Title                                              Stage  Diff  Lang     Status
-------------------- -------------------------------------------------- ------ ----- -------- ---------------
practice_01          Session 01: Make an equation executable            1      1     rust     NOT STARTED
practice_02          Session 02: Turn algebra into a tested function    1      1     rust     IN PROGRESS
practice_03          Session 03: Represent failure honestly             1      1     rust     NOT STARTED
...
```

The `Lang` column is auto-detected from the session's files. For mixed-language directories (future stages), this shows at a glance which sessions are Rust, C++, or Python.

**List a different directory:**

```bash
python3 scripts/new_session.py list --dir stage_03
```

The status field is read from the BRIEF.md `Status:` line. Update it as you progress:

- `NOT STARTED` - haven't begun
- `IN PROGRESS` - working through the steps
- `TESTS PASSING` - implementation done, tests green
- `COMPLETED` - mastery gate passed

---

### `doctor` - Health check all sessions

Scans every session directory and reports missing or broken files.

```bash
python3 scripts/new_session.py doctor
```

Output (healthy):

```
Health check: first_30/

practice_01: OK
practice_02: OK
...
All sessions healthy.
```

Output (problems found):

```
Health check: stage_07/

practice_07_03 (cpp):
  [!] MISSING: CMakeLists.txt
practice_07_05 (rust):
  [!] BROKEN: src/main.rs missing fn main()

Issues found. Run 'regenerate' to restore missing template files.
```

The profile is auto-detected per session, so mixed-language directories work without configuration.

**What doctor checks:** Per-profile validation:

| Profile | Checks |
|---------|--------|
| rust | Cargo.toml has `[package]`; main.rs has `fn main()` |
| cpp | CMakeLists.txt has `project()`; main.cpp has `int main()` |
| python | pyproject.toml has `[project]`; main.py has `__name__` guard |

All profiles also check: every required file exists and is non-empty.

**Check a different directory:**

```bash
python3 scripts/new_session.py doctor --dir stage_03
```

---

### `regenerate` - Restore deleted template files

The safety net. If template files are accidentally deleted, corrupted, or lost to a bad merge, regenerate restores them from the canonical templates.

**Restore a specific session:**

```bash
python3 scripts/new_session.py regenerate --session practice_05
```

**Restore across the entire repo:**

```bash
python3 scripts/new_session.py regenerate --all
```

**Overwrite existing files** (DESTRUCTIVE - use with caution):

```bash
python3 scripts/new_session.py regenerate --all --force
```

**Safety guarantees:**

| File | When regenerate restores it |
|------|---------------------------|
| `BRIEF.md` | Only if missing or empty. Never overwrites a BRIEF with content. |
| `Cargo.toml` / `CMakeLists.txt` / `pyproject.toml` | Only if missing or empty. |
| `src/main.rs` / `src/main.cpp` / `main.py` | Only if missing or empty. Never overwrites code you have written. |
| `.gitignore` | Only if missing. |

The `--force` flag overrides these protections and overwrites everything. Use it only if you want to reset a session back to the blank scaffold.

**How regenerate preserves your data:**

When rebuilding a BRIEF.md, regenerate reads whatever metadata it can find from the existing (broken or partial) BRIEF.md before overwriting. It extracts:
- The problem statement
- Math/physics concepts
- Rust skills
- Difficulty level
- Stage number

This means even a heavily edited BRIEF.md can be restored to its pre-edit state without losing the original problem definition.

---

## File Lifecycle

```
  ┌─────────────┐
  │  new / blank │──── creates ────┐
  └─────────────┘                  │
                                   ▼
                          ┌────────────────┐
                          │  Session dir   │
                          │  BRIEF.md      │
                          │  Cargo.toml    │
                          │  src/main.rs   │
                          │  .gitignore    │
                          └───────┬────────┘
                                  │
                    ┌─────────────┼─────────────┐
                    │             │             │
                    ▼             ▼             ▼
              ┌──────────┐ ┌──────────┐ ┌────────────┐
              │  doctor  │ │   list   │ │ accidental │
              │ (check)  │ │ (view)   │ │ deletion   │
              └────┬─────┘ └──────────┘ └──────┬─────┘
                   │                          │
                   │ reports issues            │
                   ▼                          ▼
              ┌──────────────────────────────────────┐
              │           regenerate                 │
              │  (restore missing/broken files)      │
              └──────────────────────────────────────┘
```

---

## The Session Structure

Every session created by this script follows the same pattern. The 7-step BRIEF.md is always present; the implementation files depend on the profile:

```
practice_NN/
|-- BRIEF.md         The problem, 7-step learning loop, checklist, notes
|
|-- [if profile=rust]
|   |-- Cargo.toml       Independent Cargo project (edition 2024)
|   |-- .gitignore       Ignores /target
|   |-- src/
|       `-- main.rs      Scaffold with PREDICT/DERIVE/IMPLEMENT/TEST sections
|
|-- [if profile=cpp]
|   |-- CMakeLists.txt    CMake build (C++17, -Wall -Wextra -Wpedantic)
|   |-- .gitignore        Ignores /build
|   |-- src/
|       `-- main.cpp      Scaffold with PREDICT/DERIVE/IMPLEMENT/TEST sections
|
|-- [if profile=python]
    |-- pyproject.toml    Project config (pytest + ruff dev deps)
    |-- main.py           Scaffold with PREDICT/DERIVE/IMPLEMENT/TEST sections
    `-- .gitignore        Ignores __pycache__/, .pytest_cache/, etc.
```

The required files for each profile are defined in the `PROFILES` registry at the top of the script. To add a new profile (e.g. a fourth language), add an entry to `PROFILES` with its templates, required files, marker file, and checklist items.

---

## Workflows

### Starting a new curriculum session

```bash
# 1. Create the session
python3 scripts/new_session.py new

# 2. Move into it
cd first_30/practice_31

# 3. Read the brief
cat BRIEF.md

# 4. Follow the 7-step loop (predict, explain, derive, implement, test, falsify, teach)
# 5. Update the status line in BRIEF.md as you progress
```

### Creating a review session for yourself

```bash
python3 scripts/new_session.py blank --name week2_review
cd first_30/week2_review
# Fill in your own problem in BRIEF.md
```

### Adding a session to a future stage

```bash
# Rust session in a later stage
python3 scripts/new_session.py new \
  --dir stage_03 \
  --title "Two-body dynamics" \
  --problem "Implement and propagate a two-body orbit." \
  --math "Newtonian gravitation, ODEs" \
  --lang "Structs, traits, iterators" \
  --difficulty 5 \
  --stage 3

# C++ session (Stage 7+)
python3 scripts/new_session.py new \
  --profile cpp --dir stage_07 \
  --title "F Prime component" \
  --problem "Implement a flight software component" \
  --math "State machines, real-time constraints" \
  --lang "classes, templates, RAII" \
  --difficulty 5 --stage 7

# Python session (Stage 10+)
python3 scripts/new_session.py new \
  --profile python --dir stage_10 \
  --title "Orbit determination" \
  --problem "Estimate orbital elements from radar observations" \
  --math "Nonlinear least squares" \
  --lang "numpy, scipy, jax" \
  --difficulty 5 --stage 10
```

### Recovering from accidental deletion

```bash
# 1. Check what's broken
python3 scripts/new_session.py doctor

# 2. Restore missing files
python3 scripts/new_session.py regenerate --all

# 3. Verify everything is healthy
python3 scripts/new_session.py doctor
```

### Tracking your progress

```bash
# See which sessions are done, in progress, or not started
python3 scripts/new_session.py list
```

Update the status line at the top of each BRIEF.md as you work:

```
> Stage 1 | Difficulty: ||| | Status: IN PROGRESS
```

---

[<- README](../README.md)  |  [<- Documentation Index](INDEX.md)
