def count_letters():
        while True:
            word = input("Enter a word (q to quit): ")
            if word == "q":
                break
            lenght = len(word)
            print(f"The word {word} has {lenght} letters")
count_letters()