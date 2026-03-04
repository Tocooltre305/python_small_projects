import os
import datetime
students = {}
def main_menu():
    while True:
        print("\n--- STUDENT MANAGEMENT SYSTEM ---")
        print("1. Add Student\n2. View All\n3. Add Grade\n4. Reports\n5. Save\n6. Load\n7. Exit")
        choice = input("Select: ")
        if choice == '1': add_student()
        elif choice == '2': view_all()
        elif choice == '3': add_grade()
        elif choice == '4': generate_reports()
        elif choice == '5': save_data()
        elif choice == '6': load_data()
        elif choice == '7': break
def add_student():
    s_id = input("ID: ")
    if s_id in students: return
    name = input("Name: ")
    age = input("Age: ")
    course = input("Course: ")
    students[s_id] = {"name": name, "age": age, "course": course, "grades": []}
def view_all():
    for s_id, info in students.items():
        print(f"{s_id}: {info['name']} | {info['course']} | Grades: {info['grades']}")
def add_grade():
    s_id = input("ID: ")
    if s_id in students:
        grade = float(input("Grade: "))
        students[s_id]["grades"].append(grade)
def generate_reports():
    report = []
    for s_id, info in students.items():
        avg = sum(info["grades"]) / len(info["grades"]) if info["grades"] else 0
        report.append((s_id, info["name"], avg))
    report.sort(key=lambda x: x[2], reverse=True)
    for r in report:
        print(f"ID: {r[0]} | Name: {r[1]} | Avg: {r[2]:.2f}")
def save_data():
    with open("students.txt", "w") as f:
        for s_id, info in students.items():
            g_str = "|".join(map(str, info["grades"]))
            f.write(f"{s_id},{info['name']},{info['age']},{info['course']},{g_str}\n")
def load_data():
    global students
    if os.path.exists("students.txt"):
        with open("students.txt", "r") as f:
            for line in f:
                p = line.strip().split(",")
                if len(p) == 5:
                    g_list = [float(g) for g in p[4].split("|") if g]
                    students[p[0]] = {"name": p[1], "age": p[2], "course": p[3], "grades": g_list}
if __name__ == "__main__":
    main_menu()