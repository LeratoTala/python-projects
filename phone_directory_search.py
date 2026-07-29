# The Phone Directory Search

# Step 1: Create a dictionary with friend names as keys and phone numbers as values
# Phone numbers are stored as strings to keep the leading 0
contacts = {
    "Thabo": "0821112222",
    "Lerato": "0833334444",
    "Sipho": "0845556666"
}

# Step 2: Ask the user to input the name of the friend they want to look up
name = input("Enter the name of the friend you want to look up: ")

# Step 3 & 4: Check if the name exists in the dictionary
if name in contacts:
    number = contacts[name]
    print(f"Found! {name}'s number is {number}")
else:
    print("Contact not found.")