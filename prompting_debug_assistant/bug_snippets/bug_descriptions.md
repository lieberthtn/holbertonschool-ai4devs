# Project: Prompting Debug Assistant - Bug Descriptions

This repository contains a collection of 4 flawed code snippets used for AI-assisted debugging analysis. Each section below follows a standardized format to ensure clarity and consistency.

---

## Bug 1 – bug1.cpp
**Intended Behavior**: The program is designed to perform basic string manipulation. It should initialize two strings, concatenate them to form a single message, and print a confirmation indicating the calculator logic is active.
**Expected Outcome**: The console should display the concatenated string and the text "hesablayici isleyir" without any errors.
**Issue Type**: Syntax Error and Type Mismatch.
**Technical Notes**: 
- Compilation fails because of missing semicolons after variable declarations.
- It contains a type mismatch where a string concatenation is assigned to an integer variable.
- The use of the multiplication operator on strings is unsupported in C++.
- A stray 'x' character at the end causes a terminal syntax error.

---

## Bug 2 – bug2.py
**Intended Behavior**: This function is intended to manage a user's profile and shopping data. It calculates the user's age for the next year and determines the average price of items from a provided list.
**Expected Outcome**: Successful printing of the user's name, their updated age (e.g., 21), and the correctly calculated average price of the items.
**Issue Type**: TypeError and Runtime Logic Exception.
**Technical Notes**: 
- A `TypeError` occurs when trying to concatenate a string with an integer in the print statement.
- The script is vulnerable to a `ZeroDivisionError` if the items list is empty during average calculation.
- The logic fails to account for `None` values in the price list, leading to an application crash.

---

## Bug 3 – bug3.js
**Intended Behavior**: This script serves as a search utility for a user database. It iterates through an array of objects to find a user by their unique ID and logs the corresponding name to the console.
**Expected Outcome**: If a valid ID is provided, the system should log "Tapılan istifadəçi: [Name]" and return the user object.
**Issue Type**: Reference Error and Logical Assignment Error.
**Technical Notes**: 
- The loop variable `i` is not declared, causing it to leak into the global scope.
- An assignment operator `=` is mistakenly used instead of a comparison operator `===` inside the `if` block, making the condition always evaluate to true.
- The program will crash if the user is not found because it tries to access properties of a `null` object.

---

## Bug 4 – bug4.c
**Intended Behavior**: The program's purpose is to iterate through a fixed-size integer array, print its elements one by one, and then execute a simple division operation.
**Expected Outcome**: The program should print exactly 5 integers and complete the division without any runtime crashes or memory leaks.
**Issue Type**: Buffer Overflow and Arithmetic Exception.
**Technical Notes**: 
- A buffer overflow occurs because the loop condition `i <= 10` exceeds the array boundary of 5, leading to a potential segmentation fault.
- The program suffers an immediate crash (SIGFPE) due to an unhandled division by zero.
- The lack of bounds checking results in undefined behavior during execution.
