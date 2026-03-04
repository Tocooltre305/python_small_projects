a = float(input("Side 1: "))
b = float(input("Side 2: "))
c = float(input("Side 3: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Not a valid triangle")