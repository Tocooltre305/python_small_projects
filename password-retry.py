password = "mango6741"
password2 = input("Enter password: ")

while password2 != password:
    print("Incorrect password")
    password2 = input("Enter password: ")

print("Login successful")