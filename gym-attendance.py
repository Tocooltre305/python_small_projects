total_visitors = 0
busiest_count = -1
busiest_hour_label = ""
zero_visitor_hours = 0
print("--- Gym Attendance Logger ---")
for hour in range(6, 23):
    time_label = f"{hour}:00"
    count = int(input(f"Visitors at {time_label}: "))
    total_visitors += count
    if count > busiest_count:
        busiest_count = count
        busiest_hour_label = time_label
    if count == 0:
        zero_visitor_hours += 1
print("\n--- Daily Summary ---")
print(f"Total Visitors: {total_visitors}")
print(f"Busiest Hour: {busiest_hour_label} ({busiest_count} people)")
print(f"Hours with Zero Visitors: {zero_visitor_hours}")