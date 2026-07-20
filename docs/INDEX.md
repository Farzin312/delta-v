# Documentation Index

Master navigation for the delta-v curriculum. Start here, go anywhere.

---

## Start Here

| If you are... | Read this first |
|---------------|-----------------|
| **Starting your day** | [Daily Practice Guide](daily_practice.md) - exactly what to do each session |
| **New to the repo** | [README](../README.md) - what this is, who it is for, where it leads |
| **Setting up your environment** | [Setup Guide](setup.md) - install Rust, clone, run your first session |
| **Understanding the method** | [The Method](method.md) - the 7-step loop, AI quarantine, mastery gates |
| **Learning the session format** | [Session Template](session_template.md) - the Attempt Page + Debrief Page structure |
| **Looking for a specific formula** | [Formula Reference](formula_reference.md) - every equation, organized by topic |
| **Wondering what session N teaches** | [Concept Map](concept_map.md) - dependency chain and learning connections |
| **Stuck on the PREDICT step** | [Predict Practice](predict_practice/README.md) - scale estimation guide with examples |
| **Wanting the full curriculum** | [Field Manual](FIELD_MANUAL.md) - the complete markdown companion to the PDF |
| **Tracking knowledge modules** | [Knowledge Tracker](knowledge_tracker.md) - M/P/C/S module progress |

---

## Practice Locations

