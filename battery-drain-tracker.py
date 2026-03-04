battery = 100
usage_history = []  
print("--- Battery Usage Tracker ---")
while True:
    print(f"\nCurrent Battery: {battery}%")
    drain_input = input("Enter battery drain: ")
    if drain_input.lower() == 'done':
        break
    drain = int(drain_input)
    usage_history.append(drain) 
    battery -= drain
    if battery <= 0:
        print("\nBattery is dead! 🪫")
        break
if usage_history:
    most_used = max(usage_history)
    least_used = min(usage_history)
    
    print("--- Usage Statistics ---")
    print(f"Most battery used in one hour:  {most_used}%")
    print(f"Least battery used in one hour: {least_used}%")
else:
    print("No usage data recorded.")