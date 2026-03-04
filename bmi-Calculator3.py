weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))
BMI = weight / (height ** 2)
if BMI <= 18.5:
    print("BMI:", BMI)
    print("Underweight")
elif BMI <= 25:
    print("BMI:", BMI)
    print("Normal weight")
elif BMI <= 30:
    print("BMI:", BMI)
    print("Overweight")
else:
    print("BMI:", BMI)
    print("Obese")