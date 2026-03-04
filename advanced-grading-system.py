cat_score = float(input("Enter CAT score (out of 30): "))
exam_score = float(input("Enter Exam score (out of 70): "))
total = cat_score + exam_score
print(f"Total Score: {total}")
if total >= 80 and exam_score >= 40:
    print("Grade: A")
elif total >= 70 and exam_score >= 35:
    print("Grade: B")
elif 60 <= total <= 69:
    print("Grade: C")
elif 50 <= total <= 59:
    print("Grade: D")
else:
    print("Grade: Fail")