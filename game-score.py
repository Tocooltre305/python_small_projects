target_score = int(input("Enter the target score to win: "))
total_score = 0
levels_played = 0

while total_score < target_score:
    points = int(input(f"Enter points earned in level {levels_played + 1}: "))
    
    total_score += points
    levels_played += 1
    
    if total_score >= target_score:
        print("Target reached!")
        break

print("\n--- Game Summary ---")
print(f"Final Score: {total_score}")
print(f"Total Levels Played: {levels_played}")