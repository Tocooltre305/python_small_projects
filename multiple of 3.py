def multiple_of_3():
    multiple_for_3 = 0
    while True:
        num = input("Enter a number (q to quit): ").lower()
        if num == "q":
            break
        num = int(num)
        if num % 3 == 0:
            print("Number is multiple of 3")
            multiple_for_3 += 1
        elif num % 3 != 0:
            print("Number is not multiple of 3")
    return multiple_for_3 
count = multiple_of_3()
print(f"Numbers that are multiple of 3: {count}")