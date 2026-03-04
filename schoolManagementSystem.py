def school_management_system():
    students = []
    teachers = []
    while True:
        print("\n--- SCHOOL MANAGEMENT SYSTEM ---")
        print("1. Add Student\n2. Add Teacher\n3. Assign Class\n4. View All\n5. Exit")
        choice = input("Select an option (1-5): ")
        if choice == "1":
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            grade = input("Enter student grade: ")
            students.append({
                "name": name, 
                "age": age, 
                "grade": grade, 
                "teacher": "Unassigned"
            })
            print(f"Student {name} added.")
        elif choice == "2":
            name = input("Enter teacher name: ")
            subject = input("Enter teacher subject: ")
            teachers.append({"name": name, "subject": subject})
            print(f"Teacher {name} added.")
        elif choice == "3":
            if not students or not teachers:
                print("Error: You need both students and teachers to make an assignment.")
                continue
            print("\nAvailable Students:")
            for i, s in enumerate(students): print(f"{i}. {s['name']}")
            s_idx = int(input("Select student index: "))
            print("\nAvailable Teachers:")
            for i, t in enumerate(teachers): print(f"{i}. {t['name']} ({t['subject']})")
            t_idx = int(input("Select teacher index: "))


            students[s_idx]["teacher"] = teachers[t_idx]["name"]
            print(f"Assigned {teachers[t_idx]['name']} to {students[s_idx]['name']}.")

        elif choice == "4":
            print("\n--- STUDENT ROSTER ---")
            if not students:
                print("No records found.")
            for s in students:
                print(f"Student: {s['name']} | Grade: {s['grade']} | Teacher: {s['teacher']}")

        elif choice == "5":
            print("Exiting system.")
            break