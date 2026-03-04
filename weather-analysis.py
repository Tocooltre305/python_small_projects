temps = []

for i in range(1, 8):
    t = float(input(f"Day {i} temperature: "))
    temps.append(t)

highest = temps[0]
lowest = temps[0]
total = 0

for t in temps:
    if t > highest:
        highest = t
    if t < lowest:
        lowest = t
    total += t

average = total / len(temps)

print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", average)