def short_word_counter():
    short_word = 0
    while True:
        word = input("Enter a word (q to quit): ").lower()
        if word == "q":
            break
        word = str(word)
        if len(word) <= 3:
            print("Short word")
            short_word += 1
        elif len(word) > 3:
            print("Long word")
    return short_word 
count = short_word_counter()
print(f"Short words entered: {count}")