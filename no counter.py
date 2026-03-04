def no_counter():
    no = 0
    while True:
        ans = input("Enter yes/no (q to quit): ").lower()
        if ans == "q":
            break
        ans = str(ans)
        if ans == "no":
            print("Why?")
            no += 1
        elif ans == "yes":
            print("Ok")
        else:
            print("Invalid")    
    return no
count = no_counter()
print(f"Amount of times no entered: {count}")