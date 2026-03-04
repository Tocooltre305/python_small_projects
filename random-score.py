import random
player1 = random.randint(1, 100)
player2 = random.randint(1, 100)
player3 = random.randint(1, 100)
average = round((player1 + player2 + player3) / 3, 1)
print(f"Player 1: {player1}")
print(f"Player 2: {player2}")
print(f"Player 3: {player3}")
print(f"The average score is: {average}")