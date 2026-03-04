def zero_counter():
    zero_num = 0
    while True:
        num = input("Enter a number (q to quit): ")
        if num == "q":
            break
        num = int(num)
        if num == 0:
            print("Number is zero")
            zero_num += 1
        elif num  != 0:
            print("number is not zero")
    return zero_num 
count = zero_counter()
print(f"Numbers entered that are 0: {count}")