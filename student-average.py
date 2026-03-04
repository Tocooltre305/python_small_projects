num_students = int(input("Number of students: "))
total_marks = 0

for i in range(num_students):
    mark = float(input(f"Marks for student {i+1}: "))
    total_marks += mark

average = total_marks / num_students
print("Class average:", average)