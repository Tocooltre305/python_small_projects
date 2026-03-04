def three_or_more_letter():
    more_than_3 = 0
    
    while True:
        word = input("Enter a word (or 'quit'): ").lower()
        
        if word == "quit":
            break
            
        if len(word) >= 3:
            more_than_3 += 1
            print("Has 3 or more letters")
        else:
            print("Not more than 3 letters")
            
    return more_than_3

result = three_or_more_letter()
print(f"Total words with 3+ letters: {result}")