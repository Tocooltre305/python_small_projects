price = float(input("Enter the price: "))
vat_rate = float(input("Enter VAT rate (%): "))

vat_amount = price * (vat_rate / 100)
final_price = price + vat_amount

print(f"VAT amount: {vat_amount}")
print(f"Final price after VAT: {final_price}")
