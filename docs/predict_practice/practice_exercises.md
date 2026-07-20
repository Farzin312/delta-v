# Practice Exercises: The PREDICT Step

Test your prediction skills! For each of the following scenarios, attempt to fill out the Step 1: PREDICT block.

**Rules**:
1. **No AI, no hints, no calculators.**
2. **Do not look up the equations first.**
3. Use the three tools: **Bounding** (max/min sanity checks), **Dimensional Matchmaker** (combine units), and **Extreme Limits** (qualitative trends).

---

## The Practice Scenarios

### Scenario A: Heating Water in a Microwave

**Problem**: You place a cup containing 250 grams of water (about 1 cup) in a 1,000 W microwave. You run it for 60 seconds at full power. Predict the temperature increase (in degrees Celsius) of the water, assuming the microwave is 100% efficient at transferring energy. (Specific heat of water is about 4.2 J / (g deg-C)).

#### Fill in:
```
Sign:         
Scale:        
Direction:    
Units:        
Failure case: 
```

---

### Scenario B: Aerodynamic Drag Force on a Cyclist

**Problem**: A cyclist is riding at a speed of 10 m/s (about 22 mph). The density of air is about 1.2 kg/m^3. The frontal area of the cyclist is about 0.5 m^2, and their drag coefficient is about 0.9. Predict the drag force (in Newtons) resisting the cyclist's motion.

#### Fill in:
```
Sign:         
Scale:        
Direction:    
Units:        
Failure case: 
```

---

### Scenario C: Escape Velocity of Earth

**Problem**: What is the speed (in meters per second) a projectile needs to be launched from the surface of the Earth to escape Earth's gravity entirely and never fall back? (Earth Mass M ~ 6 x 10^24 kg, Radius R ~ 6.4 x 10^6 m, Gravitational constant G ~ 6.67 x 10^-11 m^3 kg^-1 s^-2).

#### Fill in:
```
Sign:         
Scale:        
Direction:    
Units:        
Failure case: 
```

---

### Scenario D: Draining a Water Tank

**Problem**: A cylindrical water tank has a height of 2.0 m and is filled with water. A small drain hole of cross-sectional area 0.001 m^2 is opened at the bottom. The total cross-sectional area of the tank is 1.0 m^2. Predict the initial volumetric flow rate (in cubic meters per second, m^3/s) of the water leaving the tank. (Assume gravity g ~ 10 m/s^2).

#### Fill in:
```
Sign:         
Scale:        
Direction:    
Units:        
Failure case: 
```

---

<br><br><br>
<br><br><br>
<br><br><br>
*(Scroll down for solutions, physical reasoning, and calculations...)*
<br><br><br>
<br><br><br>
<br><br><br>

---

## Answers & Explanations

Here is how to reason through each prediction step-by-step.

---

### Scenario A: Heating Water in a Microwave

#### How to predict:
1. **Sign**: The microwave is transferring energy to heat the water. The temperature change must be **positive**.
2. **Scale**: Water in a microwave for 1 minute gets hot but does not boil instantly from room temp. Room temp is ~20 deg-C, boiling is 100 deg-C. The change must be around 30 to 70 degrees. This is in the tens of degrees. Under the 3.16 rule, any value between 3.16 and 31.6 is 10^1, and between 31.6 and 316 is 10^2. Let's predict **10^1 deg-C** or **10^2 deg-C** (tens of degrees).
3. **Direction**: If microwave power or heating time increases, temperature change **increases**. If water mass increases, temperature change **decreases** (takes more energy to heat more water).
4. **Units**: Temperature change is measured in **Degrees Celsius (deg-C)**.
5. **Failure case**: Water mass is zero (division by zero), specific heat is zero, microwave power is negative.

#### The Equation & Calculation:
The energy supplied by the microwave is power times time:

    E = P * t = 1,000 W * 60 s = 60,000 Joules

The heat energy absorbed by water is:

    Q = m * c * dT

Assuming 100% efficiency, Q = E:

    E = m * c * dT
    dT = E / (m * c)

Substitute the values:

    dT = 60,000 / (250 * 4.2)
       = 60,000 / 1050
       ~ 57.1 deg-C

Using the 3.16 rule: 57.1 > 31.6, so the scale is **10^2 deg-C** (meaning it is closer to 100 than to 10).

#### Correct Predict Block:
```
Sign:         Positive
Scale:        10^2 deg-C
Direction:    Increasing with power and time, decreasing with water mass
Units:        Degrees Celsius (deg-C)
Failure case: Water mass <= 0, Specific heat <= 0
```

---

### Scenario B: Aerodynamic Drag Force on a Cyclist

