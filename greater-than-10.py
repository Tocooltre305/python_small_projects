def greater_than_10():
    more_than_10 = 0
    while True:
        num = input("Enter a number (q to quit): ")
        if num == "q":
            break
        num = int(num)
        if num > 10:
            print("Greater than 10")
            more_than_10 += 1
        elif num < 10:
            print("Less than 10")
        else:
            print("Equal to 10")
    return more_than_10 
count = greater_than_10()
print(f"Numbers entered greater than 10: {count}")