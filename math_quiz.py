import random 
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
correct_ans = num1 + num2
print(f"What is {num1} + {num2}?")
while True:
    user_guess = int(input("Enter your answer: "))
    if user_guess == correct_ans:
        print("Correct! Well done.")
        break  
    elif user_guess > correct_ans:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")