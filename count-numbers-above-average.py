def count_above_average():
    numbers = [] 
    while True:
        val = input("Enter a number (q to quit): ").lower()
        if val == "q":
            break
        numbers.append(float(val)) 
    if len(numbers) == 0:
        return 0
    total_sum = 0
    i = 0
    while i < len(numbers):
        total_sum += numbers[i]
        i += 1
    average = total_sum / len(numbers)
    print(f"The average is: {average}")
    above_count = 0
    j = 0
    while j < len(numbers):
        if numbers[j] > average:
            print(f"{numbers[j]} is above average!")
            above_count += 1
        else:
            print(f"{numbers[j]} is not above average.")
        j += 1
    return above_count
count = count_above_average()
print(f"Total numbers above average: {count}")