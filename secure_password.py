# The Secure Password Hint Tool

# 1. Ask the user to input their secret password
password = input("Enter your secret password: ")

# 2. Use .strip() to remove any accidental spaces at the start or end
password = password.strip()

# 3. Grab the very first letter and the very last letter using string indexing
first_letter = password[0]
last_letter = password[-1]

# 4. Print a hint using an f-string, forcing the letters into uppercase
print(f"Your password hint: It starts with {first_letter.upper()} and ends with {last_letter.upper()}")