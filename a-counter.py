def count_letter_a():
    total_a_count = 0
    while True:
        word = input("Enter a word (q to quit): ").lower().strip()
        if word == "q":
            break
        current_word_count = 0
        for letter in word:
            if letter == 'a':
                current_word_count += 1
            else:
                pass 
        print(f"The letter 'a' appeared {current_word_count} times in '{word}'.")
        total_a_count += current_word_count
    return total_a_count
final_total = count_letter_a()
print(f"\nTotal 'a's across all words: {final_total}")