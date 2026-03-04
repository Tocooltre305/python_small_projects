age = int(input("Enter Age: "))
smoker = input("Are you a smoker? (yes/no): ").lower()
accidents = int(input("Number of accidents: "))
if age < 25 or (smoker == "yes" and accidents >= 2):
    print("Risk Category: High Risk")
elif (25 <= age <= 40) and accidents <= 2:
    print("Risk Category: Medium Risk")
elif age > 40 and smoker == "no" and accidents == 0:
    print("Risk Category: Low Risk")
else:
    print("Risk Category: Standard/Undetermined")