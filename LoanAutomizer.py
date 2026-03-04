loan_amount = float(input("Enter the loan amount: "))
annual_interest_rate = float(input("Enter the annual interest rate (percentage): "))
months_to_repay = int(input("Enter the number of months to repay: "))
monthly_interest_rate = (annual_interest_rate / 100) / 12
current_balance = loan_amount
total_interest_paid = 0
month_count = 1
while current_balance > 0:
    monthly_interest = current_balance * monthly_interest_rate
    print(f"\n--- Month {month_count} ---")
    print(f"Current Balance: {current_balance:.2f}")
    print(f"Interest accrued this month: {monthly_interest:.2f}")
    payment = float(input("Enter your payment amount for this month: "))
    while payment <= monthly_interest and current_balance > 0:
        print("Payment too low (must cover at least the monthly interest).")
        payment = float(input("Please enter a higher payment amount: "))
    current_balance -= (payment - monthly_interest)
    total_interest_paid += monthly_interest
    month_count += 1
    if current_balance < 0:
        current_balance = 0
print("\n" + "="*30)
print("LOAN PAID OFF")
print(f"Total Interest Paid: {total_interest_paid:.2f}")
print("="*30)