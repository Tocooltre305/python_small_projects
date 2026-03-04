annual_profit = float(input("Enter annual profit: "))
if annual_profit < 0:
    print("Business loss, no tax")
else:
    if annual_profit <= 100000:
        tax_rate = 0.10
    elif annual_profit <= 500000:
        tax_rate = 0.20
    else:
        tax_rate = 0.30
    tax_amount = annual_profit * tax_rate
    print(f"Tax Rate: {int(tax_rate * 100)}%")
    print(f"Tax Amount: {tax_amount}")
    print(f"Net Profit: {annual_profit - tax_amount}")