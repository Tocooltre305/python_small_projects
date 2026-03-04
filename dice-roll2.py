import random

while True:

    user_choice = input("Enter a number (1-6) or 'quit': ").lower()

    if user_choice == "quit":
        print("Game over.")
        break  
    

    human = int(user_choice)
    

    dice = random.randint(1, 6)

    print(f"Computer rolled: {dice}")
    print(f"You chose: {human}")

    if human == dice:
        print("You win!")
        break
    else:
        print("You lose. Try again!")
        print("-" * 20)