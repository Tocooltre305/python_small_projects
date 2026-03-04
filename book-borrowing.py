total_books = 0
max_books = 0
top_student = ""
zero_books_count = 0

while True:
    name = input("Student Name (or 'done'): ")
    if name.lower() == 'done':
        break
        
    count = int(input(f"Books borrowed by {name}: "))
    
    total_books += count
    
    if count > max_books:
        max_books = count
        top_student = name
        
    if count == 0:
        zero_books_count += 1

print(f"Total Books: {total_books}")
print(f"Top Borrower: {top_student} ({max_books})")
print(f"Students with 0 books: {zero_books_count}")