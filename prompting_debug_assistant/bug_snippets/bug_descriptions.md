# Bug Descriptions 


## Bug 1 – bug1.py

**Intended Behavior**: Calculate and return the average of a list of numbers.
**Issue Type**: Syntax errors.
**Notes**: The function is intended to iterate through a list, compute the total, and return the average. However, missing colons and parentheses prevent the program from running at all.


## Bug 2 – bug2.js

**Intended Behavior**: Count how many even numbers exist in an array.
**Issue Type**: Logical errors.
**Notes**: The `isEven` function incorrectly returns `false` for even numbers and `true` for odd numbers. Additionally, the counter decreases instead of increasing when an even number is found, resulting in incorrect negative values.


## Bug 3 – bug3.java

**Intended Behavior**: Print all names in uppercase from a list and then print the length of a string.
**Issue Type**: Runtime exceptions.
**Notes**: The loop condition allows access beyond the bounds of the list, causing an `IndexOutOfBoundsException`. The program also attempts to call a method on a null reference, leading to a `NullPointerException`.


## Bug 4 – bug4.cpp

**Intended Behavior**: Calculate and print the sum of all elements in an integer array.
**Issue Type**: Off-by-one / loop boundary error.
**Notes**: The loop starts from the wrong index and allows access past the end of the array, resulting in undefined behavior and incorrect summation.


## Bug 5 – bug5.py

**Intended Behavior**: Parse a JSON string, manipulate its values, and perform simple list operations.
**Issue Type**: Misuse of data types / library misuse.
**Notes**: The code incorrectly treats a JSON string as a dictionary, attempts to concatenate an integer with a string, and calls a string method on a list object, leading to runtime errors.
