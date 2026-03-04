grade_average = float(input("Enter your grade average: "))
family_income = float(input("Enter your family income: "))
discipline_record = input("Enter your Discipline record (good/bad): ").lower()
if discipline_record == "bad":
    print("Not eligible")
elif grade_average >= 85 and family_income < 50000 and discipline_record == "good":
    print("Full scholarship")
elif grade_average >= 75 and family_income < 100000:
    print("Partial scholarship")
else:
    print("Not eligible")