age = int(input("Enter your age: "))

if age >= 60:
    print("You are eligible to retire")
    print("You are eligible to vote and drive")
    print("You are eligible to drink alcohol")

elif age >= 21:
    print("You are eligible to drink alcohol")
    print("You are eligible to vote and drive")

elif age >= 18:
    print("You are eligible to vote and drive")

else:
    print("You are not eligible to vote, drive, or drink alcohol")
