orders = []
total_revenue = 0
high_value_count = 0
threshold = 100

while True:
    current_count = len(orders) + 1
    order_input = input(f"Order #{current_count} Price (or 'done'): ")
    
    if order_input.lower() == 'done':
        break
        
    price = float(order_input)
    orders.append(price)
    total_revenue += price
    
    if price > threshold:
        high_value_count += 1

print(f"Total Orders: {len(orders)}")
print(f"Total Revenue: {total_revenue}")
print(f"Orders over {threshold}: {high_value_count}")