temp = float(input("Enter temperature: "))
if temp >= 30:
    print("Hot weather")
elif 20 <= temp < 30:
    print("Warm weather")
elif 10 <= temp <= 19:
    print("Cool weather")
elif temp < 10:
     print("Cold weather")