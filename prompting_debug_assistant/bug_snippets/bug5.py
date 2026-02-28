# bug5.py
# Category: Misuse of Data Types / Libraries

import json

data = '{"name": "Alice", "age": 30}'

# Incorrect assumption that json string behaves like dictionary
print(data["name"])

parsed = json.loads(data)

# Misuse of data type
age = parsed["age"]
new_age = age + "5"

print("New age:", new_age)

numbers = [1, 2, 3, 4]
result = numbers.split(",")

print(result)