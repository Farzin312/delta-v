# Session 05: Own a small vector type

> Mission 1: Equation to Domain Type | Difficulty: || | Status: NOT STARTED
>
> **Repository destination:** `crates/math/src/vec2.rs`

---

## ATTEMPT PAGE

Work through this page BEFORE opening the Debrief Page below.

### Three columns

| Mathematics | Physical Meaning | Rust / Engineering |
|-------------|-----------------|-------------------|
| Coordinate pairs, magnitude, Pythagorean theorem | Displacement has direction and magnitude | Structs, methods, self, references, derive |

---

### Integrated Build

Implement `Vec2` with addition, scaling, norm (magnitude), and safe normalization. Use it to combine 3 m east and 4 m north, compute the resultant, and verify its magnitude is 5 m.

---

### By-Hand Practice

- [ ] Draw 3 m east and 4 m north on graph paper (or sketch). Draw the resultant vector from origin to the endpoint.
- [ ] Compute the magnitude using the Pythagorean theorem: sqrt(3^2 + 4^2) = sqrt(9 + 16) = sqrt(25) = 5
- [ ] State why the zero vector cannot be normalized. What goes wrong mathematically? (Division by zero.)

---

### Prediction Before Code

```
Sign:         (components can be positive or negative; magnitude is always non-negative)
Scale:        (magnitude of (3, 4) is 5 — what scale?)
Direction:    (the resultant of east + north points northeast — about 53 degrees from east)
Units:        (Vec2 components are in meters for displacement; magnitude is in meters)
Failure case: (normalizing the zero vector)
```

Sketch the API:

```
Struct name:     Vec2 { x: f64, y: f64 }
Methods:         new(x, y) -> Vec2
                 add(self, other) -> Vec2
                 scale(self, factor) -> Vec2
                 norm(self) -> f64
                 normalize(self) -> Result<Vec2, ___>
Test names:      1. ___________  2. ___________  3. ___________  4. ___________
```

---

### Independent Rust Drill

Separate from the physics build. From a blank file:

- [ ] Implement a `Point2` struct with x, y fields and methods for distance to another point
- [ ] Implement a `Vec2` with intentionally different API from your Point2 (different method names, different conventions)
- [ ] Derive `Debug`, `Clone`, `Copy`, `PartialEq` on both
- [ ] Write a test that the 3-4-5 triangle has magnitude 5

---

### Tests Written First

```
1. test_3_4_5_vector:          Vec2(3, 4).norm() == 5.0
2. test_zero_norm:             Vec2(0, 0).norm() == 0.0
3. test_addition_identity:     Vec2(3, 4).add(Vec2(0, 0)) == Vec2(3, 4)
4. test_scaling:               Vec2(3, 4).scale(2.0) == Vec2(6, 8)
5. test_zero_normalization:    Vec2(0, 0).normalize() returns Err(___________)
```

---

### Gate: Do Not Open the Debrief Until

- [ ] Hand result exists (drew the vectors and computed magnitude by hand)
- [ ] API is sketched (struct and methods)
- [ ] Tests are named
- [ ] First implementation attempt compiles or has a diagnosed error

---

## DEBRIEF PAGE

### Hint Ladder

**Hint 1.** Operations belong near the type. Put `add`, `scale`, `norm` as methods on Vec2 in an `impl` block, not as free functions.

**Hint 2.** Use `hypot` for the norm. `f64::hypot(y)` computes sqrt(x^2 + y^2) with better numerical properties than naive squaring (avoids overflow for large values).

**Hint 3.** Normalization needs an error path. Dividing by zero magnitude is undefined. Return `Result<Vec2, MathError>` or similar.

---

### Failure Campaign

- [ ] Normalize the zero vector. What happens if you divide by zero without checking? (You get NaN or infinity components.) Your error path should prevent this.

- [ ] Normalize a vector with one huge component (e.g., 1e300, 1e300). Does `hypot` overflow? Compare with `sqrt(x*x + y*y)` — which one survives?

- [ ] Create a Vec2 with NaN components. What is its norm? Can you detect this?

---

### Repository Destination

`Vec2` graduates to `crates/math/src/vec2.rs`. This is the canonical
2-D vector type for the entire workspace. When Session 16 introduces
`Vec3`, it goes in `crates/math/src/vec3.rs` in the same crate.

---

### Python / Independent Check

Plot the component vectors and resultant:

```python
import matplotlib.pyplot as plt

# Components
plt.arrow(0, 0, 3, 0, head_width=0.2, color='blue', label='3m east')
plt.arrow(0, 0, 0, 4, head_width=0.2, color='green', label='4m north')
plt.arrow(0, 0, 3, 4, head_width=0.2, color='red', label='resultant')

# Verify magnitude
import math
print(f"Magnitude: {math.hypot(3, 4)}")  # Should be 5.0
```

---

### Reference Shape

```rust
#[derive(Clone, Copy, Debug, PartialEq)]
struct Vec2 { x: f64, y: f64 }

impl Vec2 {
    fn new(x: f64, y: f64) -> Self { Self { x, y } }
    fn add(self, other: Self) -> Self { Self { x: self.x + other.x, y: self.y + other.y } }
    fn norm(self) -> f64 { self.x.hypot(self.y) }
}
```

---

### Mastery Claim

> "I can explain the ownership choices for Copy versus borrowed vector operations."

Why does Vec2 derive Copy? When would you NOT want Copy? Write in Notes.

---

### Delayed Gate (complete at least ONE WEEK after the session)

- [ ] Recreate Vec2 with all methods from memory
- [ ] Solve a changed case by hand (e.g., 5 m east and 12 m north)
- [ ] Explain why zero normalization fails and why hypot is safer than sqrt(x^2+y^2)
- [ ] Reproduce from clean clone

---

## Session Notes

- **What surprised me:**
- **What I trust:**
- **Where it fails:**
- **What this unlocks:** (Vec2 is the foundation for all 2-D motion, forces, frames)
- **Copy vs borrowed explanation:**
- **Last practiced:** (date)
- **Delayed gate date:** (date + 1 week)
- **Mastery gate passed:** [ ] yes [ ] not yet
