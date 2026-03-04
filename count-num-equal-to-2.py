def equal_to_2_counter():
    two = 0
    while True:
        num = input("Enter a number (q to quit): ")
        if num == "q":
            break
        num = int(num)
        if num == 2:
            print("Number is 2")
            two += 1
        elif num  != 2:
            print("Number is not 2")
    return two
count = equal_to_2_counter()
print(f"Numbers entered that are equal to 2: {count}")