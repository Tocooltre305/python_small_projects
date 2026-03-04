name = input("Enter your name: ")
balance = float(input("Enter your starting balance: "))
expenses = []  
while True:
    print("\nMenu:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Summary")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")
    if choice == "1":
        description = input("Expense description: ")
        category = input("Category: ")
        amount = float(input("Amount: "))
        expense = {
            "description": description,
            "category": category,
            "amount": amount
        }
        expenses.append(expense)
        balance -= amount
        print("Expense added.")
    elif choice == "2":
        if not expenses:
            print("No expenses recorded.")
        else:
            print("\nYour Expenses:")
            for i in expenses:
                print(f"- {i['description']} | {i['category']} | {i['amount']}")
    elif choice == "3":
        total_expenses = 0
        for i in expenses:
            total_expenses += i["amount"]
        print("\nSummary:")
        print("Total expenses:", total_expenses)
        print("Remaining balance:", balance)
    elif choice == "4":
        print(f"Goodbye, {name}!")
        break
    else:
        print("Invalid choice. Try again.")