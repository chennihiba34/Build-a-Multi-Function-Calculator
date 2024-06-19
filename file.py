import math
from fractions import Fraction

def solve_proportion(a, b, c, d):
    """
    Solve a proportion: a/b = c/d
    Returns the value of x in the equation ax = cd
    """
    return (c * b) / a

def solve_for_x(a, b, c):
    """
    Solve for x in the equation ax + b = c
    Returns the value of x
    """
    return (c - b) / a

def factor_square_root(n):
    """
    Factor a square root: √n = √(a^2) = a
    Returns the factored value
    """
    for i in range(1, int(math.sqrt(n)) + 1):
        if i * i == n:
            return i
    return "Cannot factor"

def decimal_to_fraction_and_percent(n):
    """
    Convert a decimal to a fraction and percent
    Returns a tuple of (fraction, percent)
    """
    fraction = Fraction(n).limit_denominator()
    percent = n * 100
    return (fraction, percent)

def fraction_to_decimal_and_percent(numerator, denominator):
    """
    Convert a fraction to a decimal and percent
    Returns a tuple of (decimal, percent)
    """
    decimal = numerator / denominator
    percent = decimal * 100
    return (decimal, percent)

def percent_to_decimal_and_fraction(n):
    """
    Convert a percent to a decimal and fraction
    Returns a tuple of (decimal, fraction)
    """
    decimal = n / 100
    fraction = Fraction(decimal).limit_denominator()
    return (decimal, fraction)

def main():
    print("Multi-Function Calculator")
    print("1. Solve Proportions")
    print("2. Solve for x in Equations")
    print("3. Factor Square Roots")
    print("4. Convert Decimals to Fractions and Percents")
    print("5. Convert Fractions to Decimals and Percents")
    print("6. Convert Percents to Decimals and Fractions")
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        d = float(input("Enter d: "))
        result = solve_proportion(a, b, c, d)
        print(f"x = {result}")

    elif choice == "2":
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        result = solve_for_x(a, b, c
