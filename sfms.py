import os
students = {}
def main_menu():
    while True:
        print("\n--- SCHOOL FEE MANAGEMENT ---")
        print("1. Add Student\n2. Record Payment\n3. View Balance\n4. List Defaulters\n5. Reports\n6. Save\n7. Load\n8. Exit")
        choice = input("Select: ")
        if choice == '1': add_student()
        elif choice == '2': record_payment()
        elif choice == '3': view_balance()
        elif choice == '4': list_defaulters()
        elif choice == '5': view_reports()
        elif choice == '6': save_data()
        elif choice == '7': load_data()
        elif choice == '8': break
def add_student():
    s_id = input("Student ID: ")
    if s_id in students: return
    name = input("Name: ")
    s_class = input("Class: ")
    total_fee = float(input("Total Fee Amount: "))
    students[s_id] = {"name": name, "class": s_class, "total": total_fee, "paid": 0.0, "history": []}
def record_payment():
    s_id = input("Student ID: ")
    if s_id in students:
        amt = float(input("Payment Amount: "))
        students[s_id]["paid"] += amt
        students[s_id]["history"].append(f"Paid {amt}")
        print(f"Update successful. Balance: {students[s_id]['total'] - students[s_id]['paid']}")
def view_balance():
    s_id = input("Student ID: ")
    if s_id in students:
        bal = students[s_id]["total"] - students[s_id]["paid"]
        print(f"Student: {students[s_id]['name']} | Balance: {bal}")
def list_defaulters():
    print("\n--- Defaulters (Balance > 0) ---")
    for s_id, info in students.items():
        bal = info["total"] - info["paid"]
        if bal > 0: print(f"ID: {s_id} | Name: {info['name']} | Owed: {bal}")
def view_reports():
    total_collected = sum(info["paid"] for info in students.values())
    print(f"Total Money Collected: {total_collected}")
    if students:
        top_payer = max(students.values(), key=lambda x: x["paid"])
        print(f"Highest Payer: {top_payer['name']} ({top_payer['paid']})")
def save_data():
    with open("fees.txt", "w") as f:
        for s_id, info in students.items():
            h = "|".join(info["history"])
            f.write(f"{s_id},{info['name']},{info['class']},{info['total']},{info['paid']},{h}\n")
def load_data():
    global students
    if os.path.exists("fees.txt"):
        with open("fees.txt", "r") as f:
            for line in f:
                p = line.strip().split(",")
                if len(p) == 6:
                    h = p[5].split("|") if p[5] else []
                    students[p[0]] = {"name": p[1], "class": p[2], "total": float(p[3]), "paid": float(p[4]), "history": h}
if __name__ == "__main__":
    main_menu()