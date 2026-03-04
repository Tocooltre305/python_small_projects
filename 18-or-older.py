def age_checker():
    eighteen_or_older = 0
    while True:
        age = input("Enter an age (q to quit): ").lower()
        if age == "q":
            break
        age = int(age)
        if age >= 18:
            print("Adult")
            eighteen_or_older += 1
        elif age < 18:
            print("Minor")
    return eighteen_or_older 
count = age_checker()
print(f"Age entered above or equal to 18: {count}")