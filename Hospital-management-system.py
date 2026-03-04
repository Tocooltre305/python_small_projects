patients = []
doctors = []
appointments = []
def main_menu():
    while True:
        print("\n--- Hospital Management System ---")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. Book Appointment")
        print("4. View Patients")
        print("5. View Appointments")
        print("6. Exit")
        choice = input("Select an option (1-6): ")

        if choice == '1':
            add_patient()
        elif choice == '2':
            add_doctor()
        elif choice == '3':
            book_appointment()
        elif choice == '4':
            view_patients()
        elif choice == '5':
            view_appointments()
        elif choice == '6':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
def add_patient():
    name = input("Enter patient name: ")
    age = input("Enter patient age: ")
    gender = input("Enter patient gender: ")
    illness = input("Enter illness: ")
    patient = {
        "name": name,
        "age": age,
        "gender": gender,
        "illness": illness
    }
    patients.append(patient)
    print(f"Patient {name} added successfully.")
def add_doctor():
    name = input("Enter doctor name: ")
    specialization = input("Enter specialization: ")
    doctor = {
        "name": name,
        "specialization": specialization
    }
    doctors.append(doctor)
    print(f"Doctor {name} ({specialization}) added successfully.")
def book_appointment():
    if not patients or not doctors:
        print("Error: You need at least one patient and one doctor to book an appointment.")
        return
    print("\nSelect Patient:")
    for i, p in enumerate(patients):
        print(f"{i}. {p['name']}")
    p_idx = int(input("Enter patient number: "))
    print("\nSelect Doctor:")
    for i, d in enumerate(doctors):
        print(f"{i}. {d['name']} ({d['specialization']})")
    d_idx = int(input("Enter doctor number: "))
    appointment = {
        "patient": patients[p_idx]['name'],
        "doctor": doctors[d_idx]['name'],
        "specialization": doctors[d_idx]['specialization']
    }
    appointments.append(appointment)
    print(f"Appointment booked: {patients[p_idx]['name']} with Dr. {doctors[d_idx]['name']}")
def view_patients():
    print("\n--- Patients ---")
    for p in patients:
        print(f"Name: {p['name']}, Age: {p['age']}, Gender: {p['gender']}, Illness: {p['illness']}")
def view_appointments():
    print("\n--- Appointments ---")
    for a in appointments:
      print(f"Patient: {a['patient']} ---> Doctor: {a['doctor']} ({a['specialization']})")
if __name__ == "__main__":
    main_menu()