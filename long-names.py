def long_name_counter():
    long_name = 0
    while True:
        name = input("Enter a name (q to quit): ").lower()
        if name == "q":
            break
        name = str(name)
        if len(name) >= 4:
            print("Long name")
            long_name += 1
        elif len(name) < 4:
            print("Short name")
    return long_name 
count = long_name_counter()
print(f"Long names entered: {count}")