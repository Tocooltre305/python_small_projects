total_minutes = 0
max_minutes = 0
top_subject = ""
under_goal_count = 0
planned_time = 45 
while True:
    subject = input("Subject: ")
    if subject.lower() == 'done':
        break
    minutes = int(input("Minutes: "))
    total_minutes += minutes
    if minutes > max_minutes:
        max_minutes = minutes
        top_subject = subject
    if minutes < planned_time:
        under_goal_count += 1
print(f"Total: {total_minutes}")
print(f"Most Studied: {top_subject}")
print(f"Sessions < {planned_time}m: {under_goal_count}")