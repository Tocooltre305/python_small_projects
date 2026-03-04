def yes_counter():
    yes = 0
    while True:
        ans = input("Enter yes/no (q to quit): ").lower()
        if ans == "q":
            break
        ans = str(ans)
        if ans == "yes":
            print("Ok")
            yes += 1
        elif ans == "no":
            print("Why")
        else:
            print("Invalid")    
    return yes
count = yes_counter()
print(f"Amount of times yes entered: {count}")