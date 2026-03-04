distance = float(input("Enter distance: "))
liters = float(input("Enter liters: "))
fuel_consumption = distance / liters
final = round(fuel_consumption, 2)
print(f"The fuel consumption is: {final} km/l")