#### How to predict:
1. **Sign**: Force opposing motion is **positive** in the backward direction (resisting motion).
2. **Scale**: How hard is the wind pushing back on a cyclist? A strong wind can feel like a solid push, but it does not knock a house down. It is not 0.1 Newtons (10^-1), nor is it 1000 Newtons (10^3, which is the weight of a person). It should be a few dozen Newtons. We predict **10^1 N** (tens of Newtons).
3. **Direction**: If speed increases, drag force **increases** (very rapidly, actually speed squared!). If frontal area or air density increases, drag **increases**.
4. **Units**: Force is measured in **Newtons (N)**.
5. **Failure case**: Air density is negative, frontal area is negative.

#### The Equation & Calculation:
The drag equation is:

    F_d = (1/2) * rho * v^2 * C_d * A

Where:
- rho = 1.2 kg/m^3 (air density)
- v = 10 m/s (speed)
- C_d = 0.9 (drag coefficient)
- A = 0.5 m^2 (frontal area)

Substitute the values:

    F_d = 0.5 * 1.2 * (10)^2 * 0.9 * 0.5
        = 0.5 * 1.2 * 100 * 0.9 * 0.5
        = 27 Newtons

Using the 3.16 rule: 27 is between 3.16 and 31.6, so the scale is **10^1 N**.

#### Correct Predict Block:
```
Sign:         Positive
Scale:        10^1 N (27 N)
Direction:    Increasing with velocity, air density, drag coefficient, and area
Units:        Newtons (N)
Failure case: Frontal area < 0, air density < 0
```

---

### Scenario C: Escape Velocity of Earth

#### How to predict:
1. **Sign**: Speed must be **positive**.
2. **Scale**: You need to go extremely fast to escape Earth. Normal highway speeds are 30 m/s (10^1). Orbital speeds are around 8,000 m/s (10^4). Escape velocity must be higher than orbital velocity. It is likely in the tens of thousands of meters per second. So we predict **10^4 m/s** (tens of thousands).
3. **Direction**: If Earth's mass increases, escape velocity **increases** (stronger gravity pulling you back). If Earth's radius increases (meaning you start further from the center of mass), escape velocity **decreases** (gravity is weaker at the surface).
4. **Units**: Speed is measured in **Meters per second (m/s)**.
5. **Failure case**: Earth mass is zero or negative, Earth radius is zero (singularity/black hole).

#### The Equation & Calculation:
By conservation of energy, the kinetic energy must balance the gravitational potential energy to escape to infinity:

    (1/2) * m * v_esc^2 = G * M * m / R
    v_esc = sqrt(2 * G * M / R)

Substitute the values:

    v_esc = sqrt( 2 * (6.67 x 10^-11) * (6 x 10^24) / (6.4 x 10^6) )
          = sqrt( 8.0 x 10^14 / 6.4 x 10^6 )
          = sqrt( 1.25 x 10^8 )
          ~ 11,180 m/s

Using the 3.16 rule: 11,180 is between 3,162 and 31,622, so the scale is **10^4 m/s**.

#### Correct Predict Block:
```
Sign:         Positive
Scale:        10^4 m/s (11,180 m/s)
Direction:    Increasing with planet mass, decreasing with planet radius
Units:        Meters per second (m/s)
Failure case: Planet radius <= 0, planet mass <= 0
```

---

### Scenario D: Draining a Water Tank

#### How to predict:
1. **Sign**: Flow rate out of the tank must be **positive**.
2. **Scale**: The drain hole is tiny (0.001 m^2 = 10 cm^2). The speed of the water squirting out might be a few meters per second.
   - Using the **Dimensional Matchmaker**:

         Volumetric flow rate Q = Area A * Velocity v
         Units: m^2 * m/s = m^3/s

   - If A = 0.001 m^2 and v is around 5 m/s, then Q ~ 0.005 m^3/s.
   - Under the 3.16 rule: 0.005 is between 0.00316 and 0.0316, so its scale is **10^-3 m^3/s**.
3. **Direction**: If water height h increases, pressure increases, so the flow rate **increases**. If gravity g increases, flow rate **increases**. If the drain hole area A increases, flow rate **increases**.
4. **Units**: Cubic meters per second (m^3/s).
5. **Failure case**: Water height is negative, drain hole area is negative, gravity is negative.

#### The Equation & Calculation:
By Torricelli's Law, the velocity of the fluid leaving the orifice is:

    v = sqrt(2 * g * h)

Volumetric flow rate Q is:

    Q = A_hole * v = A_hole * sqrt(2 * g * h)

Substitute the values:

    Q = 0.001 * sqrt(2 * 10 * 2.0)
      = 0.001 * sqrt(40)
      ~ 0.001 * 6.32
      ~ 0.00632 m^3/s

Using the 3.16 rule: 0.00632 is between 0.00316 and 0.0316, so the scale is indeed **10^-3 m^3/s**.

#### Correct Predict Block:
```
Sign:         Positive
Scale:        10^-3 m^3/s (0.0063 m^3/s)
Direction:    Increasing with height, gravity, and drain hole area
Units:        Cubic meters per second (m^3/s)
Failure case: height < 0, drain hole area < 0, gravity < 0
```

---

[<- Back to README](README.md)
