present_count = 0
absent_count = 0
total_students = 0
print("--- School Attendance Register ---")
print("Enter 'done' when you are finished.\n")
while True:
    name = input("Student Name: ")
    if name.lower() == 'done':
        break
    status = input(f"Is {name} (P)resent or (A)bsent?: ").lower()
    if status == 'p':
        present_count += 1
        total_students += 1
    elif status == 'a':
        absent_count += 1
        total_students += 1
    else:
        print("Invalid input. Please use 'P' for Present or 'A' for Absent.")
if total_students > 0:
    percentage = (present_count / total_students) * 100
    
    print("\n--- Final Report ---")
    print(f"Total Students:   {total_students}")
    print(f"Total Present:    {present_count}")
    print(f"Total Absent:     {absent_count}")
    print(f"Attendance Rate: {percentage:.2f}%")
else:
    print("\nNo data was entered.")