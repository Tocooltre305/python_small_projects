items = []

count = int(input("How many items do you want to enter? "))

for i in range(count):
    item = input(f"Enter item {i + 1}: ")
    items.append(item)

print(f"Total number of items entered: {len(items)}")
