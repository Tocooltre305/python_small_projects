def count_empty_spaces():
    total_spaces = 0
    while True:
        sentence = input("Enter a sentence (q to quit): ")
        if sentence.lower().strip() == "q":
            break
        space_count = 0
        for char in sentence:
            if char == " ":
                space_count += 1
            else:
                pass 
        print(f"There are {space_count} spaces in that sentence.")
        total_spaces += space_count
    return total_spaces
final_count = count_empty_spaces()
print(f"\nTotal spaces counted across all sentences: {final_count}")