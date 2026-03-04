def workout_tracker():
    long_workouts = 0
    while True:
        time = input("Enter time spent working out in minutes(q to quit): ")
        if time.lower() == "q":
            break
        time = int(time)
        if time >= 30:
            print("Long workout")
            long_workouts += 1
        else:
            print("Short workout")
    return long_workouts
count = workout_tracker()
print(f"Days of long workouts: {count}")