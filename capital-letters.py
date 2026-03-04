def count_capitals(word):
    count = 0
    for char in word:
        if char.isupper():
            count += 1
        else:
            pass
    return count

user_word = input("Enter a word or sentence: ")
result = count_capitals(user_word)
print(result)