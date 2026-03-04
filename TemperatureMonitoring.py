num_readings = int(input("Enter the number of temperature readings: "))
total_temp = 0
high_count = 0
low_count = 0
for i in range(num_readings):
    temp = float(input(f"Enter temperature reading {i+1}: "))
    total_temp += temp
    if temp > 38.0:
        high_count += 1
    elif temp < 10.0:
        low_count += 1
average_temp = total_temp / num_readings
print("\n---System Analysis---")
if high_count > 3:
    print("Heat alert")
elif low_count > 3:
    print("Cold alert")
else:
    print("Normal temperature")
print(f"Average temperature: {average_temp:.1f}")