side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))
s = (side_a + side_b + side_c) / 2
area = (s * (s - side_a) * (s - side_b) * (s - side_c)) ** 0.5
print("The area of the triangle is", area)