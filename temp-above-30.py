def temp_checker():
    above_30 = 0
    while True:
        temp = input("Enter a the degrees in celsius (q to quit): ").lower()
        if temp == "q":
            break
        temp = int(temp)
        if temp >= 30:
            print("Hot day")
            above_30 += 1
        elif temp < 30:
            print("Not hot day")
    return above_30 
count = temp_checker()
print(f"Days above 30 degrees celsius: {count}")