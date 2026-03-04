units = float(input("Enter the total units consumed: "))
total_bill = 0
if units <= 50:    
    total_bill = units * 0.50
elif units <= 150:
    total_bill = (50 * 0.50) + ((units - 50) * 0.75)
else:
    total_bill = (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.20)
    
print(f"Total Electricity Bill: ${total_bill:.2f}")