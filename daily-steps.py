steps_list = []
total_steps = 0
high_activity_days = 0
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print("--- Enter your steps for the week ---")
for day in days_of_week:
    daily_input = int(input(f"Enter steps for {day}: "))
    total_steps += daily_input
    if daily_input > 10000:
        high_activity_days += 1
average_steps = total_steps / 7
print("\n--- Weekly Report ---")
print(f"Total Steps: {total_steps:,}")
print(f"Average Steps: {average_steps:,.0f}")
print(f"Days over 10,000 steps: {high_activity_days}")