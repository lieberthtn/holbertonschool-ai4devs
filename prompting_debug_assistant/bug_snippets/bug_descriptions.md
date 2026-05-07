## Bug 1 – bug1.cpp
**Intended Behavior**: The program should take or concatenate strings and perform basic operations, then print a confirmation message.
**Issue Type**: Multiple (Syntax errors and Type mismatch).
**Notes**: 
- Missing semicolons at the end of declarations and assignments.
- Attempting to multiply strings (`a * b`), which is not supported in C++.
- Storing a string result into an integer variable (`c = a + b`).
- Contains a random 'x' character at the end of the main function.


## Bug 2 – bug2.py
**Intended Behavior**: Process user information and calculate the average price of items in a list.
**Issue Type**: TypeError and ZeroDivisionError.
**Notes**: String concatenation with integer, potential division by zero, and handling None values in a list.

## Bug 3 – bug3.js
**Intended Behavior**: Find a user by their ID in an array of objects.
**Issue Type**: ReferenceError, Assignment instead of Comparison, and Null Pointer.
**Notes**: Global variable leakage, using '=' instead of '===' in IF statement, and accessing properties of a null object.



