number = int(input("Enter a number: "))
total_sum = 0

while number > 0:
    digit = number % 10
    total_sum += digit
    number //= 10

print("Sum of digits:", total_sum)