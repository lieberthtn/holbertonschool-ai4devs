# Bug Descriptions

## bug1.py
- **Intended Behavior**: Return the last n items in a list.
- **Current Issue**: Off-by-one error in slicing logic causing it to skip an element.

## bug2.js
- **Intended Behavior**: Fetch and return updated data after a delay.
- **Current Issue**: Missing await/promise logic; returns initial value before update.

## bug3.java
- **Intended Behavior**: Compare a string variable with a literal safely.
- **Current Issue**: Throws NullPointerException because the variable is null.

## bug4.cpp
- **Intended Behavior**: Store a value in a pointer and print it.
- **Current Issue**: Dereferencing an uninitialized pointer (Undefined Behavior).
