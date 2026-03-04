def count_vowels():
    word = input("Enter a word: ").lower()
    vowels = "aeiou"
    vowel_count = 0
    
    for char in word:
        if char in vowels:
            vowel_count += 1
            
    return vowel_count

result = count_vowels()
print(f"Number of vowels: {result}")