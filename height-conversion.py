import math
height = float(input("Enter your height in meters: "))
upper = math.ceil(height * 100)
lower = math.floor(height * 100)
print("Your height in cm:", height * 100)
print("Rounded up:", upper)
print("Rounded down:", lower)
