word = input("Enter a word: ")
print("Reversed word: ", end="")
for i in range(len(word) - 1, -1, -1):
    print(word[i], end="")
print()