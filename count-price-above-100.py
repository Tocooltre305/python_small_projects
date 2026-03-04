def count_cheap_prices():
    below_100_count = 0
    while True:
        entry = input("Enter a price (q to quit): ").lower().strip()
        if entry == 'q':
            break
        price = float(entry)
        if price < 100:
            print(f"  -> {price} is below 100. Adding to count.")
            below_100_count += 1
        else:
            print(f"  -> {price} is 100 or more. Skipping.")
    return below_100_count
count = count_cheap_prices()
print(f"\nTotal prices below 100: {count}")