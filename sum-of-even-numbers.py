def sum_even_inputs():
    total_sum = 0
    while True:
        num_input = input("Enter a number (q to quit): ")
        if num_input.lower() == "q":
            break
        num = int(num_input)
        if num % 2 == 0:
            print(f"{num} is even. Adding to total.")
            total_sum += num
        else:
            print(f"{num} is odd. Skipping.")
    return total_sum
result = sum_even_inputs()
print("-" * 20)
print(f"The total sum of even numbers entered is: {result}")