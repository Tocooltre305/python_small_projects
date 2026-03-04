valid_usernames = ["admin", "user123", "python_pro", "guest"]

username = input("Enter your username: ")

while username not in valid_usernames:
    print("Invalid username. Please try again.")
    username = input("Enter your username: ")

print("Access granted")