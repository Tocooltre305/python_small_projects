selling_price = float(input("Enter selling price: "))
cost_price = float(input("Enter cost price: "))
profit = selling_price - cost_price
if profit > 0:
    print("You made a profit of", profit)
else:
    print("You made a loss of", -profit)