password  = input("Enter your password: ")
if len(password) >= 10 :
    print("Password is strong")
elif len(password) <= 9:
    print("Password is moderate")
elif len(password) <= 6:
    print("Password is weak")