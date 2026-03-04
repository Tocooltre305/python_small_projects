
balance = float(input("Enter your current airtime balance (Ksh): "))
duration = float(input("Enter the call duration in minutes: "))
rate_per_minute = 3
call_cost = duration * rate_per_minute
remaining_balance = balance - call_cost
print(f"\nCall Cost: Ksh {call_cost:.2f}")
print(f"Remaining Airtime Balance: Ksh {remaining_balance:.2f}")