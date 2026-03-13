import tkinter as tk
from tkinter import messagebox
class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.books = []
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)
        tk.Label(self.frame, text="Title:").grid(row=0, column=0)
        self.title_entry = tk.Entry(self.frame)
        self.title_entry.grid(row=0, column=1)
        tk.Label(self.frame, text="Author:").grid(row=1, column=0)
        self.author_entry = tk.Entry(self.frame)
        self.author_entry.grid(row=1, column=1)
        tk.Button(self.frame, text="Add Book", command=self.add_book).grid(row=2, column=0, columnspan=2, sticky="we")
        tk.Label(self.frame, text="Borrower Name:").grid(row=3, column=0)
        self.borrower_entry = tk.Entry(self.frame)
        self.borrower_entry.grid(row=3, column=1)
        tk.Button(self.frame, text="Issue Book", command=self.issue_book).grid(row=4, column=0, sticky="we")
        tk.Button(self.frame, text="Return Book", command=self.return_book).grid(row=4, column=1, sticky="we")
        self.listbox = tk.Listbox(self.frame, width=50)
        self.listbox.grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(self.frame, text="Exit", command=root.quit).grid(row=6, column=0, columnspan=2, sticky="we")
        self.update_list()
    def add_book(self):
        t, a = self.title_entry.get(), self.author_entry.get()
        if t and a:
            self.books.append({"title": t, "author": a, "status": "Available", "borrower": ""})
            self.update_list()
            self.title_entry.delete(0, tk.END)
            self.author_entry.delete(0, tk.END)
    def issue_book(self):
        sel = self.listbox.curselection()
        name = self.borrower_entry.get()
        if sel and name:
            idx = sel[0]
            if self.books[idx]["status"] == "Available":
                self.books[idx]["status"] = "Borrowed"
                self.books[idx]["borrower"] = name
                self.update_list()
                self.borrower_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Error", "Book already borrowed")
    def return_book(self):
        sel = self.listbox.curselection()
        if sel:
            idx = sel[0]
            self.books[idx]["status"] = "Available"
            self.books[idx]["borrower"] = ""
            self.update_list()
    def update_list(self):
        self.listbox.delete(0, tk.END)
        for b in self.books:
            info = f"{b['title']} by {b['author']} - [{b['status']}]"
            if b['borrower']: info += f" ( {b['borrower']} )"
            self.listbox.insert(tk.END, info)
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()