buying_price = float(input("Enter buying price: "))
selling_price = float(input("Enter selling price: "))
if selling_price > buying_price:
    profit = selling_price - buying_price
    print(f"Profit: {profit}")
    if profit > (0.5 * buying_price):
        print("High profit")
elif selling_price < buying_price:
    loss = buying_price - selling_price
    print(f"Loss: {loss}")
    if loss > (0.3 * buying_price):
        print("Heavy loss")
else:
    print("No profit no loss")