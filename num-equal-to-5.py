def five_counter():
    equal_5 = 0
    while True:
        num = input("Enter a number (q to quit): ").lower()
        if num == "q":
            break
        num = int(num)
        if num == 5:
            print("Number is 5")
            equal_5 += 1
        elif num != 5:
            print("Number is not 5")
    return equal_5 
count = five_counter()
print(f"Numbers entered that are 5: {count}")