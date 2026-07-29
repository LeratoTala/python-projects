# South African Fuel Cost Calculator

print("=" * 40)
print(" SOUTH AFRICAN FUEL COST CALCULATOR ")
print("=" * 40)

# Ask the user for input
kilometers = float(input("Enter the number of kilometers you want to drive: "))
petrol_price = float(input("Enter the current petrol price per liter (R): "))

# Calculate liters needed
liters_needed = kilometers / 10

# Calculate total cost
total_cost = liters_needed * petrol_price

# Display results
print("\nFuel Cost Summary")
print("-" * 40)
print(f"Distance to travel : {kilometers:.2f} km")
print(f"Petrol price       : R{petrol_price:.2f} per liter")
print(f"Fuel needed        : {liters_needed:.2f} liters")
print(f"Total fuel cost    : R{round(total_cost, 2):.2f}")
print("-" * 40)
print("Thank you for using the Fuel Cost Calculator!")