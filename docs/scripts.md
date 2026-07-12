# delta-v Scripts

Automation tools for managing the delta-v curriculum repository.

Location: `scripts/new_session.py`
Run from: repo root (`cd delta-v`)

---

## Table of Contents

- [Quick Start](#quick-start)
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
  --rust "Constants, f64, functions" \
  --difficulty 3
```

**Options:**

| Flag | Default | Description |
|------|---------|-------------|
| `--dir` | `first_30` | Target directory |
| `--title` | (prompts) | Session title |
| `--problem` | (prompts) | Problem statement |
| `--math` | (prompts) | Math/physics concepts |
| `--rust` | (prompts) | Rust skills |
| `--difficulty` | (prompts) | 1-6 |
| `--stage` | `1` | Stage number |
| `--no-pad` | (padded) | Do not zero-pad (practice_3 instead of practice_03) |

**Creating sessions in a future stage directory:**

```bash
python3 scripts/new_session.py new --dir stage_03 --title "Two-body dynamics" --problem "..."
```

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

Name                 Title                                              Stage  Diff  Status
-------------------- -------------------------------------------------- ------ ----- ---------------
practice_01          Session 01: Make an equation executable            1      1     NOT STARTED
practice_02          Session 02: Turn algebra into a tested function    1      1     IN PROGRESS
practice_03          Session 03: Represent failure honestly             1      1     NOT STARTED
...
```

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
Health check: first_30/

practice_05:
  [!] MISSING: BRIEF.md
  [!] MISSING: Cargo.toml
practice_12:
  [!] BROKEN: src/main.rs missing fn main()

Issues found. Run 'regenerate' to restore missing template files.
```

**What doctor checks:**

| Check | What it looks for |
|-------|-------------------|
| MISSING | File does not exist at all |
| EMPTY | File exists but is 0 bytes |
| BROKEN | Cargo.toml missing `[package]` section |
| BROKEN | src/main.rs missing `fn main()` |

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
| `Cargo.toml` | Only if missing or empty. |
| `src/main.rs` | Only if missing or empty. Never overwrites code you have written. |
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

Every session created by this script follows the same pattern:

```
practice_NN/
├── BRIEF.md      The problem, 7-step learning loop, checklist, notes
├── Cargo.toml    Independent Cargo project (edition 2024)
├── .gitignore    Ignores /target
└── src/
    └── main.rs   Scaffold with PREDICT/DERIVE/IMPLEMENT/TEST sections
```

The four required files are defined in `REQUIRED_FILES` at the top of the script. If you ever need to change what files a session contains (e.g. add a `tests/` directory), update that list and the template functions.

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
python3 scripts/new_session.py new \
  --dir stage_03 \
  --title "Two-body dynamics" \
  --problem "Implement and propagate a two-body orbit." \
  --math "Newtonian gravitation, ODEs" \
  --rust "Structs, traits, iterators" \
  --difficulty 5 \
  --stage 3
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

[<- README](../README.md)
