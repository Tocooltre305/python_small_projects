def school_attendance():
    present_count = 0
    absent_count = 0
    while True:
        status = input("Enter attendance status (Present/Absent) or 'q' to quit: ").lower()
        if status == 'q':
            break
        if status == 'present':
            present_count += 1
            print("Status recorded: Present")
        elif status == 'absent':
            absent_count += 1
            print("Status recorded: Absent")
        else:
            print("Invalid input. Please enter 'Present' or 'Absent'.")
    total_days = present_count + absent_count
    print(f"\nTotal Days Tracked: {total_days}")
    print(f"Total Days Present: {present_count}")
    print(f"Total Days Absent: {absent_count}")
    if total_days > 0:
        if present_count > (total_days / 2):
            print("Good attendance record!")
        else:
            print("Attendance is low. Try to attend more days.")
    else:
        print("No data recorded.")
school_attendance()