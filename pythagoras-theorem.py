import math
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
hypotnuse = (side_a ** 2) + (side_b ** 2)
ans = math.sqrt(hypotnuse)
finalans = round(ans, 1)
print(f"The hypotnuse of the triangle is: {finalans} cm")