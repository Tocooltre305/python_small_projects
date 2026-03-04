def sum_less_than_10():
    total = 0
    while True:
        entry = input("Enter a number (or 'q' to quit): ").lower()
        if entry == 'q':
            break
        
        num = int(entry)
        if num < 10:
            print(f" -> {num} is less than 10, adding it.")
            total += num
        else:
            print(f" -> {num} is 10 or greater, skipping.")
            
    return total

grand_total = sum_less_than_10()
print(f"\nThe final sum of numbers < 10 is: {grand_total}")