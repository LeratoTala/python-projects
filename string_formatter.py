"""
Student Info Formatter
------------------------
Collects personal information from the user and displays it
in a formatted profile card. Demonstrates use of all four
core data types (str, int, float, bool), string manipulation,
arithmetic, and f-string formatting.
"""

# ----- Collect information from the user -----
first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
favourite_number = float(input("Enter your favourite number: "))

# ----- String manipulation -----
full_name = f"{first_name} {surname}"
full_name_upper = full_name.upper()
full_name_title = full_name.title()

# ----- Arithmetic -----
age_in_months = age * 12

# ----- Rounding -----
favourite_number_rounded = round(favourite_number, 2)

# ----- Boolean (fourth data type) -----
is_adult = age >= 18

# ----- Display formatted profile card -----
print("\n" + "=" * 40)
print(f"Welcome, {full_name}!")
print("=" * 40)
print(f"Full Name (UPPERCASE): {full_name_upper}")
print(f"Full Name (Title Case): {full_name_title}")
print(f"Age: {age} years old")
print(f"Age in Months: {age_in_months} months")
print(f"Favourite Number (rounded to 2 d.p.): {favourite_number_rounded}")
print(f"Is Adult (18+): {is_adult}")
print("=" * 40)

# ----- Display data types of each collected value -----
print("\nData Types:")
print(f"first_name -> {type(first_name)}")
print(f"surname -> {type(surname)}")
print(f"age -> {type(age)}")
print(f"favourite_number -> {type(favourite_number)}")
print(f"is_adult -> {type(is_adult)}")