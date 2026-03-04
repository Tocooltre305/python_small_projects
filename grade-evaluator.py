grade = int(input("Enter your grade: "))

if grade >= 80:
    print("A")
elif grade >= 60:  # 60–79
    print("B")
elif grade >= 40:  # 40–59
    print("C")
elif grade >= 20:  # 20–39
    print("D")
else:              # 0–19
    print("F")
