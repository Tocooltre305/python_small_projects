def even_number():
   while True:
        num = input("Enter a number (or quit): ").lower()
        if num == "quit":
            break
        num = int(num)
        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")
even_number()