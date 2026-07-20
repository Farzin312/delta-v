# M1 Diagnostic: Algebra and Functions

> No notes. No AI. Calculator allowed for arithmetic only (not for solving).
> Time: 20 minutes. 20 questions.

Tests algebraic manipulation needed for physics and numerical code.
If you score below 65%, repair the failed nodes before Sessions 02-05.

---

## Questions

### Rearranging Equations (5 questions)

1. Rearrange d = v x t to solve for v.
2. Rearrange d = v x t to solve for t.
3. Rearrange F = m x a to solve for m.
4. Rearrange E = 1/2 x m x v^2 to solve for v.
5. Rearrange a = (v_f - v_0) / t to solve for v_f.

### Inverse Functions (4 questions)

6. If f(x) = 2x + 3, what is f^-1(x)?
7. If f(x) = x^2 (for x >= 0), what is f^-1(x)?
8. If you compute speed from (d, t), then compute distance from (speed, t),
   do you recover d? Prove it algebraically.
9. If f(x) = 3x - 1 and g(x) = (x + 1)/3, is g the inverse of f? Prove it.

### Inequalities and Domains (4 questions)

10. For what values of t is d/t defined? (mathematical domain)
11. For what values of t does d/t make physical sense for elapsed time? (physical domain)
12. Solve: 2x - 5 > 3. Express the solution set.
13. Is -0.0 a valid input for v = d/t? What about the physical domain?

### Exponents and Logarithms (4 questions)

14. Simplify: x^3 x x^4
15. Simplify: (x^2)^3
16. Compute: log_10(1000)
17. If a^b = c, express b in terms of a and c using logarithms.

### Composition and Asymptotics (3 questions)

18. If f(x) = x^2 and g(x) = x + 1, compute f(g(2)).
19. What happens to 1/x as x approaches infinity? As x approaches 0+?
20. For large n, which grows faster: n^2 or 2^n? Why does this matter in computing?

---

## Scoring

| Score | Interpretation |
|-------|---------------|
| 18-20 correct (90-100%) | Strong algebra foundation. Proceed. |
| 15-17 correct (75-85%) | Good. Review the failed categories. |
| 12-14 correct (60-70%) | Repair needed. Focus on the weak categories. |
| Below 12 (below 65%) | PAUSE. Repair algebra before proceeding. |

### Answer Key

1. v = d/t
2. t = d/v
3. m = F/a
4. v = sqrt(2E/m)
5. v_f = v_0 + a x t
6. f^-1(x) = (x - 3)/2
7. f^-1(x) = sqrt(x)
8. Yes. speed = d/t. distance = speed x t = (d/t) x t = d. QED.
9. Yes. f(g(x)) = 3((x+1)/3) - 1 = x + 1 - 1 = x. QED.
10. t != 0 (all real numbers except zero)
11. t > 0 (positive, real, finite time only)
12. x > 4 (2x > 8, x > 4)
13. Mathematically yes (-0.0 is a valid IEEE-754 value). Physically, zero elapsed
    time is a degenerate case.
14. x^7
15. x^6
16. 3 (because 10^3 = 1000)
17. b = log_a(c)
18. f(g(2)) = f(3) = 9
19. As x -> inf: 1/x -> 0. As x -> 0+: 1/x -> +infinity.
20. 2^n grows faster. n^2 is polynomial, 2^n is exponential. Exponential
    growth always dominates polynomial for large n. This matters because
    algorithm complexity (O(n^2) vs O(2^n)) determines whether code scales.

---

## Score: ____ / 20

Record in the Diagnostic Log in diagnostics/README.md.
