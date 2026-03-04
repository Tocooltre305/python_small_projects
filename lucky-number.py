import random
user = int(input("Enter a number: "))
num = random.randint(1, 10)
if user == num:
    print("You're lucky")
else:
    print("Not this time")