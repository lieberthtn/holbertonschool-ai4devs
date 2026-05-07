# Project: Prompting Debug Assistant - Bug Descriptions

This repository contains 4 buggy code snippets across different languages (C++, Python, JS, C). Below is the structured description of each bug's intended functionality and known issues.

---

## Bug 1 – bug1.cpp
**Intended Behavior**: The goal of this program is to manage basic string operations. It should concatenate two input strings and display a success message to the user, confirming that the "calculator" logic is functioning correctly.
**Expected Outcome**: The program should compile, merge string A and B, and print "hesablayici isleyir".
**Issue Type**: Syntax Error & Type Mismatch.
**Detailed Notes**: 
- Compilation fails due to missing semicolons at variable declarations.
- Logic error: Multiplication of string objects is not defined in C++.
- Type error: Attempting to store a string concatenation result in an integer variable.

---

## Bug 2 – bug2.py
**Intended Behavior**: This script is designed to process user profile data. It should take a name, an age (integer), and a list of item prices. It is supposed to calculate the average price of those items and predict the user's age for next year.
**Expected Outcome**: "İstifadəçi emal olunur: Murad", "Gələn il yaşınız olacaq: 21", and the average price.
**Issue Type**: TypeError & Runtime Exception.
**Detailed Notes**: 
- The print statement fails because it tries to add a string and an integer without casting.
- The average calculation is prone to `ZeroDivisionError` if the list is empty.
- No null-check for items, which causes a crash if a price is `None`.

---

## Bug 3 – bug3.js
**Intended Behavior**: This JavaScript function is a search utility for a user database. Given an array of user objects and a target ID, it should locate the matching user and display their name.
**Expected Outcome**: If ID 2 is provided, it should return the object for "Veli" and log "Tapılan istifadəçi: Veli".
**Issue Type**: Logic Error & Reference Error.
**Detailed Notes**: 
- The loop counter `i` is leaked to the global scope (missing `let/var`).
- The `if` statement uses a single `=` (assignment) instead of `==` or `===` (comparison), making the search always return the first item incorrectly.
- Accessing properties on a potentially `null` result leads to a crash.

---

## Bug 4 – bug4.c
**Intended Behavior**: This C program should safely iterate through a small fixed-size array of 5 integers, print each value, and then perform a standard division operation.
**Expected Outcome**: Successful printing of 5 numbers and a valid division result without the program crashing.
**Issue Type**: Buffer Overflow & Arithmetic Exception.
**Detailed Notes**: 
- The loop condition `i <= 10` is an "off-by-one" and "out-of-bounds" error since the array only has 5 elements.
- The program crashes with a "Floating point exception" due to a hardcoded division by zero.
