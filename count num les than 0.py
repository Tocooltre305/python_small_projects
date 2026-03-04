def less_than_0():
    less_0 = 0
    while True:
        num = input("Enter a number (q to quit): ")
        if num.lower() == "q":
            break
        
        num = float(num)
        
        if num < 0:
            print("Number is less than 0")
            less_0 += 1
        elif num > 0:
            print("Number is not less than 0")
        else:
            print("Number is zero")
            
    return less_0

count = less_than_0()
print(f"Numbers entered that are less than 0: {count}")