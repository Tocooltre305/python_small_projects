import random
choices = ["rock", "paper", "scissors"]
while True:
    user = input("Type rock, paper, scissors, or quit: ").lower()
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
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")