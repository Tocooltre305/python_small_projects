import random
dice = random.randint(1, 6)
human = int(input("Enter a number between 1 and 6: "))

if human == dice:
    print("You win")
    print(f"Computer: {dice}")
    print(f"Human: {human}")
else:
    print("You lose")
    print(f"Computer: {dice}")
    print(f"Human: {human}")