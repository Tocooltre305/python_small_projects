account_balance = float(input("Enter account balance: "))
withdrawal_amount = float(input("Enter withdrawal amount: "))
if withdrawal_amount > account_balance:
    print("Insufficient funds")
else:
    new_balance = account_balance - withdrawal_amount
    print("New balance:", new_balance)