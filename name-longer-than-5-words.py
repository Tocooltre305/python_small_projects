def name_length_checker():
    names_list = []
    while True:
        name = input("Enter a name (q to quit): ")
        if name == "q":
            break
        names_list.append(name)
    long_names_count = 0
    for name in names_list:
        if len(name) > 5:
            print(f"{name}: More than 5 letters")
            long_names_count += 1
        else:
            print(f"{name}: 5 letters or less")
    return long_names_count
count = name_length_checker()
print(f"Total names with more than 5 letters: {count}")