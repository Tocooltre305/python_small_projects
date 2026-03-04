import random
choices = ["heads", "tails"]
coin_flip = random.choice(choices)
while True:
    user = input("Type heads or tails, or quit: ").lower()
    if user == "quit":
        print("Game over.")
        break
    if user not in choices:
        print("Invalid choice. Try again.")
        continue
    computer = random.choice(choices)
    print(f"You chose {user}, computer chose {computer}.")
    if user == computer:
        print("It's a draw!")
    elif user == coin_flip: 
        print("You win!")
    else:
        print("Computer wins!")