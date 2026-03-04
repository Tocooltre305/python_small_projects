def count_empty_strings(text_list):
    empty_count = 0
    
    for text in text_list:

        if text == "":
            empty_count += 1
        else:
           
            pass
            
    return empty_count



result = count_empty_strings()

print(f"Total empty strings found: {result}")