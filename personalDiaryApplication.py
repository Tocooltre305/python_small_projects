import datetime

def personal_diary():
    # 1. Security: Set password
    password = input("Set your diary password: ")
    entries = []  # List of dictionaries to store entries

    # Simple login check
    attempt = input("Enter password to log in: ")
    if attempt != password:
        print("Incorrect password. Access denied.")
        return

    while True:
        # 2. Show Menu
        print("\n--- PERSONAL DIARY MENU ---")
        print("1. Add Entry\n2. View Entries\n3. Search Entry\n4. Delete Entry\n5. Exit")
        
        choice = input("Select an option (1-5): ")

        if choice == "1":
            # 3. Add Entry: Include date, title, and content
            title = input("Enter Title: ")
            content = input("Write your thoughts: ")
            date = datetime.date.today().strftime("%Y-%m-%d")
            entries.append({"date": date, "title": title, "content": content})
            print("Entry saved!")

        elif choice == "2":
            # View all entries
            if not entries:
                print("Your diary is empty.")
            for i, entry in enumerate(entries):
                print(f"\n[{i+1}] {entry['date']} - {entry['title']}")
                print(f"Content: {entry['content']}")

        elif choice == "3":
            # 5. Search by title or date
            query = input("Search by title or date (YYYY-MM-DD): ").lower()
            results = [e for e in entries if query in e['title'].lower() or query in e['date']]
            if results:
                for r in results:
                    print(f"\nFound: {r['date']} | {r['title']}\n{r['content']}")
            else:
                print("No matches found.")

        elif choice == "4":
            # Delete an entry
            try:
                idx = int(input("Enter entry number to delete: ")) - 1
                if 0 <= idx < len(entries):
                    deleted = entries.pop(idx)
                    print(f"Deleted entry: {deleted['title']}")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            print("Closing diary. Goodbye!")
            break

personal_diary()