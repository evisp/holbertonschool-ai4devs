# bug1_fixed.py
# Category: Syntax Errors


def calculate_average(numbers):
    total = 0
    count = len(numbers)

    for n in numbers:
        total += n

    if count == 0:
        print("No numbers provided")
        return 0

    return total / count


values = [10, 20, 30]
avg = calculate_average(values)
print("Average:", avg)

# Tests (assertions)
assert calculate_average([10, 20, 30]) == 20
assert calculate_average([]) == 0
