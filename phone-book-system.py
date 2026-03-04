def phone_book():
    contacts = []
    while True:
        print("\n--- PHONE BOOK SYSTEM ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            contact = {
                "name": input("Enter name: "),
                "phone": input("Enter phone number: "),
                "email": input("Enter email: "),
                "address": input("Enter address: ")
            }
            contacts.append(contact)
            print("Contact added sucessfully.")
        elif choice == '2':
            if not contacts:
                print("\n[Phone book is currently empty.]")
            else:
                print(f"\n{'Name':<20} | {'Phone':<15} | {'Email':<25}")
                print("-" * 65)
                for c in contacts:
                    print(f"{c['name']:<20} | {c['phone']:<15} | {c['email']:<25}")
        elif choice == '3':
            query = input("Search by name or phone number: ").lower()
            results = [c for c in contacts if query in c['name'].lower() or query in c['phone'].lower()]
            if results:
                for r in results:
                    print(f"\nFound: {r['name']} - {r['phone']} ({r['email']})")
            else:
                print("No matching contact found.")
        elif choice == '4':
            name_to_update = input("Enter the full name of contact to update: ").lower()
            found = False
            for c in contacts:
                if c['name'].lower() == name_to_update:
                    print("Enter new details (leave blank to keep current):")
                    c['phone'] = input(f"New Phone [{c['phone']}]: ") or c['phone']
                    c['email'] = input(f"New Email [{c['email']}]: ") or c['email']
                    c['address'] = input(f"New Address [{c['address']}]: ") or c['address']
                    print("Contact updated .")
                    found = True
                    break
            if not found:
                print("Contact not found.")
        elif choice == '5':
            name_to_delete = input("Enter the  name of contact to delete: ").lower()
            initial_count = len(contacts)
            contacts = [c for c in contacts if c['name'].lower() != name_to_delete]
            if len(contacts) < initial_count:
                print("Contact deleted.")
            else:
                print("Contact not found.")
        elif choice == '6':
            print("Exciting Phone Book. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
    phone_book()