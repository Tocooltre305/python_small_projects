weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))
BMI = weight / height ** 2
BMIR = round(BMI, 1)
print(f"Your BMI is: {BMIR}")