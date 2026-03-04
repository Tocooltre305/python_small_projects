def less_than_5():
    less_5 = 0
    while True:
        num = input("Enter a number (q to quit): ").lower()
        if num == "q":
            break
        num = int(num)
        if num < 5:
            print("Less than 5")
            less_5 += 1
        elif num > 5:
            print("More than 5")
        else:
            print("Number is five")    
    return less_5
count = less_than_5()
print(f"Numbers entered less than 5: {count}")