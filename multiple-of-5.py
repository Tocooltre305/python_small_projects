def multiple_of_5():
    multiple_for_5 = 0
    while True:
        num = input("Enter a number (q to quit): ").lower()
        if num == "q":
            break
        num = int(num)
        if num % 5 == 0:
            print("Number is multiple of 5")
            multiple_for_5 += 1
        elif num % 5 != 0:
            print("Number is not multiple of 5")
    return multiple_for_5 
count = multiple_of_5()
print(f"Numbers entered that are multiple of 5: {count}")