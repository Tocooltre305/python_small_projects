secret_password = "open123"
while True:
    attempt = input("Enter the password: ")
    if attempt == secret_password:
        print("Door unlocked!")
        break
    else:
        print("Access denied! Try again.")