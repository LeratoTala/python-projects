# Python String Tools

A collection of Python scripts demonstrating string manipulation, data types, and f-string formatting.

---

## Student Info Formatter (`string_formatter.py`)

Collects personal information from the user and displays it in a formatted profile card.

### What it does

Prompts the user for:
- First name and surname
- Age
- Favourite number

Then outputs a profile card showing:
- Full name in uppercase and title case
- Age in years and months
- Favourite number rounded to 2 decimal places
- Whether the user is an adult (18+)
- Data types of each collected value

### Concepts demonstrated

- Core data types: `str`, `int`, `float`, `bool`
- String manipulation and f-string formatting
- Arithmetic operations
- Rounding and boolean expressions

### Usage

```bash
python string_formatter.py
```

Example output:

```
========================================
Welcome, Jane Doe!
========================================
Full Name (UPPERCASE): JANE DOE
Full Name (Title Case): Jane Doe
Age: 20 years old
Age in Months: 240 months
Favourite Number (rounded to 2 d.p.): 3.14
Is Adult (18+): True
========================================

Data Types:
first_name -> <class 'str'>
surname -> <class 'str'>
age -> <class 'int'>
favourite_number -> <class 'float'>
is_adult -> <class 'bool'>
```

---

## Secure Password Hint Tool (`secure_password.py`)

Takes a user's password and generates a hint showing only the first and last letters in uppercase.

### What it does

- Prompts the user to enter a secret password
- Strips accidental leading/trailing spaces with `.strip()`
- Extracts the first and last characters using string indexing
- Displays a hint with both letters forced to uppercase

### Concepts demonstrated

- String input and `.strip()`
- String indexing (`[0]` and `[-1]`)
- `.upper()` and f-string formatting

### Usage

```bash
python secure_password.py
```

Example output:

```
Enter your secret password: hello
Your password hint: It starts with H and ends with O
```

---

## Multi-Function Calculator (`calculater.py`)

Takes two numbers and displays results for all basic arithmetic operations.

### What it does

- Prompts for two numbers
- Computes addition, subtraction, multiplication, division, floor division, and modulus
- Handles division by zero gracefully

### Concepts demonstrated

- Arithmetic operators including `//` and `%`
- Conditional logic for zero-division guard
- f-string table formatting with alignment

### Usage

```bash
python calculater.py
```

---

## ATM Simulator (`atm_simulator.py`)

Simulates a basic ATM withdrawal with a fixed starting balance.

### What it does

- Starts with a balance of R500
- Prompts the user for a withdrawal amount
- Approves, declines, or rejects invalid amounts accordingly

### Concepts demonstrated

- `if/elif/else` branching
- Float input casting
- Basic financial logic

### Usage

```bash
python atm_simulator.py
```

---

## Contact Book (`contact_book.py`)

An in-memory contact manager with a menu-driven interface.

### What it does

- Add, search, delete, and view contacts
- Each contact stores a name, phone number, and email
- Runs in a loop until the user chooses to exit

### Concepts demonstrated

- Lists of dictionaries
- Functions and modular design
- String comparison with `.lower()`
- `while True` menu loop

### Usage

```bash
python contact_book.py
```

---

## Fuel Cost Calculator (`fuel_calculater.py`)

Calculates the fuel cost for a trip based on distance and petrol price.

### What it does

- Prompts for distance (km) and petrol price per litre
- Assumes a consumption rate of 10 km/litre
- Displays a formatted cost summary

### Concepts demonstrated

- Float arithmetic
- f-string formatting with `.2f`
- Simple formula-based calculation

### Usage

```bash
python fuel_calculater.py
```

---

## Student Grade Classifier (`grade_classifier.py`)

Collects marks for three subjects and produces a report card for a single learner.

### What it does

- Prompts for a learner's name and three subject marks
- Calculates the average and assigns a letter grade (A–F)
- Determines pass/fail status and flags subjects needing intervention (below 40)

### Concepts demonstrated

- `if/elif/else` chains
- List building with `.append()`
- f-string report formatting

### Usage

```bash
python grade_classifier.py
```

---

## Class Grade Report (`grade_report.py`)

Generates a full grade report for a hardcoded class of five students.

### What it does

- Processes a list of student dictionaries to calculate averages, grades, and pass/fail status
- Displays a formatted class report with the class average, highest, and lowest marks
- Lets the user search for a student by name in a `while` loop

### Concepts demonstrated

- List of dictionaries and `for` loops
- List comprehensions for extracting values
- `while True` search loop with `break`
- `min()`, `max()`, and `sum()` on lists

### Usage

```bash
python grade_report.py
```

---

## Phone Directory Search (`phone_directory_search.py`)

Looks up a friend's phone number from a small hardcoded dictionary.

### What it does

- Stores three contacts as a dictionary (name → phone number)
- Prompts the user to enter a name
- Prints the number if found, or a "not found" message otherwise

### Concepts demonstrated

- Dictionary lookup with `in`
- String keys and values
- Basic `if/else` branching

### Usage

```bash
python phone_directory_search.py
```

---

## Score Tracker Game (`tracker_game.py`)

A simple loop that tracks game scores entered by the user.

### What it does

- Repeatedly prompts the user to enter a score
- Prints a reaction based on whether the score exceeds 100
- Handles non-numeric input gracefully and exits on `'stop'`

### Concepts demonstrated

- `while True` loop with `break`
- `try/except` for input validation
- `.strip().lower()` for input normalisation

### Usage

```bash
python tracker_game.py
```
