def message_notifications():
    quiet_hours = 0
    active_hours = 0
    total_messages = 0
    hour_counter = 1
    while True:
        entry = input(f"Enter messages for hour {hour_counter} (q to quit): ")
        if entry.lower() == 'q':
            break
        count = int(entry)
        total_messages += count
        if count == 0:
            print(f"Hour {hour_counter} was a quiet hour.")
            quiet_hours += 1
        else:
            print(f"Hour {hour_counter} had {count} messages.")
            active_hours += 1
        hour_counter += 1
    print("\n--- Notification Summary ---")
    print(f"Total Hours Tracked: {hour_counter - 1}")
    print(f"Total Messages Received: {total_messages}")
    print(f"Quiet Hours (No Messages): {quiet_hours}")
    print(f"Active Hours: {active_hours}")
    if hour_counter > 1:
        if quiet_hours > active_hours:
            print("Status: It was a very quiet day.")
        else:
            print("Status: You were quite busy today!")
    else:
        print("No data recorded.")
message_notifications()