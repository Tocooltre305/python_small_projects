def short_name_counter():
    short_name = 0
    while True:
        name = input("Enter a name (q to quit): ").lower()
        if name == "q":
            break
        name = str(name)
        if len(name) <= 4:
            print("Short name")
            short_name += 1
        elif len(name) > 4:
            print("Long name")
    return short_name
count = short_name_counter()
print(f"Short names entered: {count}")