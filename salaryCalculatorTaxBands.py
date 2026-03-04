salary = float(input("Enter your monthly salary: "))
if salary < 30000:
    tax_rate = 0.05
elif 30000 <= salary <= 100000:
    tax_rate = 0.15
else:
    tax_rate = 0.25
tax_amount =salary * tax_rate
net_salary = salary - tax_amount
print(f"Tax Amount: {tax_amount:.2f}")
print(f"Final Net Salary: {net_salary:.2f}")