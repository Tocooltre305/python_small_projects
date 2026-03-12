import tkinter as tk
from tkinter import messagebox
class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern To-Do List")
        self.root.geometry("400x500")
        self.root.configure(bg="#2C3E50")
        self.tasks = []
        self.header = tk.Label(root, text="My Tasks", font=("Helvetica", 18, "bold"), bg="#2C3E50", fg="#ECF0F1")
        self.header.pack(pady=20)
        self.frame = tk.Frame(root, bg="#2C3E50")
        self.frame.pack(pady=10)
        self.listbox = tk.Listbox(self.frame, width=45, height=10, bg="#34495E", fg="#ECF0F1", borderwidth=0, highlightthickness=0, font=("Helvetica", 10))
        self.listbox.pack(side=tk.LEFT, padx=5)
        self.entry_name = tk.Entry(root, width=30, bg="#ECF0F1", font=("Helvetica", 10))
        self.entry_name.pack(pady=5)
        self.entry_name.insert(0, "Task Name")
        self.entry_date = tk.Entry(root, width=30, bg="#ECF0F1", font=("Helvetica", 10))
        self.entry_date.pack(pady=5)
        self.entry_date.insert(0, "Due Date (e.g. 12/03)")
        self.btn_add = tk.Button(root, text="ADD TASK", command=self.add_task, bg="#27AE60", fg="white", width=25, relief="flat", font=("Helvetica", 9, "bold"))
        self.btn_add.pack(pady=10)
        self.btn_complete = tk.Button(root, text="MARK COMPLETE", command=self.mark_complete, bg="#2980B9", fg="white", width=25, relief="flat", font=("Helvetica", 9, "bold"))
        self.btn_complete.pack(pady=5)
        self.btn_delete = tk.Button(root, text="DELETE TASK", command=self.delete_task, bg="#E74C3C", fg="white", width=25, relief="flat", font=("Helvetica", 9, "bold"))
        self.btn_delete.pack(pady=5)
    def add_task(self):
        name = self.entry_name.get()
        date = self.entry_date.get()
        if name and name != "Task Name":
            self.tasks.append({"name": name, "date": date, "status": "Pending"})
            self.update_listbox()
            self.entry_name.delete(0, tk.END)
            self.entry_date.delete(0, tk.END)
    def mark_complete(self):
        try:
            index = self.listbox.curselection()[0]
            self.tasks[index]["status"] = "✔ Done"
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Selection", "Please select a task first!")
    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            del self.tasks[index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Selection", "Please select a task to delete!")
    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, f" {task['status']} | {task['name']} (Due: {task['date']})")
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()