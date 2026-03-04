def long_number_counter():
    long_number = 0
    while True:
        num = input("Enter a number (q to quit): ").lower()
        if num == "q":
            break
        num = int(num)
        if num >= 10:
            print("Long number")
            long_number += 1
        elif num < 10:
            print("Short number")
    return long_number 
count = long_number_counter()
print(f"Long numbers entered: {count}")