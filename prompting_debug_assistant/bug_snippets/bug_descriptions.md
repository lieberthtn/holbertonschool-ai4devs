# Project: Prompting Debug Assistant - Bug Descriptions

This document outlines the intended behavior, identified issues, and technical constraints for the provided buggy code snippets.

---

## 1. Bug 1 – bug1.cpp
**Intended Behavior**: The program is designed to initialize two strings, concatenate them, and perform a simulated multiplication (repetition) or additional logic, finally printing a success message.
**Expected Output**: A clean execution showing concatenated strings and the message "hesablayici isleyir".
**Issue Type**: Syntax, Type Mismatch, and Garbage Characters.
**Technical Notes**: 
- Missing semicolons (`;`) lead to compilation failure.
- In C++, you cannot multiply two `std::string` objects using the `*` operator.
- Assigning a string concatenation result to an `int` variable (`c = a + b`) causes a type mismatch.
- Stray character `x` before the closing brace is invalid syntax.

---

## 2. Bug 2 – bug2.py
**Intended Behavior**: A function that takes a user's name, age, and a list of item prices. it should calculate the average price and predict the user's age for the following year.
**Expected Output**: "İstifadəçi emal olunur: Murad", "Gələn il yaşınız olacaq: 21", and the average price.
**Issue Type**: Logical Error, TypeError, and Runtime Exception.
**Technical Notes**: 
- `TypeError`: Cannot concatenate `str` and `int` without explicit casting using `str()`.
- `ZeroDivisionError`: The code fails if the `items` list is empty.
- `Logic Error`: Iterating through a list containing `None` values without a check causes a `TypeError` during summation.

---

## 3. Bug 3 – bug3.js
**Intended Behavior**: This script searches through a user database (array of objects) to find a specific user by their unique ID and prints their name.
**Expected Output**: "Tapılan istifadəçi: Veli" (if searching for ID 2).
**Issue Type**: ReferenceError and Logic/Assignment Error.
**Technical Notes**: 
- Implicit Global: Variable `i` is not declared with `let` or `const`.
- Logic Error: Using a single equals sign `=` inside an `if` statement performs an assignment instead of a comparison, causing it to always be true for non-zero IDs.
- Runtime Error: If no user is found, `foundUser` remains `null`, and accessing `foundUser.name` crashes the script.

---

## 4. Bug 4 – bug4.c
**Intended Behavior**: The program should iterate through a fixed-size integer array, print each element, and perform a simple mathematical division.
**Expected Output**: Printing numbers 1 through 5 and completing without a crash.
**Issue Type**: Runtime Exception (Segmentation Fault & SIGFPE).
**Technical Notes**: 
- Buffer Overflow: The loop condition `i <= 10` exceeds the array size (5), leading to undefined behavior or memory corruption.
- Arithmetic Exception: Division by zero (`x / y` where `y = 0`) causes the program to terminate abruptly.
