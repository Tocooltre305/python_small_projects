def voting_counter():
    above_18 = 0
    while True:
        age = input("Enter your age (q to quit): ").lower()
        if age == "q":
            break
        age = int(age)
        if age >= 18:
            print("Eligible to vote")
            above_18 += 1
        elif age < 18:
            print("Not eligible to vote")
    return above_18 
count = voting_counter()
print(f"People eligible to vote: {count}")