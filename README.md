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
