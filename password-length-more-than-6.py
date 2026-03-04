def password_length_counter():
    long_password = 0
    while True:
        password = input("Enter a password (q to quit): ").lower()
        if password == "q":
            break
        password = str(password)
        if len(password) >= 6:
            print("Strong Password")
            long_password += 1
        elif len(password)  < 6:
            print("Weak Password")
    return long_password 
count = password_length_counter()
print(f"Password entered more or has 6 charcters: {count}")