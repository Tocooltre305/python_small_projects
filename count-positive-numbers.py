def check_numbers():
    while True:
        num = float(input("Enter a number: "))
        
        if num > 0:
            print("Positive")
        elif num < 0:
            print("Negative")
        else:
            print("Zero")

check_numbers()