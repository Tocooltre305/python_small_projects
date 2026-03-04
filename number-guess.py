import random
number = random.randint(1, 10)
guess = int(input("Enter a number between 1 and 10: "))

if guess == number:
    print("Correct! 🎉")
    print("The number was", number)
    print(f"You guessed {guess}")
else:
    print("Wrong guess. The number was", number)
    print(f"You guessed {guess}")