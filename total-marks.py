def total_marks_calculator():
    marks_list = []
    
    while True:
        mark = input("Enter a mark (q to quit): ")
        if mark == "q":
            break
        marks_list.append(int(mark))

    total = 0
    for mark in marks_list:
        total += mark
        
    if total > 200:
        print(f"Total is {total}: Above 200")
    else:
        print(f"Total is {total}: 200 or below")
            
    return total

final_score = total_marks_calculator()