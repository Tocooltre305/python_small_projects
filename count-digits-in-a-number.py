def count_digits(number):
    num = abs(number)
    if num == 0:
        return 1
    digit_count = 0
    while True:
        if num == 0:
            break 
        num = num // 10  
        digit_count += 1
    return digit_count
test_num = int(input("Enter a whole number: "))
result = count_digits(test_num)
print(f"The number {test_num} has {result} digits.")