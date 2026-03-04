import random

while True:
    winning_path = random.choice(["left", "right"])
    choice = input("left or right: ").lower()

    if choice == winning_path:
        print("You found the treasure!")
        break
    else:
        print("Game Over! Try again.")