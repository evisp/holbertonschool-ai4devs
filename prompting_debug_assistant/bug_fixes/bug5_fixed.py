# bug5_fixed.py
# Category: Misuse of Data Types / Libraries

import json

data = '{"name": "Alice", "age": 30}'

# Fix 1: parse JSON string into a dict before key access
parsed = json.loads(data)
print(parsed["name"])

# Fix 2: age is an int; do numeric addition (or cast if you intended a string)
age = parsed["age"]
new_age = age + 5
print("New age:", new_age)

# Fix 3: split() is a string method; either split a string or just use the list as-is
numbers = [1, 2, 3, 4]
result = [str(n) for n in numbers]  # consistent "split-like" list of string tokens
print(result)

# Tests (assertions)
assert parsed["name"] == "Alice"
assert parsed["age"] == 30
assert new_age == 35
assert result == ["1", "2", "3", "4"]

