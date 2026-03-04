def count_items_in_list(items_list):
    count = 0  
    for item in items_list:
        count += 1  
    return count
user_items = []
while True:
    entry = input("Enter an item (or 'q' to finish): ").lower()
    if entry == 'q':
        break
    user_items.append(entry)
total_count = count_items_in_list(user_items)
print(f"\nYour list: {user_items}")
print(f"There are {total_count} items in your list.")