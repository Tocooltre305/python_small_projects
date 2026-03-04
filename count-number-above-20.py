def above_twenty_counter():
    twenty_or_above = 0
    while True:
        num = input("Enter a number (q to quit): ")
        if num == "q":
            break
        num = int(num)
        if num > 20:
            print("Number > 20")
            twenty_or_above += 1
        elif num  <= 20:
            print("Number is or not greater than 20")
    return twenty_or_above 
count = above_twenty_counter()
print(f"Numbers entered that are greater than 20: {count}")