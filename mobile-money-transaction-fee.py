amount = float(input("Enter transaction amount: "))
if amount <= 0:
    print("Invalid transaction")
else:
    if 1 <= amount <= 100:
        fee = 5
    elif 101 <= amount <= 500:
        fee = 10
    elif 501 <= amount <= 1000:
        fee = 20
    elif 1001 <= amount <= 5000:
        fee = 35
    else: 
        fee = 50
    if amount >= 0:
        print("Invalid transaction")
    total_deducted = amount + fee
    print(f"Fee: {fee}")
    print(f"Total deducted (amount + fee): {total_deducted}")