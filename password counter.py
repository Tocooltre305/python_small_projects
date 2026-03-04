def long_password_counter():
    long_password = 0
    while True:
        password = input("Enter a password (q to quit): ").lower()
        if password == "q":
            break
        
        if len(password) >= 4:
            print("Long password")
            long_password += 1
        else:
            print("Short password")
            
    return long_password

count = long_password_counter()
print(f"Long passwords entered: {count}")