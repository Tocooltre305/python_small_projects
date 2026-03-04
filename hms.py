import os
data = {"patients": {}, "doctors": {}, "appointments": []}
def main_menu():
    while True:
        print("\n--- HOSPITAL MANAGEMENT ---")
        print("1. Add Patient\n2. Add Doctor\n3. Book Appointment\n4. View Schedule\n5. Cancel Appointment\n6. Save\n7. Load\n8. Exit")
        choice = input("Select: ")
        if choice == '1': add_patient()
        elif choice == '2': add_doctor()
        elif choice == '3': book_appointment()
        elif choice == '4': view_schedule()
        elif choice == '5': cancel_appointment()
        elif choice == '6': save_data()
        elif choice == '7': load_data()
        elif choice == '8': break
def add_patient():
    p_id = input("Patient ID: ")
    if p_id in data["patients"]: return
    name = input("Name: ")
    age = input("Age: ")
    illness = input("Illness: ")
    data["patients"][p_id] = {"name": name, "age": age, "illness": illness}
def add_doctor():
    d_id = input("Doctor ID: ")
    if d_id in data["doctors"]: return
    name = input("Name: ")
    spec = input("Specialty: ")
    data["doctors"][d_id] = {"name": name, "specialty": spec, "schedule": []}
def book_appointment():
    p_id = input("Patient ID: ")
    d_id = input("Doctor ID: ")
    if p_id in data["patients"] and d_id in data["doctors"]:
        date = input("Date (YYYY-MM-DD): ")
        time = input("Time (HH:MM): ")
        slot = f"{date} {time}"
        if slot not in data["doctors"][d_id]["schedule"]:
            data["doctors"][d_id]["schedule"].append(slot)
            data["appointments"].append({"p_id": p_id, "d_id": d_id, "slot": slot})
            print("Booked.")
        else: print("Doctor busy at that time.")
    else: print("Patient or Doctor not found.")
def view_schedule():
    d_id = input("Doctor ID: ")
    if d_id in data["doctors"]:
        for slot in sorted(data["doctors"][d_id]["schedule"]):
            print(f"Booked: {slot}")
def cancel_appointment():
    p_id = input("Patient ID: ")
    d_id = input("Doctor ID: ")
    slot = input("Slot (YYYY-MM-DD HH:MM): ")
    for appt in data["appointments"]:
        if appt["p_id"] == p_id and appt["d_id"] == d_id and appt["slot"] == slot:
            data["appointments"].remove(appt)
            data["doctors"][d_id]["schedule"].remove(slot)
            print("Cancelled.")
            return
def save_data():
    with open("hospital.txt", "w") as f:
        for p_id, info in data["patients"].items():
            f.write(f"P,{p_id},{info['name']},{info['age']},{info['illness']}\n")
        for d_id, info in data["doctors"].items():
            sched = "|".join(info["schedule"])
            f.write(f"D,{d_id},{info['name']},{info['specialty']},{sched}\n")
def load_data():
    if os.path.exists("hospital.txt"):
        with open("hospital.txt", "r") as f:
            for line in f:
                p = line.strip().split(",")
                if p[0] == 'P': data["patients"][p[1]] = {"name": p[2], "age": p[3], "illness": p[4]}
                elif p[0] == 'D':
                    s = p[4].split("|") if p[4] else []
                    data["doctors"][p[1]] = {"name": p[2], "specialty": p[3], "schedule": s}
if __name__ == "__main__":
    main_menu()