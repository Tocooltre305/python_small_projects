units_consumed = float(input("Enter number of units consumed: "))
ppu = float(input("Enter price per unit: "))
bill = units_consumed * ppu
final_bill = bill + 150
print("Your electric bill is:", bill, "with an extra charge of 150 KES. Your final bill is:", final_bill,"KES . ")