## Bug 1 – bug1_fixed.cpp
- **Input**: a = "10", b = "20"
- **Expected Output**: c= 1020, hesablayici isleyir
- **Actual Output**: c= 1020, hesablayici isleyir ✅
- **Note**: Manual tweak: Added #include <string> and removed invalid multiplication logic.

## Bug 2 – bug2_fixed.py
- **Input**: name="Murad", age=20, items=[{"price": 20}, {"price": 30}, {"price": None}]
- **Expected Output**: User processing: Murad, Next year you will be: 21, Affordable price.
- **Actual Output**: User processing: Murad, Next year you will be: 21, Affordable price. ✅
- **Note**: Added None-check for prices and handled empty list case.

## Bug 3 – bug3_fixed.js
- **Input**: userList, id = 3 (non-existent)
- **Expected Output**: User not found.
- **Actual Output**: User not found. ✅
- **Input**: userList, id = 1
- **Expected Output**: Found user: Ali
- **Actual Output**: Found user: Ali ✅
- **Note**: Fixed comparison operator and added null-check for foundUser.

## Bug 4 – bug4_fixed.c
- **Input**: Array of 5 elements, divisor y=2
- **Expected Output**: Prints 5 numbers and Result: 5
- **Actual Output**: Prints 5 numbers and Result: 5 ✅
- **Note**: Fixed array out-of-bounds loop and prevented division by zero.
