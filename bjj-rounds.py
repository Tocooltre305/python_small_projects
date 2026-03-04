total_rounds = 0
most_rounds = 0
low_volume_sessions = 0
num_sessions = int(input("How many sessions do you want to log? "))
for i in range(1, num_sessions + 1):
    rounds = int(input(f"Enter rounds for session {i}: "))
    total_rounds += rounds
    if rounds > most_rounds:
        most_rounds = rounds
    if rounds < 5:
        low_volume_sessions += 1
print("\n--- BJJ Training Summary ---")
print(f"Total Rounds Rolled: {total_rounds}")
print(f"Most Rounds in a Session: {most_rounds}")
print(f"Sessions with < 5 rounds: {low_volume_sessions}")