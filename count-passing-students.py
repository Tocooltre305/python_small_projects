def pass_checker():
    passed_students = 0
    while True:
        marks = input("Enter student marks (q to quit): ").lower()
        if marks == "q":
            break
        marks = int(marks)
        if marks > 100 or marks < 0:
            print("Invalid input")
        elif marks >= 50:
            print("Passed")
            passed_students += 1
        else:
            print("Failed")
    return passed_students
count = pass_checker()
print(f"Students passed: {count}")