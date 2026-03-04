def daily_water_intake():
    days_intake_more_or_equal_to_8_glasses = 0
    while True:
        num = input("Enter how many glasses of water you drank (q to quit): ")
        if num.lower() == "q":
            break
        num = int(num)
        if num >= 8:
            print("Water intake is high")
            days_intake_more_or_equal_to_8_glasses += 1
        else:
            print("Water intake is low")
    return days_intake_more_or_equal_to_8_glasses
count = daily_water_intake()
print(f"Days of high intake of water: {count}")