start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

for i in range(start, end + 1):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)