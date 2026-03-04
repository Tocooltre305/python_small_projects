total_spending = 0
over_budget_days = 0
highest_expense = 0
budget_limit = float(input("Enter your daily budget limit: "))
num_days = int(input("How many days of expenses do you want to enter? "))
for i in range(1, num_days + 1):
    price = float(input(f"Enter expense for day {i}: "))
    total_spending += price
    if price > budget_limit:
        over_budget_days += 1
    if price > highest_expense:
        highest_expense = price
print("\n--- Monthly Budget Report ---")
print(f"Total Spending: ${total_spending:,.2f}")
print(f"Days Over Budget: {over_budget_days}")
print(f"Most Expensive Day: ${highest_expense:,.2f}")