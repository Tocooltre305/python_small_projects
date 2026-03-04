temp = float(input("Enter temperature (°C): "))
rain = input("Is it raining? (yes/no): ").lower()
wind_speed = float(input("Enter wind speed (km/h): "))
if temp < 0 or (wind_speed > 50 and rain == "yes"):
    print("Severe Weather Alert")
elif temp < 10 and rain == "no":
    print("Cold Weather Advisory")
elif temp > 35 and wind_speed < 20:
    print("Heat Advisory")
else:
    print("Normal Weather")