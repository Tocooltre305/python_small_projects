import random
choices = ["rock", "paper", "scissors"]
human = input("Enter your choice: ")
computer = random.choice(choices)
if human == computer:
    print("Tie")
    print(f"Computer: {computer}")
    print(f"Human: {human}")
elif human == "rock" and computer == "scissors":
    print("You win")
    print(f"Computer: {computer}")
    print(f"Human: {human}")
elif human == "paper" and computer == "rock":
    print("You win")
    print(f"Computer: {computer}")
    print(f"Human: {human}")
elif human == "scissors" and computer == "paper":
    print("You win")
    print(f"Computer: {computer}")
    print(f"Human: {human}")
else:
    print("You lose")
    print(f"Computer: {computer}")
    print(f"Human: {human}")