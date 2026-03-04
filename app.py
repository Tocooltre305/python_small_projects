# print("hello world")
# name = "John"
# age= 40
# height = 174.65
# is_adult = True
# numbers = [1,2,3,4,5]
# student = {"name": "John", "age": 23, "height": 178.87, "classes": ["Math", "Physics", "Chemistry"]} 

# # print(name)
# print(age)
# print(height)
# print(is_adult)
# print(numbers)
# print(student)

# print(type(name))

# #

# print(5 % 2)

# a = int(input("Enter number:"))
# b = int(input("Enter another number:"))
# c = a % b

# if c == 0:
#     print("a is divisible by b")
# else:
#     print("a is not divisible by b")

# score = int(input("Enter score:"))
# def get_grade(score):
#     if score >= 90:
#         return "A"
#     elif score >= 75:
#         return "B"
#     elif score >= 60:
#         return "C"
#     elif score >= 50:
#         return "D"
#     else:
#         return "F"

# print(get_grade(score))   

a = int(input("Enter number:"))
b = int(input("Enter another number:"))
print("Choose an operator (+, -, *, /)")
operator = input("Enter operator:")
if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    print(a / b)
else:
    print("Invalid operator")