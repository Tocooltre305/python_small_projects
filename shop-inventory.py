total_quantity = 0
out_of_stock_count = 0
low_stock_count = 0
num_products = int(input("How many different products are you checking? "))
for i in range(1, num_products + 1):
    qty = int(input(f"Enter quantity for product {i}: "))
    total_quantity += qty
    if qty == 0:
        out_of_stock_count += 1
    elif qty < 5:
        low_stock_count += 1
print("\n--- Inventory Report ---")
print(f"Total items in store: {total_quantity}")
print(f"Products out of stock: {out_of_stock_count}")
print(f"Products low in stock (< 5): {low_stock_count}")