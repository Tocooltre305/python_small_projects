def count_true_values():
    true_count = 0
    while True:
        entry = input("Enter True or False (q to quit): ").lower().strip()
        if entry == "q":
            break
        if entry == "true":
            val = True
        elif entry == "false":
            val = False
        else:
            print("Not a boolean value, try again.")
            continue 
        if val == True:
            print("Value is True")
            true_count += 1
        else:
            print("Value is False")
    return true_count
count = count_true_values()
print(f"Total True values entered: {count}")