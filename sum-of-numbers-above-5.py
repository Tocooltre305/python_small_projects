def sum_more_than_5():
    total = 0
    while True:
        entry = input("Enter a number (or 'q' to quit): ").lower()
        if entry == 'q':
            break
        
        num = int(entry)
        if num > 5:
            print(f" -> {num} is greater than 5, adding it.")
            total += num
        elif num == 5:
            print(f"-> {num} is equal to 5, adding it")
            total += num
        else:
            print(f" -> {num} is less than 5, skipping.")
            
    return total

grand_total = sum_more_than_5()
print(f"\nThe final sum of numbers < 5 is: {grand_total}")