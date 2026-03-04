import random
coin = ["heads", "tails"]
human = input("Enter your choice (heads/tails): ").lower()
computer = random.choice(coin)
if human not in coin:
    print("Invalid choice")
elif human == computer:
    print("You win")
    print(f"Computer: {computer}")
else:
    print("You lose")
    print(f"Computer: {computer}")
