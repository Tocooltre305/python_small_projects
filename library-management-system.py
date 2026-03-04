def library_system():
    books = []
    while True:
        print("\n--- LIBRARY MANAGEMENT  ---")
        print("1. Add Book\n2. View Books\n3. Issue Book\n4. Return Book\n5. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            title = input("Title: ")
            author = input("Author: ")
            books.append({"title": title, "author": author, "status": "Available", "borrower": None})
        elif choice == '2':
            for b in books:
                print(f"[{b['status']}] {b['title']} by {b['author']}")
        elif choice == '3':
            title = input("Title to issue: ")
            for b in books:
                if b['title'] == title and b['status'] == "Available":
                    b['borrower'] = input("Borrower Name: ")
                    b['status'] = "Borrowed"
                    print("Book issued.")
        elif choice == '4':
            title = input("Title to return: ")
            for b in books:
                if b['title'] == title:
                    b['status'] = "Available"
                    b['borrower'] = None
                    print("Book returned.")
        elif choice == '5':
            break
if __name__ == "__main__":
    library_system()