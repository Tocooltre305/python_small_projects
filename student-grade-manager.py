students = []
num_students = int(input("Enter the number of students: "))
for _ in range(num_students):
    name = input("\nEnter student name:")
    num_subjects = int(input("How many subjects?: "))
    marks = []
    for i in range(num_subjects):
        mark = float(input(f"Enter marks for subject {i + 1}: "))
        marks.append(mark)
total = sum(marks)
average = total / num_subjects
if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"
student = {
    "name": name,
    "marks": marks,
    "total": total,
    "average": average,
    "grade": grade
}
students.append(student)
print("\nAll Students Grades:")
for s in students:
    print(f"{s['name']} | Total: {s['total']} | Average: {s['average']:.2f} | Grade: {s['grade']}")
search = input("\nEnter a student name to search: ")
found = False
for s in students:
    if s["name"].lower() == search.lower():
        print("\nStudent Found:")
        print(f"Name: {s['name']}")
        print(f"Marks: {s['marks']}")
        print(f"Total: {s['total']}")
        print(f"Average: {s['average']:.2f}")
        print(f"Grade: {s['grade']:}")
        found = True
        break
if not found:
    print("Student not found.")