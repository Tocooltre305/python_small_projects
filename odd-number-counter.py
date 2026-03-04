def odd_or_even():
    odd_num = 0
    while True:
        num = input("Enter a number (q to quit): ")
        if num == "q":
            break
        num = int(num)
        if num % 2 == 0:
            print("Even number")
            odd_num += 1
        elif num % 2 != 0:
            print("Odd number")
        else:
            print("Is 0")
    return odd_num 
count = odd_or_even()
print(f"Numbers entered are odd: {count}")