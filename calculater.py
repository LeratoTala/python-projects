# calculator.py

print("=" * 40)
print("      MULTI-FUNCTION CALCULATOR")
print("=" * 40)

# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Basic operations
addition = round(num1 + num2, 2)
subtraction = round(num1 - num2, 2)
multiplication = round(num1 * num2, 2)

print("\nResults")
print("-" * 40)
print(f"{'Operation':<20}{'Result'}")
print("-" * 40)

print(f"{'Addition':<20}{addition}")
print(f"{'Subtraction':<20}{subtraction}")
print(f"{'Multiplication':<20}{multiplication}")

# Division-related operations
if num2 != 0:
    division = round(num1 / num2, 2)
    floor_division = num1 // num2
    modulus = num1 % num2

    print(f"{'Division':<20}{division}")
    print(f"{'Floor Division':<20}{floor_division}")
    print(f"{'Modulus':<20}{modulus}")
else:
    print(f"{'Division':<20}Cannot divide by zero")
    print(f"{'Floor Division':<20}Cannot divide by zero")
    print(f"{'Modulus':<20}Cannot divide by zero")

print("-" * 40)
print("Calculation complete!")