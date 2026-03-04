salary = float(input("Enter your annual salary: "))
years_employed = float(input("Enter years at current job: "))
credit_score = int(input("Enter your credit score: "))
if salary < 50000:
    print("Rejected: Low income")
elif years_employed < 2:
    print("Rejected: Not enough employment history")
elif credit_score < 700:
    print("Rejected: Low credit score")
else:
    print("Loan Approved")