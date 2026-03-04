vehicle_speed = int(input("Enter the vehicle speed: "))
if vehicle_speed > 100:
    print("Dangerous speed")
elif 60 <= vehicle_speed < 100:
    print("Overspeeding")
else:
    print("Safe speed")
