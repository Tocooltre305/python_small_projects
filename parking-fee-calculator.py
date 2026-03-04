hours = float(input("Enter hours parked: "))
is_weekend = input("Is it weekend? (yes/no): ").lower()
if hours <= 0:
    print("invalid")
else:
    if hours <= 2:
        fee = hours * 100
    else:
        fee = (2 * 100) + ((hours - 2) * 50)
    if is_weekend == "yes":
        fee = fee + (fee * 0.20)
    print(f"Total Parking Fee: {fee}")