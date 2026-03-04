count = int(input("How many numbers will you enter? "))

first_num = float(input("Enter number 1: "))
maximum = first_num
minimum = first_num

for i in range(2, count + 1):
    num = float(input(f"Enter number {i}: "))
    
    if num > maximum:
        maximum = num
    
    if num < minimum:
        minimum = num

print("Maximum:", maximum)
print("Minimum:", minimum)