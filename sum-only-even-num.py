def sum_even_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total
user_input = input("Enter numbers separated by spaces: ")
num_list = [int(x) for x in user_input.split()]
result = sum_even_numbers(num_list)
print(result)