og_username = input("Enter username: ")
og_password = input("Enter password: ")
user_input_username = input("Enter username: ")
user_input_password = input("Enter password: ")

if og_username == user_input_username and og_password == user_input_password:
    print("Login successful")
else:
    print("Login failed")