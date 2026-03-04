def check_attendance():
    attendance_list = []
    while True:
        status = input("Enter status (present/absent) or 'done' to finish: ").lower()
        if status == 'done':
            break
        if status == 'present' or status == 'absent':
            attendance_list.append(status)
        else:
            print("Invalid input. Please enter 'present' or 'absent'.")
    absent_count = 0
    for record in attendance_list:
        if record == "absent":
            absent_count += 1
    return absent_count
total = check_attendance()
print(f"Total students absent: {total}")