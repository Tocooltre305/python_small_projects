units = float(input("Enter units consumed: "))
bill = 0
if units <= 100:
    bill = units * 10
elif units <= 200:
    bill = (100 * 10) + ((units - 100) * 15)
else:
    bill = (100 * 10) + (100 * 15) + ((units - 200) * 20)
if bill > 10000:
    bill = bill + (bill * 0.16)
print(f"Final bill: {bill}")