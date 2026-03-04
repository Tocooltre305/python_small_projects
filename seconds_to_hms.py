seconds = int(input("Enter seconds: "))
hours = seconds // 3600
remaining_seconds = seconds % 3600
minutes = remaining_seconds // 60
final_seconds = remaining_seconds % 60
print(f"{seconds} seconds is equal to {hours} hour, {minutes} minutes, and {final_seconds} seconds.")
