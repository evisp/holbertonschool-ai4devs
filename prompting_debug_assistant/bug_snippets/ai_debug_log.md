## Bug 1 – bug1.py

**AI Diagnosis**: The code has multiple **SyntaxError** causes: missing `:` after the function definition (`def calculate_average(numbers)`), missing `:` after the `for` statement (`for n in numbers`), and an unclosed `print(` call in the `if count == 0:` block (`print("No numbers provided"`). These prevent the file from parsing/executing at all. 

**Suggested Fix**: Add the missing colons and close the `print()` parenthesis (and keep the `return` on its own valid line), e.g.:

```python
def calculate_average(numbers):
    total = 0
    count = len(numbers)

    for n in numbers:
        total += n

    if count == 0:
        print("No numbers provided")
        return 0

    return total / count
```
Missing colons and mismatched parentheses are common Python syntax issues and must be corrected for the interpreter to run the code. 

**Alternative Fixes Tested**: None.  
**Result**: Fix works as expected (prints `Average: 20.0`).


## Bug 2 – bug2.js

**AI Diagnosis**: `isEven()` returns the opposite boolean (it returns `false` when `number % 2 == 0`, i.e., when the number is even), so the predicate is inverted. [stackoverflow]

**Suggested Fix**: Flip the returns (or just return the condition) so evens produce `true`:
```js
function isEven(number) {
  return number % 2 === 0;
}
```
Using `% 2 === 0` is the standard even-check in JavaScript. 

**Alternative Fixes Tested**: Fix the counting logic too: inside `countEvens`, you currently do `count--` when an even is found, which makes the count go negative; it should be `count++` (or compute via `filter`).  

**Result**: After `isEven` is corrected and `count--` is changed to `count++`, `countEvens([2,4,6,7,9])` returns `3` and logs `Even count: 3`.


## Bug 3 – bug3.java

**AI Diagnosis**: The `for` loop uses `i <= names.size()`, so on the last iteration `i == names.size()` and `names.get(i)` throws `IndexOutOfBoundsException` (valid indices are `0` to `names.size() - 1`).  

**Suggested Fix**: Change the loop condition to `i < names.size()`:

```java
for (int i = 0; i < names.size(); i++) {
    System.out.println(names.get(i).toUpperCase());
}
```

**Alternative Fixes Tested**: Use an enhanced for-loop to avoid indexing entirely:

```java
for (String name : names) {
    System.out.println(name.toUpperCase());
}
```

**Result**: The loop prints both names without throwing `IndexOutOfBoundsException`.



## Bug 4 – bug4.cpp

**AI Diagnosis**: The loop starts at `i = 1` (skipping `arr[0]`) and runs while `i <= 5`, which accesses `arr[5]` on the last iteration; that index is out of bounds for `int arr[5]` (valid indices are `0..4`), leading to undefined behavior and incorrect/unstable results. 

**Suggested Fix**: Iterate from `0` up to (but not including) `5`:

```cpp
for (int i = 0; i < 5; i++) {
    sum += arr[i];
}
```

**Alternative Fixes Tested**: Derive the length from the array to avoid hard-coding and future off-by-one mistakes:

```cpp
int n = sizeof(arr) / sizeof(arr[0]);
for (int i = 0; i < n; i++) sum += arr[i];
```

**Result**: Sum is computed correctly as `15` and no out-of-bounds access occurs.



## Bug 1 – bug5.py
**AI Diagnosis**: `data` is a JSON *string*, not a Python dict, so `data["name"]` tries to index a string with another string and raises `TypeError: string indices must be integers`.  
**Suggested Fix**: Parse first, then index the resulting dict:
```py
parsed = json.loads(data)
print(parsed["name"])
```
**Alternative Fixes Tested**: None.  
**Result**: `"Alice"` prints correctly.