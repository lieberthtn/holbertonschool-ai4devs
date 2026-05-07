# Debugging Project Report

## Bug Report – bug1.cpp
- **Summary**: Syntax errors and type mismatch in string operations.
- **Root Cause**: Missing semicolons and attempting to perform arithmetic operations (multiplication) on string objects which is not supported in C++.
- **Resolution**: AI suggested using proper string concatenation. Manually added `#include <string>` and removed the invalid multiplication logic to ensure the code compiles.
- **Lesson Learned**: String manipulation in C++ requires specific headers and does not support Python-like string multiplication.

## Bug Report – bug2.py
- **Summary**: Type errors and unhandled None values in user data processing.
- **Root Cause**: Implicitly concatenating strings with integers and failing to check for `None` values in a dictionary, leading to a `TypeError`.
- **Resolution**: Used AI-suggested f-strings for safe printing and added a conditional check (`if price is not None`) to handle missing data.
- **Lesson Learned**: Always validate external data (like dictionary values) before performing arithmetic operations.

## Bug Report – bug3.js
- **Summary**: Logic error in comparison and potential null pointer dereference.
- **Root Cause**: Used a single equals sign (`=`) for assignment inside an `if` condition instead of strict equality (`===`), and accessed properties of a potentially null object.
- **Resolution**: Applied the AI fix to use `===` and added a manual null-check to verify if a user was actually found before printing.
- **Lesson Learned**: In JavaScript, always use strict equality to avoid accidental assignments in conditional statements.

## Bug Report – bug4.c
- **Summary**: Buffer overflow and division by zero.
- **Root Cause**: The loop condition (`i <= 10`) exceeded the fixed array size of 5, and a hardcoded divisor was set to zero.
- **Resolution**: AI suggested fixing the loop boundary to `i < 5`. Manually added a safety check for the divisor (`if (y != 0)`) before the division.
- **Lesson Learned**: Out-of-bounds errors in C are silent but dangerous; always define loop limits based on array size.
