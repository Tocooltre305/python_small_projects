start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

even_sum = 0
odd_sum = 0

for num in range(start, end + 1):
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")
