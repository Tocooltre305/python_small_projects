minimum_balance = float(input("Enter the minimum balance: "))
if minimum_balance > 50000:
    print("Premium account")
elif 5000 <= minimum_balance < 50000:
    print("Current account")
else:
    print("Savings account")
