password = "open123"

for i in range(3):
    user_input_password = input("Enter password: ")
    
    if user_input_password == password:
        print("Password is correct")
        break
    else:
        print("Password is incorrect")
        
    if i == 2:
        print("Too many attempts")