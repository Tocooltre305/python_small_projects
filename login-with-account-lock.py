correct_user = "admin"
correct_pass = "1234"
user = input("Username: ")
pwd = input("Password: ")
status = input("Status (active/locked): ").lower()
if status == "locked":
    print("Account locked")
elif user == correct_user and pwd == correct_pass:
    print("Login successful")
else:
    print("Invalid login")