fares = []
reduced_fare_threshold = 5.00  

print("--- Bus Fare Collection System ---")
print("Enter '0' or 'done' to finish.\n")

while True:
    entry = input("Enter fare amount: ")
    
    if entry.lower() == 'done' or entry == '0':
        break
        
    try:
        fare = float(entry)
        fares.append(fare)
    except ValueError:
        print("Please enter a valid number.")


if fares:
    total_collected = sum(fares)
    highest_fare = max(fares)
  
    reduced_count = len([f for f in fares if f < reduced_fare_threshold])
    
    print("\n--- Collection Summary ---")
    print(f"Total Passengers:   {len(fares)}")
    print(f"Total Collected:    ${total_collected:.2f}")
    print(f"Highest Fare Paid:  ${highest_fare:.2f}")
    print(f"Reduced Fare Count: {reduced_count}")
else:
    print("No fares recorded today.")