text = input("Enter a word or sentence: ").lower()
vowels = 0
consonants = 0
for char in text:
    if char.isalpha(): 
        if char in "aeiou":
            vowels += 1
        else:
            consonants += 1

print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")