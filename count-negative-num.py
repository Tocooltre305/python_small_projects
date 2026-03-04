def count_negatives():
    negative_num = 0
    while True:
        num = input("Enter a number (q to quit): ").lower()
        if num == "q":
            break
        num = int(num)
        if num < 0:
            print("Number is negative")
            negative_num += 1
        elif num > 0:
            print("Number is positive")
        else:
            print("Number is zero")
            
    return negative_num 
count = count_negatives()
print(f"Number of negative numbers entered: {count}")