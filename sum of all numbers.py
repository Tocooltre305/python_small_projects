def sum_all_numbers(numbers_list):
    total = 0
    for num in numbers_list:
        total += num
    return total
user_numbers = []  
while True:
    entry = input("Enter a number (or 'q' to finish): ").lower()
    if entry == 'q':
        break
    num = int(entry)
    user_numbers.append(num)
grand_total = sum_all_numbers(user_numbers)
print(f"\nYour list: {user_numbers}")
print(f"The total sum is: {grand_total}")