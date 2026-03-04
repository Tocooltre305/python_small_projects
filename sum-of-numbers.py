def calculate_sum():
    numbers = []
    while True:
        user_input = input("Enter a number (or 'done' to see total): ").lower()
        if user_input == 'done':
            break
        num = float(user_input)
        numbers.append(num)
    total = 0
    for n in numbers:
        total += n
    return total
result = calculate_sum()
print(f"The total sum is: {result}")