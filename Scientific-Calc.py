"""
Scientific Calculator - Python
School Project
Uses only the built-in 'math' module (no external libraries needed)
"""

import math

# ─────────────────────────────────────────────
#  Helper utilities
# ─────────────────────────────────────────────

def get_float(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  [!] Invalid input. Please enter a number.")

def deg_to_rad(deg):
    return math.radians(deg)

def rad_to_deg(rad):
    return math.degrees(rad)

# ─────────────────────────────────────────────
#  Calculator functions
# ─────────────────────────────────────────────

# ── Basic Arithmetic ──────────────────────────
def add(a, b):       return a + b
def subtract(a, b):  return a - b
def multiply(a, b):  return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
def modulus(a, b):
    if b == 0:
        raise ValueError("Cannot take modulus with zero.")
    return a % b
def power(a, b):     return a ** b

# ── Roots & Logarithms ────────────────────────
def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(a)

def cube_root(a):
    # Works for negatives too
    return math.copysign(abs(a) ** (1/3), a)

def nth_root(a, n):
    if n == 0:
        raise ValueError("Root index cannot be zero.")
    return math.copysign(abs(a) ** (1/n), a)

def natural_log(a):
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive numbers.")
    return math.log(a)

def log_base10(a):
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive numbers.")
    return math.log10(a)

def log_base(a, base):
    if a <= 0 or base <= 0 or base == 1:
        raise ValueError("Invalid input for logarithm.")
    return math.log(a, base)

def exponential(a):  return math.exp(a)   # e^a

# ── Trigonometry (input in degrees) ──────────
def sine(deg):       return math.sin(deg_to_rad(deg))
def cosine(deg):     return math.cos(deg_to_rad(deg))
def tangent(deg):
    if math.cos(deg_to_rad(deg)) == 0:
        raise ValueError("tan is undefined at this angle.")
    return math.tan(deg_to_rad(deg))

# Inverse trig (result in degrees)
def arc_sine(a):
    if not -1 <= a <= 1:
        raise ValueError("arcsin input must be in [-1, 1].")
    return rad_to_deg(math.asin(a))

def arc_cosine(a):
    if not -1 <= a <= 1:
        raise ValueError("arccos input must be in [-1, 1].")
    return rad_to_deg(math.acos(a))

def arc_tangent(a):  return rad_to_deg(math.atan(a))

# Hyperbolic
def sinh(a):   return math.sinh(a)
def cosh(a):   return math.cosh(a)
def tanh(a):   return math.tanh(a)

# ── Number Theory & Combinatorics ─────────────
def factorial(n):
    n = int(n)
    if n < 0:
        raise ValueError("Factorial is undefined for negative integers.")
    return math.factorial(n)

def permutation(n, r):
    n, r = int(n), int(r)
    if n < 0 or r < 0 or r > n:
        raise ValueError("Invalid n or r for permutation.")
    return math.factorial(n) // math.factorial(n - r)

def combination(n, r):
    n, r = int(n), int(r)
    if n < 0 or r < 0 or r > n:
        raise ValueError("Invalid n or r for combination.")
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

def gcd(a, b):  return math.gcd(int(a), int(b))
def lcm(a, b):
    a, b = int(a), int(b)
    return abs(a * b) // math.gcd(a, b) if a and b else 0

# ── Misc ──────────────────────────────────────
def absolute_value(a):  return abs(a)
def floor_val(a):       return math.floor(a)
def ceil_val(a):        return math.ceil(a)
def round_val(a, d):    return round(a, int(d))

# ─────────────────────────────────────────────
#  Menu & main loop
# ─────────────────────────────────────────────

MENU = """
╔══════════════════════════════════════════════╗
║         SCIENTIFIC CALCULATOR  v1.0          ║
╠══════════════════════════════════════════════╣
║  BASIC ARITHMETIC                            ║
║   1. Addition (a + b)                        ║
║   2. Subtraction (a - b)                     ║
║   3. Multiplication (a × b)                  ║
║   4. Division (a ÷ b)                        ║
║   5. Modulus (a % b)                         ║
║   6. Power (a ^ b)                           ║
╠══════════════════════════════════════════════╣
║  ROOTS & EXPONENTS                           ║
║   7. Square Root (√a)                        ║
║   8. Cube Root (∛a)                          ║
║   9. Nth Root (ⁿ√a)                          ║
║  10. Exponential (eˣ)                        ║
╠══════════════════════════════════════════════╣
║  LOGARITHMS                                  ║
║  11. Natural Log  ln(a)                      ║
║  12. Log base 10  log(a)                     ║
║  13. Log any base  logₙ(a)                   ║
╠══════════════════════════════════════════════╣
║  TRIGONOMETRY  (angles in degrees)           ║
║  14. sin(θ)   15. cos(θ)   16. tan(θ)        ║
║  17. arcsin   18. arccos   19. arctan        ║
║  20. sinh     21. cosh     22. tanh          ║
╠══════════════════════════════════════════════╣
║  COMBINATORICS & NUMBER THEORY               ║
║  23. Factorial (n!)                          ║
║  24. Permutation P(n,r)                      ║
║  25. Combination C(n,r)                      ║
║  26. GCD        27. LCM                      ║
╠══════════════════════════════════════════════╣
║  MISC                                        ║
║  28. Absolute Value |a|                      ║
║  29. Floor  30. Ceiling  31. Round           ║
║  32. Constants (π, e, φ)                     ║
╠══════════════════════════════════════════════╣
║   0. Exit                                    ║
╚══════════════════════════════════════════════╝
"""

def show_constants():
    print(f"\n  π  (pi)      = {math.pi}")
    print(f"  e  (Euler)   = {math.e}")
    print(f"  φ  (golden)  = {(1 + math.sqrt(5)) / 2}")
    print(f"  √2            = {math.sqrt(2)}")
    print(f"  √3            = {math.sqrt(3)}")

def run():
    print("\nWelcome to Scientific Calculator!")
    while True:
        print(MENU)
        choice = input("Enter option: ").strip()

        try:
            if choice == "0":
                print("\nGoodbye! 👋\n")
                break

            # ── Basic Arithmetic ──
            elif choice == "1":
                a, b = get_float("  a = "), get_float("  b = ")
                print(f"  Result: {a} + {b} = {add(a, b)}")

            elif choice == "2":
                a, b = get_float("  a = "), get_float("  b = ")
                print(f"  Result: {a} - {b} = {subtract(a, b)}")

            elif choice == "3":
                a, b = get_float("  a = "), get_float("  b = ")
                print(f"  Result: {a} × {b} = {multiply(a, b)}")

            elif choice == "4":
                a, b = get_float("  a = "), get_float("  b = ")
                print(f"  Result: {a} ÷ {b} = {divide(a, b)}")

            elif choice == "5":
                a, b = get_float("  a = "), get_float("  b = ")
                print(f"  Result: {a} % {b} = {modulus(a, b)}")

            elif choice == "6":
                a, b = get_float("  base a = "), get_float("  exponent b = ")
                print(f"  Result: {a}^{b} = {power(a, b)}")

            # ── Roots & Exponents ──
            elif choice == "7":
                a = get_float("  a = ")
                print(f"  Result: √{a} = {square_root(a)}")

            elif choice == "8":
                a = get_float("  a = ")
                print(f"  Result: ∛{a} = {cube_root(a)}")

            elif choice == "9":
                a = get_float("  a = ")
                n = get_float("  n (root index) = ")
                print(f"  Result: {n}√{a} = {nth_root(a, n)}")

            elif choice == "10":
                a = get_float("  x = ")
                print(f"  Result: e^{a} = {exponential(a)}")

            # ── Logarithms ──
            elif choice == "11":
                a = get_float("  a = ")
                print(f"  Result: ln({a}) = {natural_log(a)}")

            elif choice == "12":
                a = get_float("  a = ")
                print(f"  Result: log₁₀({a}) = {log_base10(a)}")

            elif choice == "13":
                a    = get_float("  a = ")
                base = get_float("  base = ")
                print(f"  Result: log_{base}({a}) = {log_base(a, base)}")

            # ── Trigonometry ──
            elif choice == "14":
                a = get_float("  angle (degrees) = ")
                print(f"  Result: sin({a}°) = {sine(a)}")

            elif choice == "15":
                a = get_float("  angle (degrees) = ")
                print(f"  Result: cos({a}°) = {cosine(a)}")

            elif choice == "16":
                a = get_float("  angle (degrees) = ")
                print(f"  Result: tan({a}°) = {tangent(a)}")

            elif choice == "17":
                a = get_float("  value [-1, 1] = ")
                print(f"  Result: arcsin({a}) = {arc_sine(a)}°")

            elif choice == "18":
                a = get_float("  value [-1, 1] = ")
                print(f"  Result: arccos({a}) = {arc_cosine(a)}°")

            elif choice == "19":
                a = get_float("  value = ")
                print(f"  Result: arctan({a}) = {arc_tangent(a)}°")

            elif choice == "20":
                a = get_float("  x = ")
                print(f"  Result: sinh({a}) = {sinh(a)}")

            elif choice == "21":
                a = get_float("  x = ")
                print(f"  Result: cosh({a}) = {cosh(a)}")

            elif choice == "22":
                a = get_float("  x = ")
                print(f"  Result: tanh({a}) = {tanh(a)}")

            # ── Combinatorics ──
            elif choice == "23":
                n = get_float("  n = ")
                print(f"  Result: {int(n)}! = {factorial(n)}")

            elif choice == "24":
                n, r = get_float("  n = "), get_float("  r = ")
                print(f"  Result: P({int(n)},{int(r)}) = {permutation(n, r)}")

            elif choice == "25":
                n, r = get_float("  n = "), get_float("  r = ")
                print(f"  Result: C({int(n)},{int(r)}) = {combination(n, r)}")

            elif choice == "26":
                a, b = get_float("  a = "), get_float("  b = ")
                print(f"  Result: GCD({int(a)}, {int(b)}) = {gcd(a, b)}")

            elif choice == "27":
                a, b = get_float("  a = "), get_float("  b = ")
                print(f"  Result: LCM({int(a)}, {int(b)}) = {lcm(a, b)}")

            # ── Misc ──
            elif choice == "28":
                a = get_float("  a = ")
                print(f"  Result: |{a}| = {absolute_value(a)}")

            elif choice == "29":
                a = get_float("  a = ")
                print(f"  Result: floor({a}) = {floor_val(a)}")

            elif choice == "30":
                a = get_float("  a = ")
                print(f"  Result: ceil({a}) = {ceil_val(a)}")

            elif choice == "31":
                a = get_float("  a = ")
                d = get_float("  decimal places = ")
                print(f"  Result: round({a}, {int(d)}) = {round_val(a, d)}")

            elif choice == "32":
                show_constants()

            else:
                print("  [!] Invalid option. Please enter a number from the menu.")

        except ValueError as e:
            print(f"  [!] Error: {e}")
        except Exception as e:
            print(f"  [!] Unexpected error: {e}")

        input("\n  Press Enter to continue...")

# ─────────────────────────────────────────────
if __name__ == "__main__":
    run()
