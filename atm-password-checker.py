pin = 6741
user_pin = int(input("Enter your pin: "))
for i in range(2):
    if user_pin == pin:
        print("Login successful")
        break
    else:
        print("Incorrect pin")
        user_pin = int(input("Enter your pin: "))