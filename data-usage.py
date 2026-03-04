data = float(input("Enter data left in GB: "))
if data >= 5:
    print("High data remaining")
elif 1 < data < 5:
    print("Moderate data remaining")
else:
    print("Low data remaining")
