def sum_positive_numbers(numbers):
    total = 0
    for num in numbers:
        if num > 0:
            total += num
    return total
user_input = input("Enter a list of numbers separated by spaces: ")
try:
    num_list = [float(x) for x in user_input.split()]
    final_sum = sum_positive_numbers(num_list)
    print(f"\nYour list: {num_list}")
    print(f"The sum of only the positive numbers is: {final_sum}")
except ValueError:
    print("Oops! Please make sure you only enter numbers.")