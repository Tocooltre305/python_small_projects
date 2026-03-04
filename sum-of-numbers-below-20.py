def sum_numbers_below_20():
    total_sum = 0
    while True:
        num_input = input("Enter a number (q to quit): ")
        if num_input.lower() == "q":
            break
        num = float(num_input)
        if num < 20:
            print(f"{num} is less than 20. Adding to sum.")
            total_sum += num 
        else:
            print(f"{num} is 20 or greater. Skipping.")
    return total_sum
result = sum_numbers_below_20()
print(f"---")
print(f"The total sum of numbers below 20 is: {result}")