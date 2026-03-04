total = 0
print("Enter item prices (enter 0 to stop):")
for i in range(1000): 
    price = float(input(f"Item {i+1} price: "))
    if price == 0:
        break 
    total += price
print(f"---")
print(f"Total Amount: ${total:.2f}")