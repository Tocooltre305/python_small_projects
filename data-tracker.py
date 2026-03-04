data_plan = float(input("Enter your total data plan (GB): "))
daily_limit = float(input("Enter your daily warning limit (GB): "))
days_to_track = int(input("How many days to record? "))
total_used = 0
exceeded_limit_days = 0
for day in range(1, days_to_track + 1):
    usage = float(input(f"Day {day} usage (GB): "))
    total_used += usage
    if usage > daily_limit:
        exceeded_limit_days += 1
        print("Warning: Daily limit exceeded!")
    if total_used >= data_plan:
        print(f"!!! DATA EXHAUSTED on Day {day} !!!")
        break
print("\n--- Usage Report ---")
print(f"Total Data Used: {total_used:.2f} GB")
print(f"Days exceeding daily limit: {exceeded_limit_days}")
print(f"Remaining Data: {max(0, data_plan - total_used):.2f} GB")