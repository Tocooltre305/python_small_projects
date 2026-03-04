Celcuis_amount = float(input("Enter amount in Celcuis: "))
Fahrenheit_amount = float(input("Enter amount in Fahrenheit: "))
c_to_f = (Celcuis_amount * 9/5) + 32
f_to_c = (Fahrenheit_amount - 32) * 5/9
print(Celcuis_amount, "Celcuis is equal to", c_to_f, "Fahrenheit")
print(Fahrenheit_amount, "Fahrenheit is equal to", f_to_c, "Celcuis")
