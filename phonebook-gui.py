import tkinter as tk
from tkinter import messagebox
class PhoneBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Phone Book System")
        self.contacts = []
        tk.Label(root, text="Name:").grid(row=0, column=0)
        self.name_ent = tk.Entry(root)
        self.name_ent.grid(row=0, column=1)
        tk.Label(root, text="Phone:").grid(row=1, column=0)
        self.phone_ent = tk.Entry(root)
        self.phone_ent.grid(row=1, column=1)
        tk.Label(root, text="Email:").grid(row=2, column=0)
        self.email_ent = tk.Entry(root)
        self.email_ent.grid(row=2, column=1)
        tk.Label(root, text="Address:").grid(row=3, column=0)
        self.addr_ent = tk.Entry(root)
        self.addr_ent.grid(row=3, column=1)
        tk.Button(root, text="Add Contact", command=self.add_contact).grid(row=4, column=0, columnspan=2, sticky="ew")
        tk.Button(root, text="View All", command=self.view_contacts).grid(row=5, column=0, columnspan=2, sticky="ew")
        tk.Label(root, text="Search/Update/Delete by Name:").grid(row=6, column=0, columnspan=2)
        self.search_ent = tk.Entry(root)
        self.search_ent.grid(row=7, column=0, columnspan=2, sticky="ew")
        tk.Button(root, text="Search", command=self.search_contact).grid(row=8, column=0, sticky="ew")
        tk.Button(root, text="Update", command=self.update_contact).grid(row=8, column=1, sticky="ew")
        tk.Button(root, text="Delete", command=self.delete_contact).grid(row=9, column=0, columnspan=2, sticky="ew")
        self.display = tk.Text(root, height=10, width=40)
        self.display.grid(row=10, column=0, columnspan=2)
    def add_contact(self):
        name = self.name_ent.get()
        phone = self.phone_ent.get()
        if name and phone:
            self.contacts.append({"name": name, "phone": phone, "email": self.email_ent.get(), "address": self.addr_ent.get()})
            messagebox.showinfo("Success", "Contact Added")
            self.clear_entries()
        else:
            messagebox.showwarning("Error", "Name and Phone required")
    def view_contacts(self):
        self.display.delete("1.0", tk.END)
        if not self.contacts:
            self.display.insert(tk.END, "Phone book is empty.")
            return
        for c in self.contacts:
            self.display.insert(tk.END, f"Name: {c['name']}\nPhone: {c['phone']}\nEmail: {c['email']}\nAddr: {c['address']}\n{'-'*20}\n")
    def search_contact(self):
        query = self.search_ent.get().lower()
        self.display.delete("1.0", tk.END)
        found = [c for c in self.contacts if query in c['name'].lower() or query in c['phone']]
        if found:
            for c in found:
                self.display.insert(tk.END, f"FOUND:\n{c['name']} - {c['phone']}\n")
        else:
            self.display.insert(tk.END, "No contact found.")
    def update_contact(self):
        name = self.search_ent.get()
        for c in self.contacts:
            if c['name'].lower() == name.lower():
                c.update({"phone": self.phone_ent.get(), "email": self.email_ent.get(), "address": self.addr_ent.get()})
                messagebox.showinfo("Success", "Contact Updated")
                return
        messagebox.showwarning("Error", "Name not found")
    def delete_contact(self):
        name = self.search_ent.get()
        for i, c in enumerate(self.contacts):
            if c['name'].lower() == name.lower():
                self.contacts.pop(i)
                messagebox.showinfo("Success", "Contact Deleted")
                self.view_contacts()
                return
        messagebox.showwarning("Error", "Name not found")
    def clear_entries(self):
        self.name_ent.delete(0, tk.END)
        self.phone_ent.delete(0, tk.END)
        self.email_ent.delete(0, tk.END)
        self.addr_ent.delete(0, tk.END)
if __name__ == "__main__":
    root = tk.Tk()
    app = PhoneBookApp(root)
    root.mainloop()