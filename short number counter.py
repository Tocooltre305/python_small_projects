def short_number_counter():
    short_number = 0
    while True:
        num = input("Enter a number (q to quit): ").lower()
        if num == "q":
            break
        num = int(num)
        if num < 10:
            print("Short number")
            short_number += 1
        elif num <= 10:
            print("Long number")
    return short_number 
count = short_number_counter()
print(f"Short numbers entered: {count}")