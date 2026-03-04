def daily_sleep_tracker():
    hours_asleep_alot = 0
    while True:
        sleep = input("Enter how many hours did you sleep(q to quit): ")
        if sleep.lower() == "q":
            break
        sleep = int(sleep)
        if sleep >= 7:
            print("Good sleep")
            hours_asleep_alot += 1
        else:
            print("Bad sleep")
    return hours_asleep_alot
count = daily_sleep_tracker()
print(f"Days of high sleep: {count}")