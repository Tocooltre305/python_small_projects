def count_lowercase_letters():
    word = input("Enter a word: ")
    i = 0
    lower_count = 0
    while i < len(word):
        char = word[i]
        if char.islower():
            print(f"'{char}' is lowercase.")
            lower_count += 1
        else:
            print(f"'{char}' is NOT lowercase.")
        i += 1
    return lower_count
result = count_lowercase_letters()
print("-" * 20)
print(f"Total lowercase letters found: {result}")