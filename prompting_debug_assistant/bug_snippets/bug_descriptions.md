## Bug 1 – bug1.cpp
**Intended Behavior**: The program should concatenate two user-provided strings and display a confirmation message "hesablayici isleyir" upon successful execution.
**Issue Type**: Syntax and Type Mismatch.
**Notes**: The program fails to compile due to missing semicolons and invalid string-to-int operations.

## Bug 2 – bug2.py
**Intended Behavior**: This script should process a user's profile by calculating their age for the following year and returning the average price of items in their shopping cart.
**Issue Type**: Runtime Exception (TypeError / ZeroDivisionError).
**Notes**: Fails when adding integers to strings in print statements and crashes if the item list is empty or contains null values.

## Bug 3 – bug3.js
**Intended Behavior**: This function is intended to search for a specific user object within an array based on a provided ID and return the user's name.
**Issue Type**: Logical Error and Reference Error.
**Notes**: Uses assignment (=) instead of comparison (===) inside the loop and lacks a check for undefined users.

## Bug 4 – bug4.c
**Intended Behavior**: The goal is to iterate through a fixed-size integer array, print all 5 elements, and then perform a safe mathematical division.
**Issue Type**: Buffer Overflow and Arithmetic Exception.
**Notes**: The loop counter exceeds array bounds (i <= 10), and the program crashes due to a hardcoded division by zero.

