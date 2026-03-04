def count_letters(sentence):
    count = 0
    for char in sentence:
        if char != " ":
            count += 1
        else:
            continue
    return count

user_sentence = input("Enter a sentence: ")
total_letters = count_letters(user_sentence)
print(f"Letter count: {total_letters}")