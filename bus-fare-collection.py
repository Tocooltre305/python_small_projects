def bus_fare_collection():
    standard_fare = 5.00
    total_money = 0
    discounted_passengers = 0
    regular_passengers = 0
    while True:
        entry = input("Enter fare paid (q to quit): ")
        if entry.lower() == 'q':
            break
        fare = float(entry)
        total_money += fare
        if fare < standard_fare:
            print(f"Discounted fare recorded: {fare}")
            discounted_passengers += 1
        else:
            print(f"Standard fare recorded: {fare}")
            regular_passengers += 1
    print("\n--- Collection Summary ---")
    print(f"Total Money Collected: {total_money:.2f}")
    print(f"Regular Fare Passengers: {regular_passengers}")
    print(f"Discounted Fare Passengers: {discounted_passengers}")
    total_passengers = regular_passengers + discounted_passengers
    if total_passengers > 0:
        average_fare = total_money / total_passengers
        print(f"Average Fare per Passenger: {average_fare:.2f}")
    else:
        print("No passengers were recorded.")
bus_fare_collection()