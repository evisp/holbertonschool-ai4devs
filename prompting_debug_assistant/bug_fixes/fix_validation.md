## Bug 1 – bug1_fixed.py

- **Input**: [10, 20, 30]  
- **Expected Output**: 20  
- **Actual Output**: 20 ✅  
- **Test Method**: `assert calculate_average([10, 20, 30]) == 20`

- **Input**: []  
- **Expected Output**: 0 (and prints "No numbers provided")  
- **Actual Output**: 0 ✅  
- **Test Method**: `assert calculate_average([]) == 0` (print verified by running)


## Bug 2 – bug2_fixed.js
- **Input**: [2, 4, 6, 7, 9]  
- **Expected Output**: 3  
- **Actual Output**: 3 ✅  
- **Test Method**: `console.log("Even count:", countEvens(numbers))`

- **Input**: []  
- **Expected Output**: 0  
- **Actual Output**: 0 ✅  
- **Test Method**: `console.log(countEvens([]) === 0)`

- **Input**: [1, 3, 5]  
- **Expected Output**: 0  
- **Actual Output**: 0 ✅  
- **Test Method**: `console.log(countEvens([1,3,5]) === 0)`

- **Input**: [0, -2, -3]  
- **Expected Output**: 2  
- **Actual Output**: 2 ✅  
- **Test Method**: `console.log(countEvens([0,-2,-3]) === 2)`


## Bug 3 – Bug3_fixed.java
- **Input**: names = ["Alice", "Bob"]  
- **Expected Output**: Prints `ALICE` then `BOB`  
- **Actual Output**: Prints `ALICE` then `BOB` ✅  
- **Test Method**: Run program; loop uses `i < names.size()`

- **Input**: value = null  
- **Expected Output**: No `NullPointerException` (prints `0` as fallback)  
- **Actual Output**: Prints `0` ✅  
- **Test Method**: Run program; null check before `value.length()`


## Bug 4 – bug4_fixed.cpp
- **Input**: arr = [1, 2, 3, 4, 5]  
- **Expected Output**: Sum: 15  
- **Actual Output**: Sum: 15 ✅  
- **Test Method**: Run program; also checks `if (sum != 15) return 1`


## Bug 5 – bug5_fixed.py
- **Input**: data = '{"name": "Alice", "age": 30}'  
- **Expected Output**: Alice  
- **Actual Output**: Alice ✅  
- **Test Method**: `assert parsed["name"] == "Alice"`

- **Input**: age = 30, + 5  
- **Expected Output**: New age: 35  
- **Actual Output**: New age: 35 ✅  
- **Test Method**: `assert new_age == 35`

- **Input**: numbers = [1, 2, 3, 4]  
- **Expected Output**: ['1', '2', '3', '4']  
- **Actual Output**: ['1', '2', '3', '4'] ✅  
- **Test Method**: `assert result == ["1", "2", "3", "4"]`

- **Manual Tweaks Needed**: Yes — original `numbers.split(",")` is invalid because `numbers` is already a list; replaced with a clear, type-consistent transformation to a list of string tokens.
