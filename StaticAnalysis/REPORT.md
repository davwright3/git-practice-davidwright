# This is the report my David Wright's static analysis assignment

## Running Static Analysis

### Step 1: Flake8

main.py:1:1: F401 'math' imported but unused

main.py:2:1: F401 'random' imported but unused

main.py:3:1: W293 blank line contains whitespace  cd 

main.py:4:1: E302 expected 2 blank lines, found 1

main.py:9:1: W293 blank line contains whitespace

main.py:10:1: E302 expected 2 blank lines, found 1

main.py:15:1: W293 blank line contains whitespace

main.py:16:1: E302 expected 2 blank lines, found 1

main.py:21:1: W293 blank line contains whitespace

main.py:22:1: E302 expected 2 blank lines, found 1

main.py:24:5: F841 local variable 'output' is assigned to but never used

main.py:26:1: W293 blank line contains whitespace

main.py:27:1: E305 expected 2 blank lines after class or function definition, found 1


### Step 2: Pylint
************* Module main

main.py:3:0: C0303: Trailing whitespace (trailing-whitespace)

main.py:9:0: C0303: Trailing whitespace (trailing-whitespace)

main.py:15:0: C0303: Trailing whitespace (trailing-whitespace)

main.py:21:0: C0303: Trailing whitespace (trailing-whitespace)

main.py:26:0: C0303: Trailing whitespace (trailing-whitespace)

main.py:1:0: C0114: Missing module docstring (missing-module-docstring)

main.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)

main.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)

main.py:16:0: C0116: Missing function or method docstring (missing-function-docstring)

main.py:22:0: C0116: Missing function or method docstring (missing-function-docstring)

main.py:24:4: W0612: Unused variable 'output' (unused-variable)

main.py:1:0: W0611: Unused import math (unused-import)

main.py:2:0: W0611: Unused import random (unused-import)

------------------------------------------------------------------
Your code has been rated at 4.35/10 (previous run: 4.35/10, +0.00)

### Step 3: Line Profiler
Timer unit: 1e-07 s

Total time: 0.155216 s
File: C:\UALR\Spring 2025\Modern Software Development\git-practice-davidwright\staticanalysis\main.py
Function: slow_func at line 12

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    12                                           def slow_func(lst):
    13         1          3.0      3.0      0.0      result = []
    14      1001       1371.0      1.4      0.1      for i in range(len(lst)):
    15      1000    1550781.0   1550.8     99.9          result.append(expensive_op(i))
    16         1          2.0      2.0      0.0      return result

Done

## Static Analysis Fixes

### Flake8 and Pylint
Got rid of white space in empty lines

Added blank lines where they were expected

Did not use random, so removed the import

Added docstrings for module and methods.

Result:

(.venv) PS C:\UALR\Spring 2025\Modern Software Development\git-practice-davidwright\staticanalysis> flake8 main.py

(.venv) PS C:\UALR\Spring 2025\Modern Software Development\git-practice-davidwright\staticanalysis> 


(.venv) PS C:\UALR\Spring 2025\Modern Software Development\git-practice-davidwright\staticanalysis> pylint main.py

-------------------------------------------------------------------

Your code has been rated at 10.00/10 (previous run: 9.33/10, +0.67)



### Line Profiler
Using math and some ChatGPT help, expensive_op got pared down to a new formula, 'return n* math.prod([999,1000])//2'

This went into a single function to iterate through all of the numebrs.

This cut the times per hit down significantly, from 1550 ms to 1.5 ms

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     9                                           def slow_func(lst):
    10                                               """Function receives a list of numbers as an input and returns the number factored to 1000"""
    11         1         14.0     14.0      0.9      factor = math.prod([999, 1000])//2
    12      1001       1500.0      1.5     99.1      return [i*factor for i in lst]


