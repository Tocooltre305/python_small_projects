import random
while True:
    treasure_door = random.choice(["door 1", "door 2"])
    choice = input("Pick Door 1 or Door 2: ").lower()
    if choice == "quit":
        break
    if choice == treasure_door:
        print("You win treasure!")
        break
    else:
        print("A monster got you! Try again.")