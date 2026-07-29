# grade_classifier.py

print("=" * 50)
print("        STUDENT GRADE CLASSIFIER")
print("=" * 50)

# Collect learner information
name = input("Enter learner's name: ")

mark1 = float(input("Enter mark for Subject 1: "))
mark2 = float(input("Enter mark for Subject 2: "))
mark3 = float(input("Enter mark for Subject 3: "))

# Calculate average
average = (mark1 + mark2 + mark3) / 3

# Assign letter grade
if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

# Assign pass/fail status
if average >= 50:
    status = "Pass"
else:
    status = "Fail"

# Check for intervention
intervention = []

if mark1 < 40:
    intervention.append("Subject 1")

if mark2 < 40:
    intervention.append("Subject 2")

if mark3 < 40:
    intervention.append("Subject 3")

# Display report card
print("\n" + "=" * 50)
print("              REPORT CARD")
print("=" * 50)
print(f"Learner Name : {name}")
print(f"Subject 1    : {mark1:.2f}")
print(f"Subject 2    : {mark2:.2f}")
print(f"Subject 3    : {mark3:.2f}")
print(f"Average      : {average:.2f}")
print(f"Grade        : {grade}")
print(f"Status       : {status}")

if intervention:
    print("Intervention : Needed in " + ", ".join(intervention))
else:
    print("Intervention : None")

print("=" * 50)
print("End of Report")