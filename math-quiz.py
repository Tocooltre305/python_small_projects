import random
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
ans = num1 + num2
print(f"{num1} + {num2}")
human = int(input("Enter your answer: "))
if human == ans:
    print("Your Correct")
else:
    print("Your wrong")