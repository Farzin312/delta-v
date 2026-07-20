# The PREDICT Step & Scale Workbook

Welcome! This directory is a dedicated workspace to help you master **Step 1: PREDICT** of the 7-step Frontier Engineer learning loop.

Struggling with the prediction step is common, especially when you do not yet know the equations. This guide and its accompanying examples will show you how to calibrate your intuition, estimate order of magnitude (Scale), and predict behaviors using physical reasoning from a blank page.

---

## 1. What is "Scale" (Order of Magnitude)?

In engineering, **Scale** does not mean calculating a precise decimal like `42.73`. It means finding the nearest power of 10 that represents your quantity. We write this as 10^x.

Think of Scale as answering: **"How many digits does this number have, and where is the decimal point?"**

Here is a quick lookup table of scales in simple terms:

| Scale | Value | Intuitive Size (m, s, kg, N) | Example |
| :--- | :--- | :--- | :--- |
| **10^-6** | 0.000001 | Micro-scale. Invisible to the naked eye. | Width of a bacteria, wavelength of light. |
| **10^-3** | 0.001 | Milli-scale. Tiny, but visible. | Thickness of a coin, duration of a camera flash (milliseconds). |
| **10^0** | 1 | Human-scale. Single-digit numbers (1 to 9). | Length of a guitar, weight of a laptop, time to take a step (1 second). |
| **10^1** | 10 | Ten-scale. Double-digit numbers (10 to 99). | Height of a three-story building (10 m), speed of a running dog (10 m/s). |
| **10^2** | 100 | Hundred-scale. Triple-digit numbers (100 to 999). | Length of a soccer field, speed of a highway car (30 m/s ~ 100 km/h). |
| **10^3** | 1,000 | Kilo-scale. A short drive, large mass (1,000 to 9,999). | Height of a mountain (3,000 m), mass of a small car (1,500 kg). |
| **10^6** | 1,000,000 | Mega-scale. Planetary scales, high speeds. | Radius of the Earth (~6.4 x 10^6 m). |
| **10^8** | 100,000,000 | Extreme scale. | Speed of light (~3 x 10^8 m/s). |

### The 3.16 Rounding Rule

To find the scale, round to the nearest power of 10. The midpoint of a log scale is sqrt(10) ~ 3.16.

- If a number is **less than 3.16**, round it to the **lower** power of 10. (e.g., 2 m is scale 10^0 m, since 2 < 3.16).
- If a number is **greater than 3.16**, round it to the **higher** power of 10. (e.g., 8 m is scale 10^1 m, since 8 > 3.16).
- **Examples**:
  - 0.2 => 10^-1 (since 0.2 is between 0.0316 and 0.316)
  - 2.5 => 10^0 (since 2.5 is between 0.316 and 3.16)
  - 85.0 => 10^2 (since 85.0 is between 31.6 and 316)

---

## 2. Predicting Without Knowing the Equations

You do not need an equation to make a prediction. In fact, **if you look up the equation first, you bypass the learning.** The prediction is a check on your physical intuition.

Here are the three tools to make a prediction from a blank page:

### Tool 1: Bounding (Min/Max Sanity Checks)

Ask yourself: **What is the absolute physical limit of this scenario?**
- If you are calculating the speed of a satellite, it must be less than the speed of light (3 x 10^8 m/s) and greater than 0.
- If you are calculating the time to drop an object from a table, it must be greater than 0 and probably less than 10 seconds. It is human-scale, so 10^0 s (1 second) is a reasonable guess.

### Tool 2: Dimensional Matchmaker

Look at the inputs and the desired units. Try to assemble them using basic math to get the output unit.
- **Example**: You want to find **Time** (units: s). You are given **Distance** (units: m) and **Speed** (units: m/s).
- How do you get seconds from meters and meters-per-second?

      s = m / (m/s) = m * (s/m) = s

- So, even if you do not know the exact formula, you know that Time must be related to Distance / Speed.
- If Distance = 100 m and Speed = 10 m/s, your estimated time is ~10 s. The scale is 10^1 s.

### Tool 3: Extreme Limits (Qualitative Trends)

Change the inputs in your mind to see what happens to the output.
- **Direction**: "If I make the object heavier, does it fall faster or slower? (Under gravity alone: same. With drag: faster.)"
- "If I push the brakes harder, does the stopping distance increase or decrease? (Decreases.)"
- This tells you the **Direction** field. If input X increases, does output Y increase (positive relationship) or decrease (inverse relationship)?

---

## 3. Directory Map

To help you learn, this directory contains step-by-step walkthroughs of three distinct problems and a set of practice scenarios:

1. **[Example 1: Dropping a Rock](example_01_cliff_drop.md)**
   - *Concepts*: 1D Kinematics, constant gravity, time scales.
   - *Key takeaway*: How to construct a complete loop for a simple algebraic system.
2. **[Example 2: Stopping Distance of a Car](example_02_braking_car.md)**
   - *Concepts*: 1D Kinematics, braking deceleration, quadratic speed scaling.
   - *Key takeaway*: How to test and falsify scaling invariants (d ~ v^2).
3. **[Example 3: Orbital Period of a Satellite](example_03_satellite_orbit.md)**
   - *Concepts*: Circular motion, gravity, planetary scale.
   - *Key takeaway*: How to reason about scales of 10^3 to 10^6 and boundary limits.
4. **[Practice Workbook: Test Yourself](practice_exercises.md)**
   - A collection of new scenarios with questions at the top/middle, and step-by-step predictions and calculations at the bottom.

---

[<- Back to Method](../method.md)
