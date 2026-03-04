age = int(input("Enter your age: "))
monthly_income = float(input("Enter your monthly income: "))
if age >= 21 and monthly_income >= 40000:
    print("You are eligible for a loan")
else:
    print("You are not eligible for a loan")