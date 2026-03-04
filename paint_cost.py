area = float(input("Enter room area in square meters: "))
price_per_liter = float(input("Enter price per liter: "))

liters_required = area / 8
total_cost = liters_required * price_per_liter

print(f"Paint required: {liters_required} liters")
print(f"Total cost: {total_cost}")
