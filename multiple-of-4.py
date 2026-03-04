def multiple_of_4():
    multiple_for_4 = 0
    while True:
        num = input("Enter a number (q to quit): ").lower()
        if num == "q":
            break
        num = int(num)
        if num % 4 == 0:
            print("Number is multiple of 4")
            multiple_for_4 += 1
        elif num % 4 != 0:
            print("Number is not multiple of 4")
    return multiple_for_4 
count = multiple_of_4()
print(f"Numbers that are multiple of 4: {count}")