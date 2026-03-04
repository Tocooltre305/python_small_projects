def screen_time_tracker():
    high_screen_time = 0
    while True:
        screen_time = input("Enter how many hours of screen time you spent (q to quit): ")
        if screen_time.lower() == "q":
            break
        screen_time = int(screen_time)
        if screen_time >= 3:
            print("Screen time is high")
            high_screen_time += 1
        else:
            print("Screen time is low")
    return high_screen_time
count = screen_time_tracker()
print(f"Days of high screen time: {count}")