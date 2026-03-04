loan = float(input("Enter loan amount: "))
annual_interest = float(input("Enter annual interest rate (%): "))
years = int(input("Enter number of years: "))

rate = annual_interest / 100
total_interest = loan * rate * years
total_repayment = loan + total_interest
monthly_payment = total_repayment / (years * 12)

print("Total repayment:", total_repayment)
print("Average monthly payment:", monthly_payment)
