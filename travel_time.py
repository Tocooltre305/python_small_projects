distance = float(input("Enter distance: "))
speed = float(input("Enter speed: "))

time = distance / speed   # time in hours

hours = int(time)
minutes = (time - hours) * 60

print(f"It will take {hours} hours and {minutes:.0f} minutes to reach the destination.")
