def calculate_shopping_total():
    prices = []
    
    while True:
        entry = input("Enter item price (or 'done'): ").lower()
        if entry == 'done':
            break
        prices.append(float(entry))
    
    total = 0
    for price in prices:
        total += price
        
    if total > 100:
        total = total * 0.9
        print("A 10% discount has been applied.")
    else:
        print("No discount applied.")
        
    return total

final_bill = calculate_shopping_total()
print(f"Your final total is: {final_bill}")