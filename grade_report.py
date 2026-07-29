# grade_report.py - Full Grade Report Generator

# Step 1: Store at least 5 students as a list of dictionaries
students = [
    {"name": "Thabo", "maths": 78, "english": 82, "science": 74},
    {"name": "Lerato", "maths": 91, "english": 88, "science": 95},
    {"name": "Sipho", "maths": 45, "english": 52, "science": 48},
    {"name": "Amahle", "maths": 67, "english": 71, "science": 69},
    {"name": "Kgotso", "maths": 55, "english": 60, "science": 58},
]

# List to hold processed results
results = []

# Step 2 & 3: Use a for loop to calculate averages and apply grade/status logic
for student in students:
    name = student["name"]
    maths = student["maths"]
    english = student["english"]
    science = student["science"]

    # Calculate average
    average = (maths + english + science) / 3

    # Determine grade based on average (Unit 5 logic)
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

    # Determine pass/fail status
    if average >= 50:
        status = "Pass"
    else:
        status = "Fail"

    # Step 4: Build results list of dictionaries
    results.append({
        "name": name,
        "average": round(average, 1),
        "grade": grade,
        "status": status
    })

# Step 5: After the main loop, calculate class statistics
# Get all averages into a list for easy calculation
all_averages = [r["average"] for r in results]

class_average = sum(all_averages) / len(all_averages)
highest_mark = max(all_averages)
lowest_mark = min(all_averages)

# Step 6: Display a formatted class report
print("=" * 60)
print("           CLASS GRADE REPORT")
print("=" * 60)
print(f"{'Name':<12} {'Average':<10} {'Grade':<8} {'Status':<8}")
print("-" * 60)

for r in results:
    print(f"{r['name']:<12} {r['average']:<10} {r['grade']:<8} {r['status']:<8}")

print("-" * 60)
print(f"Class Average:   {round(class_average, 1)}")
print(f"Highest Mark:    {highest_mark}")
print(f"Lowest Mark:     {lowest_mark}")
print("=" * 60)

# Step 7: Use a while loop to let the user search for a student by name
print("\n--- Student Search ---")

while True:
    search_name = input("\nEnter a student's name to search (or 'exit' to quit): ").strip()

    if search_name.lower() == "exit":
        print("Goodbye!")
        break

    found = False
    for r in results:
        if r["name"].lower() == search_name.lower():
            print(f"\n  Name:    {r['name']}")
            print(f"  Average: {r['average']}")
            print(f"  Grade:   {r['grade']}")
            print(f"  Status:  {r['status']}")
            found = True
            break

    if not found:
        print(f"Student '{search_name}' not found.")