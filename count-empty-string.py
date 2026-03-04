def count_empty_strings(word_list):
    count = 0
    for word in word_list:
        if word == "":
            count += 1
        else:
            pass
    return count

# Example: Manual input (splitting by commas)
user_input = input("Enter words separated by commas (leave gaps for empty strings): ")
words = [w.strip() for w in user_input.split(",")]

result = count_empty_strings(words)
print(result)