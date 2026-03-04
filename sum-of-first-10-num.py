def sum_first_10():
    total = 0
    for num in range(1, 11):
        total += num
        print(f"Adding {num}... Current total: {total}")
    return total
result = sum_first_10()
print(f"\nThe final sum of numbers 1 to 10 is: {result}")