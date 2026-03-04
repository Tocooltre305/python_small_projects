def grocery_shopping_prices():
    total_cost = 0
    discount_threshold = 100
    discount_rate = 0.10
    
    while True:
        entry = input("Enter item price (q to quit): ")
        
        if entry.lower() == 'q':
            break
            
        price = float(entry)
        total_cost += price
        
        print(f"Current total: {total_cost:.2f}")

    print(f"\nSubtotal: {total_cost:.2f}")

    if total_cost >= discount_threshold:
        savings = total_cost * discount_rate
        final_total = total_cost - savings
        print(f"You qualified for a 10% discount!")
        print(f"Discount amount: {savings:.2f}")
        print(f"Final Total: {final_total:.2f}")
    else:
        print(f"No discount applied. Final Total: {total_cost:.2f}")
        print(f"Spend {discount_threshold - total_cost:.2f} more to get 10% off!")

grocery_shopping_prices()