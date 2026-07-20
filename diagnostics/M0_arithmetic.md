# M0 Diagnostic: Arithmetic Foundations

> No notes. No AI. No calculator. Pencil and paper only.
> Time: 15 minutes. 25 questions.

This tests the arithmetic foundation that ALL of mathematics depends on.
If you score below 65%, repair the failed nodes before starting Session 01.

---

## Questions

### Scientific Notation (5 questions)

1. Write 299,792,458 in scientific notation.
2. Write 0.0000125 in scientific notation.
3. Compute: (3.0 x 10^8) x (1.25 x 10^-2). Express in scientific notation.
4. Convert 12.5 milliseconds to seconds. Express as a decimal.
5. How many milliseconds are in 2.5 seconds?

### Unit Conversion (5 questions)

6. Convert 3,747,405 meters to kilometers.
7. Convert 0.5 hours to seconds.
8. Convert 5000 grams to kilograms.
9. If speed is 10 m/s, what is it in km/h?
10. Convert 1 Megawatt to Watts.

### Fractions and Decimals (5 questions)

11. Compute: 3/4 + 1/6. Express as a reduced fraction.
12. Compute: 2/3 x 9/4. Express as a reduced fraction.
13. What is 0.1 + 0.2? (Do this by hand, not in your head.)
14. Express 5/8 as a decimal.
15. Is 1/3 exactly representable as a finite decimal? Why or why not?

### Signs and Order of Operations (5 questions)

16. Compute: -3^2 (Is the answer 9 or -9? Explain why.)
17. Compute: (-3)^2
18. Compute: 2 + 3 x 4 - 1
19. Compute: (2 + 3) x (4 - 1)
20. If a = -5 and b = 3, compute: a x |b| - a

### Estimation and Scale (5 questions)

21. Estimate the order of magnitude: distance light travels in 1 second.
22. Estimate: how many seconds in a year? (Order of magnitude is fine.)
23. If something costs $3.50 each and you buy 7, roughly how much?
24. Estimate: is 1000 x 0.001 closer to 0, 1, or 10?
25. A satellite orbits at 7 km/s. Roughly how far does it travel in 1 hour?

---

## Scoring

| Score | Interpretation |
|-------|---------------|
| 23-25 correct (92-100%) | Strong foundation. Proceed with confidence. |
| 20-22 correct (80-88%) | Good foundation. Watch for sign and notation errors. |
| 17-19 correct (68-76%) | Repair the failed categories. You'll lose time on every session. |
| Below 17 (below 65%) | PAUSE. Repair arithmetic foundations before Session 01. |

### Answer Key (check only after completing all 25)

1. 2.99792458 x 10^8
2. 1.25 x 10^-5
3. 3.75 x 10^6
4. 0.0125 s
5. 2,500 ms
6. 3,747.405 km
7. 1,800 s
8. 5 kg
9. 36 km/h
10. 1,000,000 W (10^6 W)
11. 11/12
12. 3/2 (or 1.5)
13. 0.3 (NOT 0.30000000000000004 — that's a floating point artifact)
14. 0.625
15. No. 1/3 = 0.333... repeating infinitely. This is why 0.1 + 0.2 != 0.3 in IEEE-754.
16. -9. Exponentiation binds tighter than negation. -3^2 = -(3^2) = -9.
17. 9. The parentheses make the base negative. (-3) x (-3) = 9.
18. 13. (2 + 12 - 1 = 13)
19. 15. (5 x 3 = 15)
20. -5 x 3 - (-5) = -15 + 5 = -10
21. ~3 x 10^8 m (300,000 km)
22. ~3.15 x 10^7 s (pi x 10^7 is a good estimate)
23. ~$24.50
24. 1. (1000 x 0.001 = 1.0 exactly)
25. ~25,200 km (7 km/s x 3600 s = 25,200 km)

---

## Score: ____ / 25

Record in the Diagnostic Log in diagnostics/README.md.