| Location | What you do | Start here |
|----------|-------------|------------|
| `first_30/` | Sessions: integrated math + physics + Rust builds | [CATALOG.md](../first_30/CATALOG.md) |
| `drills/` | Rust language fluency drills (blank-file practice) | [Drills README](../drills/README.md) |
| `diagnostics/` | Readiness assessments before new modules | [Diagnostics README](../diagnostics/README.md) |
| `crates/` | Graduated concepts (migrate here after mastery) | [Architecture](FIELD_MANUAL.md#14-repository-transformation-plan) |
| `docs/learning-log/` | Your daily engineering notebook | Create a dated file |

---

## The Learning System

### Core Methodology
- **[The Method](method.md)** - The complete operating system: 7-step loop, dependency rule, AI quarantine protocol, mastery gates, engineering log, question ladder, review cadence, reduction hierarchy, field checklists. Read before Session 01, refer back constantly.

### Curriculum
- **[Full Curriculum](curriculum.md)** - All 104 units across 13 stages, from high-school algebra to mission-grade space systems. Portfolio evidence ladder and competitive positioning.

### Session Guide
- **[Session Catalog](../first_30/CATALOG.md)** - Session-by-session index with difficulty ratings and status tracking for the first 30 sessions.

---

## Reference Materials

### Formula Reference
**[Formula Reference](formula_reference.md)** - Every equation from all 30 sessions, organized by topic:
- Units and constants
- Algebra, trigonometry, vectors
- Calculus (derivatives, integrals)
- Kinematics, forces, energy
- Gravitation and orbits
- Numerical methods (Euler, midpoint, convergence)
- Floating point comparison
- Quick lookup table: formula by session number

### Concept Map
**[Concept Map](concept_map.md)** - Dependency chain showing what each session teaches and what it unlocks:
- Per-session: math concept, Rust concept, what it unlocks next
- Dependency chains for integration, vectors, error handling, physics
- Mastery checkpoints after each session group

### PREDICT Practice
**[Predict Practice Workbook](predict_practice/README.md)** - Mastering Step 1 of the 7-step loop:
- [Example 1: Dropping a Rock](predict_practice/example_01_cliff_drop.md) - 1D kinematics, constant gravity
- [Example 2: Braking Car](predict_practice/example_02_braking_car.md) - Deceleration, quadratic scaling
- [Example 3: Satellite Orbit](predict_practice/example_03_satellite_orbit.md) - Circular motion, planetary scale
- [Practice Exercises](predict_practice/practice_exercises.md) - 4 scenarios with solutions

---

## Tools and Setup

### Setup
**[Setup Guide](setup.md)** - Install Rust, format/lint tools, clone and run, engineering log template, tools needed for later stages.

### Session Generator
**[Scripts Guide](scripts.md)** - The `new_session.py` lifecycle manager:
- `new` - Create a numbered practice session (interactive or CLI)
- `blank` - Create a self-directed practice folder
- `list` - View all sessions with status
- `doctor` - Health check all sessions for missing/broken files
- `regenerate` - Restore accidentally deleted template files
- Supports Rust (default), C++ (Stage 7+), and Python (Stage 10+) profiles

---

## Quick Links

### Most Used Commands
```bash
# Start your day
# 1. Read docs/daily_practice.md
# 2. Open first_30/CATALOG.md to find your current session
# 3. Open the session's BRIEF.md and follow the Attempt Page

# Work on a session
cd first_30/practice_01
cat BRIEF.md
cargo run
cargo test

# Quality checks (run before finishing every session)
cargo fmt
cargo clippy -- -D warnings
cargo test

# Check the workspace crates (separate from sessions)
cargo check --workspace
cargo test --workspace

# Manage sessions
python3 scripts/new_session.py list           # see all sessions
python3 scripts/new_session.py doctor          # check for problems
python3 scripts/new_session.py new             # create a new session
python3 scripts/new_session.py regenerate --all  # fix broken sessions

# Python validation
cd python && pip install -e '.[dev]' && pytest -v
```

### Most Used Formulas
```
Distance:         d = v * t
Average speed:    v = d / t
Position:         x(t) = x0 + v0*t + 0.5*a*t^2
Velocity:         v(t) = v0 + a*t
Newton's 2nd:     F = m * a
Gravity:          a = mu / r^2
Circular speed:   v = sqrt(mu / r)
Orbital energy:   epsilon = v^2/2 - mu/r
Euler step:       y_next = y + h * f(t, y)
Float compare:    |a - b| <= eps_abs + eps_rel * max(|a|, |b|)
```

### Documentation File Map
```
delta-v/
|-- README.md                         What this is and how to start
|-- docs/
|   |-- INDEX.md                      <-- YOU ARE HERE
|   |-- curriculum.md                 Full 104-unit, 13-stage map
|   |-- method.md                     The 7-step loop and methodology
|   |-- formula_reference.md          Every equation, by topic
|   |-- concept_map.md                Dependency chain, what each session teaches
|   |-- setup.md                      Environment setup and first run
|   |-- scripts.md                    Session generator documentation
|   |-- predict_practice/
|       |-- README.md                 Scale estimation guide
|       |-- example_01_cliff_drop.md  Walkthrough: falling rock
|       |-- example_02_braking_car.md Walkthrough: braking car
|       |-- example_03_satellite.md   Walkthrough: orbital period
|       |-- practice_exercises.md     4 practice scenarios + solutions
|-- first_30/
|   |-- CATALOG.md                    Session index with status tracking
|   |-- practice_01/ .. practice_30/  The 30 sessions
|-- scripts/
|   |-- new_session.py                Session lifecycle manager
```

---

## How This Will Grow

As the curriculum expands beyond the first 30 sessions:

1. **New stages** (stage_03/, stage_04/, ...) follow the same `practice_NN/BRIEF.md + Cargo.toml + src/` pattern.
2. **New formula reference sections** get added to `formula_reference.md` as new physics is introduced (orbital mechanics, controls, estimation, etc.).
3. **New concept map sections** get added for each new stage's dependency chain.
4. **This INDEX.md** gets new rows in the session guide section as stages are added.
5. **The session generator** (`new_session.py`) already supports creating sessions in new stage directories with `--dir stage_NN` and language profiles for C++ and Python.

The structure is designed to scale from 30 sessions to 104 units without reorganization.

---

[<- Back to README](../README.md)
