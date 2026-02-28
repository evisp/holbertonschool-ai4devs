# Bug Fix Reports (Overview)

This document records the bugs found across the provided exercises and how each one was fixed. Each report includes a short description of what broke, why it broke, what was changed to fix it (including any manual edits beyond the initial suggested fix), and a practical lesson to avoid repeating the mistake.

## Bug Fix Report — bug1.py (Syntax errors)
- **Summary**: Code fails to run due to multiple syntax errors (missing colons and an unclosed `print()` call).  
- **Root Cause**: Block statements (`def`, `for`, `if`) were missing required `:` and `print("No numbers provided"` was missing a closing `)`, so the interpreter cannot parse the file.  
- **Resolution (AI suggestion + manual edits)**: Added missing `:` and closed the `print()` parenthesis, ensured indentation is consistent; added `assert` checks to validate behavior for a normal list and an empty list.  
- **Lessons learned**: Fix parsing errors first; then add small assertions to confirm expected results for common and edge inputs.

## Bug Fix Report — bug2.js (Logical errors)
- **Summary**: Even-count logic returns the wrong result (often negative) because the “even” check and counter update are inverted.  
- **Root Cause**: `isEven()` returns `false` for even numbers, and `countEvens()` decrements (`count--`) when an even is found.  
- **Resolution (AI suggestion + manual edits)**: Updated `isEven` to return `number % 2 === 0` and changed `count--` to `count++`; added console-based checks for empty and mixed arrays.  
- **Lessons learned**: Validate helper predicates with a couple of known values, and verify counters with a simple test case where the answer is obvious.

## Bug Fix Report — bug3.java (Runtime exceptions)
- **Summary**: Program throws runtime exceptions: out-of-bounds access in the loop and a null dereference on `value.length()`.  
- **Root Cause**: Loop condition used `i <= names.size()`, so it attempts `names.get(names.size())`; `value` was explicitly set to `null` and then dereferenced.  
- **Resolution (AI suggestion + manual edits)**: Changed loop to `i < names.size()`; added a null check and printed a safe fallback (`0`) when `value` is null; added simple sanity assertions.  
- **Lessons learned**: For collections, iterate with `< size()` (not `<= size()`), and guard against null before calling methods.

## Bug Fix Report — bug4.cpp (Off-by-one / loop logic)
- **Summary**: Sum calculation is incorrect/unstable due to out-of-bounds array access and skipping the first element.  
- **Root Cause**: Loop starts at `i = 1` (skips `arr[0]`) and runs while `i <= 5`, which accesses `arr[5]` (out of bounds for a 5-element array).  
- **Resolution (AI suggestion + manual edits)**: Iterated from `i = 0` to `i < 5`; added a basic runtime check that fails if `sum` is not 15.  
- **Lessons learned**: Use correct index ranges (`0..n-1`) and add a simple known-result check for small fixed arrays.

## Bug Fix Report — bug5.py (Misuse of data types / libraries)
- **Summary**: Script crashes due to multiple type misuses: indexing a string as a dict, mixing int + string, and calling `split()` on a list.  
- **Root Cause**: JSON text was treated like a Python dict (`data["name"]`), `age` (int) was combined with `"5"` (string), and `.split()` was used on a list instead of a string.  
- **Resolution (AI suggestion + manual edits)**: Parsed JSON first (`json.loads`), used numeric addition for age (`age + 5`), and replaced the invalid “split list” step with a clear conversion to string tokens (`[str(n) for n in numbers]`); documented that manual change in validation notes.  
- **Lessons learned**: Confirm data types before indexing or calling methods, and keep numeric operations numeric unless you explicitly intend string formatting.

## Short summary
Across all files, the issues fell into three common categories: syntax problems that prevent code from running, logic inversions/off-by-one mistakes that produce wrong results, and runtime/type errors caused by invalid indexing or calling methods on the wrong type (or on null). The fixes focused on correcting boundaries and predicates, enforcing safe access patterns (loop conditions and null checks), and adding minimal automated checks (assertions or console logs) to validate expected behavior.
