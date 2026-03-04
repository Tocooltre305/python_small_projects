import random


secret_number = random.randint(1, 10)

attempts = 0

print("I'm thinking of a number between 1 and 10. Can you guess it?")
while True:
    
    try:
        guess = int(input("Enter your guess: "))
        
        
        attempts += 1

    
        if guess == secret_number:
            print(f"Correct! You found it in {attempts} attempts.")
            break   
        elif guess < secret_number:
            print("Too low! Try a bigger number.")
        else:
            print("Too high! Try a smaller number.")
            
    except ValueError:
        print("Please enter a valid whole number!")