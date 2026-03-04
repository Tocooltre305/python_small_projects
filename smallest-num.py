def find_smallest_in_user_input():
    numbers = []
    while True:
        user_input = input("Enter a number (or 'done' to finish): ").lower()
        if user_input == 'done':
            break
        try:
            val = int(user_input)
            numbers.append(val)
        except ValueError:
            print("Invalid input.")
    if not numbers:
        return None
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest
result = find_smallest_in_user_input()
print(f"Smallest: {result}")