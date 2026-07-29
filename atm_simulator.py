# Step 1: Set a fixed variable representing a bank balance
balance = 500

# Step 2: Ask the user how much money they want to withdraw
# Cast the input to a float (or int) so we can do math with it
withdrawal_amount = float(input("How much money would you like to withdraw? R"))

# Step 3: Check if the request is less than or equal to the balance
if withdrawal_amount <= balance:
    balance = balance - withdrawal_amount
    print(f"Withdrawal successful! Remaining balance: R{balance}")

# Step 4: Check if the request is less than or equal to 0
elif withdrawal_amount <= 0:
    print("Invalid amount. You must withdraw more than R0.")

# Step 5: Otherwise, the user doesn't have enough money
else:
    print("Declined. Insufficient funds")