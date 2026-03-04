total_units = 0
max_units = 0
peak_day = 0
excess_days = 0
limit = 50
day_counter = 0

while True:
    day_counter += 1
    entry = input(f"Day {day_counter} units (or 'done'): ")
    
    if entry.lower() == 'done':
        break
        
    units = float(entry)
    total_units += units
    
    if units > max_units:
        max_units = units
        peak_day = day_counter
        
    if units > limit:
        excess_days += 1

print(f"Total Consumption: {total_units} units")
print(f"Highest Usage: Day {peak_day} ({max_units} units)")
print(f"Days exceeding {limit} units: {excess_days}")