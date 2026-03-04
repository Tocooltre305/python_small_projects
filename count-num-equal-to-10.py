def equal_to_10_counter():
    ten = 0
    while True:
        num = input("Enter a number (q to quit): ")
        if num == "q":
            break
        num = int(num)
        if num == 10:
            print("Number is 10")
            ten += 1
        elif num  != 10:
            print("Number is not 10")
    return ten
count = equal_to_10_counter()
print(f"Numbers entered that are equal to 10: {count}")