def below_thirteen_counter():
    thirteen_or_below = 0
    while True:
        age = input("Enter an age (q to quit): ")
        if age == "q":
            break
        age = int(age)
        if age < 13:
            print("Youger than 13")
            thirteen_or_below += 1
        elif age  >= 13:
            print("Is or above than 13")
    return thirteen_or_below 
count = below_thirteen_counter()
print(f"Ages entered that are 13 or below : {count}")