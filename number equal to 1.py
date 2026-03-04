def equal_to_1():
    equal_1 = 0
    while True:
        num = input("Enter a number (q to quit): ").lower()
        if num == "q":
            break
        num = int(num)
        if num == 1:
            print("Number is 1")
            equal_1 += 1
        elif num != 1:
            print("Number is not 1")  
    return equal_1
count = equal_to_1()
print(f"Numbers entered equal to 1: {count}")