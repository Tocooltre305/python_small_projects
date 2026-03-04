def divisible_by_two_counter():
    divisible_2 = 0
    while True:
        num = input("Enter a number (q to quit): ")
        if num == "q":
            break
        num = int(num)
        if num % 2 == 0:
            print("Number is divisible by 2")
            divisible_2 += 1
        else:
            print("Number is not divisible by 2")
    return divisible_2 
count = divisible_by_two_counter()
print(f"Numbers entered that are divisible by 2: {count}")