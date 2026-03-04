battery = int(input("Enter battery %: "))
if 80 <= battery <= 100:
    print("Battery is full")
elif 30 <= battery < 79:
    print("Battery Sufficient")
elif 10 <= battery < 29:
    print("Battery Low")
else:
    print("Charge Immediately")
    