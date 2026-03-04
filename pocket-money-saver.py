def pocket_money_saver():
    goal = float(input("Enter your savings goal: "))
    total_savings = 0
    while True:
        entry = input("Enter daily savings amount (q to quit): ")
        if entry.lower() == 'q':
            break
        amount = float(entry)
        total_savings += amount
        if total_savings >= goal:
            print("Goal reached!")
        else:
            print(f"Current total: {total_savings}")
    print(f"Final Total Saved: {total_savings}")
    if total_savings >= goal:
        print("Congratulations! You hit your target.")
    else:
        print(f"You missed your goal by {goal - total_savings}.")
pocket_money_saver()