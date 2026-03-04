def check_guesses(guesses, correct_number):
    matches = 0
    for guess in guesses:
        if guess == correct_number:
            matches += 1
            print(f"Match found: {guess}")
        else:
            print(f"No match: {guess}")
    return matches
my_guesses = [5, 12, 7, 22, 7]
winning_num = 7
total_matches = check_guesses(my_guesses, winning_num)
print(f"Total correct guesses: {total_matches}")