marks = [
    23, 56, 76, 12, 89, 43, 21, 10, 0, 67, 
    34, 55, 92, 18, 0, 45, 71, 29, 8, 63, 
    50, 14, 99, 5, 33, 81, 12, 0, 47, 22, 
    90, 31, 6, 74, 58, 19, 85, 40, 2, 66
]
passed_students = 0
print("The highest mark is:", max(marks))
print("The lowest mark is:", min(marks))
print("The average mark is:", sum(marks) / len(marks))
for m in marks:
    if m > 60:
        passed_students += 1
print("The number of passed students is:", passed_students)