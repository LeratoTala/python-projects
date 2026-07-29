# Student Info Formatter

A Python script that collects personal information from the user and displays it in a formatted profile card.

## What it does

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

## Concepts demonstrated

- Core data types: `str`, `int`, `float`, `bool`
- String manipulation and f-string formatting
- Arithmetic operations
- Rounding
- Boolean expressions

## Usage

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
