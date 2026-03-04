import os
from datetime import datetime, timedelta
books = {}
def main_menu():
    while True:
        print("\n--- LIBRARY MANAGEMENT ---")
        print("1. Add Book\n2. View Books\n3. Borrow Book\n4. Return Book\n5. Save\n6. Load\n7. Exit")
        choice = input("Select: ")
        if choice == '1': add_book()
        elif choice == '2': view_books()
        elif choice == '3': borrow_book()
        elif choice == '4': return_book()
        elif choice == '5': save_data()
        elif choice == '6': load_data()
        elif choice == '7': break
def add_book():
    b_id = input("Book ID: ")
    title = input("Title: ")
    author = input("Author: ")
    copies = int(input("Copies: "))
    books[b_id] = {"title": title, "author": author, "copies": copies, "borrowers": {}}
def view_books():
    for b_id, info in books.items():
        print(f"ID: {b_id} | {info['title']} by {info['author']} | Available: {info['copies']}")
def borrow_book():
    b_id = input("Book ID: ")
    if b_id in books and books[b_id]["copies"] > 0:
        name = input("Borrower Name: ")
        days = int(input("Borrow for how many days? "))
        due_date = (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d")
        books[b_id]["copies"] -= 1
        books[b_id]["borrowers"][name] = due_date
        print(f"Borrowed. Due date: {due_date}")
def return_book():
    b_id = input("Book ID: ")
    if b_id in books:
        name = input("Borrower Name: ")
        if name in books[b_id]["borrowers"]:
            due_str = books[b_id]["borrowers"][name]
            due_date = datetime.strptime(due_str, "%Y-%m-%d")
            days_late = (datetime.now() - due_date).days
            if days_late > 0:
                fine = days_late * 10
                print(f"Late by {days_late} days. Fine: {fine}")
            books[b_id]["copies"] += 1
            del books[b_id]["borrowers"][name]
            print("Returned successfully.")
def save_data():
    with open("library.txt", "w") as f:
        for b_id, info in books.items():
            borr_str = "|".join([f"{k}:{v}" for k, v in info["borrowers"].items()])
            f.write(f"{b_id},{info['title']},{info['author']},{info['copies']},{borr_str}\n")
def load_data():
    global books
    if os.path.exists("library.txt"):
        with open("library.txt", "r") as f:
            for line in f:
                p = line.strip().split(",")
                if len(p) == 5:
                    borr = {}
                    if p[4]:
                        for b in p[4].split("|"):
                            name, date = b.split(":")
                            borr[name] = date
                    books[p[0]] = {"title": p[1], "author": p[2], "copies": int(p[3]), "borrowers": borr}
if __name__ == "__main__":
    main_menu()