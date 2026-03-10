import tkinter as tk
from tkinter import messagebox
students_data = []
def calculate_grade(avg):
    if avg >= 90: return 'A'
    elif avg >= 80: return 'B'
    elif avg >= 70: return 'C'
    elif avg >= 60: return 'D'
    else: return 'F'
def add_student():
    name = ent_name.get()
    try:
        marks_str = ent_marks.get().split(',')
        marks = [float(m.strip()) for m in marks_str]
        total = sum(marks)
        avg = total / len(marks)
        letter_grade = calculate_grade(avg)
        student_entry = {
            "name": name,
            "marks": marks,
            "total": total,
            "average": avg,
            "grade": letter_grade
        }
        students_data.append(student_entry)
        messagebox.showinfo("Success", f"Data for {name} has been recorded.")
        ent_name.delete(0, tk.END)
        ent_marks.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Input Error", "Ensure marks are numbers separated by commas.")
def show_all():
    txt_display.delete(1.0, tk.END)
    if not students_data:
        txt_display.insert(tk.END, "No records found.")
        return
    for s in students_data:
        txt_display.insert(tk.END, f"Name: {s['name']} | Avg: {s['average']:.2f} | Grade: {s['grade']}\n")
def search_student():
    search_name = ent_search.get().lower()
    txt_display.delete(1.0, tk.END)
    found = False
    for s in students_data:
        if search_name in s['name'].lower():
            txt_display.insert(tk.END, f"MATCH: {s['name']} - Average: {s['average']:.2f} - Grade: {s['grade']}\n")
            found = True
    if not found:
        txt_display.insert(tk.END, f"No student matching '{search_name}' was found.")
root = tk.Tk()
root.title("Student Grade Manager")
root.geometry("450x550")
tk.Label(root, text="Student Name:").pack(pady=(10, 0))
ent_name = tk.Entry(root, width=40)
ent_name.pack(pady=5)
tk.Label(root, text="Enter Marks (e.g. 85, 92, 78):").pack(pady=(10, 0))
ent_marks = tk.Entry(root, width=40)
ent_marks.pack(pady=5)
tk.Button(root, text="Add to Records", command=add_student, width=20).pack(pady=10)
tk.Frame(root, height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=10, pady=10)
tk.Label(root, text="Search by Name:").pack()
ent_search = tk.Entry(root, width=40)
ent_search.pack(pady=5)
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)
tk.Button(btn_frame, text="Search", command=search_student, width=15).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Display All", command=show_all, width=15).pack(side=tk.LEFT, padx=5)
txt_display = tk.Text(root, height=12, width=50)
txt_display.pack(pady=15, padx=10)
root.mainloop()