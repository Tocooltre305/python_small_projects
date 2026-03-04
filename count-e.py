def count_letter_e():
    total_e_count = 0
    while True:
        word = input("Enter a word (q to quit): ").lower().strip()
        if word == "q":
            break
        current_word_count = 0
        for letter in word:
            if letter == 'e':
                current_word_count += 1
            else:
                pass 
        print(f"The letter 'e' appeared {current_word_count} times in '{word}'.")
        total_e_count += current_word_count
    return total_e_count
final_total = count_letter_e()
print(f"\nTotal 'e's across all words: {final_total}")