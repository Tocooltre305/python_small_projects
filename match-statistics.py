total = [1, 3, 4, 1, 6, 8, 4, 3, 5, 1]
total_goals = sum(total)
most_goals = max(total)
no_goals_count = 0
match_number = 0
best_match = 0
for goals in total:
    match_number += 1
    if goals == 0:
        no_goals_count += 1
    if goals == most_goals:
        best_match = match_number
print(f"Total Goals: {total_goals}")
print(f"Most Goals: {most_goals} (Match #{best_match})")
print(f"Matches with 0 goals: {no_goals_count}")