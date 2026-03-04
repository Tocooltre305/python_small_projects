import os
employees = {}
def main_menu():
    while True:
        print("\n--- PAYROLL MANAGEMENT ---")
        print("1. Add Employee\n2. View All\n3. Calculate & Record Salary\n4. View Payroll Summary\n5. Save\n6. Load\n7. Exit")
        choice = input("Select: ")
        if choice == '1': add_employee()
        elif choice == '2': view_employees()
        elif choice == '3': calculate_salary()
        elif choice == '4': payroll_summary()
        elif choice == '5': save_data()
        elif choice == '6': load_data()
        elif choice == '7': break
def add_employee():
    e_id = input("Employee ID: ")
    if e_id in employees: return
    name = input("Name: ")
    dept = input("Department: ")
    base = float(input("Basic Salary: "))
    allow = float(input("Allowances: "))
    tax_p = float(input("Tax %: "))
    deduct = float(input("Other Deductions: "))
    employees[e_id] = {"name": name, "dept": dept, "base": base, "allow": allow, "tax_p": tax_p, "deduct": deduct, "history": []}
def view_employees():
    for e_id, info in employees.items():
        print(f"ID: {e_id} | {info['name']} | Dept: {info['dept']} | Base: {info['base']}")
def calculate_salary():
    e_id = input("Employee ID: ")
    if e_id in employees:
        e = employees[e_id]
        gross = e["base"] + e["allow"]
        tax_amt = gross * (e["tax_p"] / 100)
        net = gross - tax_amt - e["deduct"]
        e["history"].append(net)
        print(f"Net Salary for {e['name']}: {net:.2f}")
def payroll_summary():
    total_cost = sum(sum(info["history"]) for info in employees.values())
    total_tax = sum((info["base"] + info["allow"]) * (info["tax_p"] / 100) for info in employees.values() if info["history"])
    print(f"Total Payroll Cost: {total_cost:.2f}")
    print(f"Total Tax Deducted: {total_tax:.2f}")
    if employees:
        highest = max(employees.values(), key=lambda x: x["base"])
        print(f"Highest Paid (Base): {highest['name']} ({highest['base']})")
def save_data():
    with open("payroll.txt", "w") as f:
        for e_id, info in employees.items():
            hist = "|".join(map(str, info["history"]))
            f.write(f"{e_id},{info['name']},{info['dept']},{info['base']},{info['allow']},{info['tax_p']},{info['deduct']},{hist}\n")
def load_data():
    global employees
    if os.path.exists("payroll.txt"):
        with open("payroll.txt", "r") as f:
            for line in f:
                p = line.strip().split(",")
                if len(p) == 8:
                    h = [float(x) for x in p[7].split("|") if x]
                    employees[p[0]] = {"name": p[1], "dept": p[2], "base": float(p[3]), "allow": float(p[4]), "tax_p": float(p[5]), "deduct": float(p[6]), "history": h}
if __name__ == "__main__":
    main_menu()