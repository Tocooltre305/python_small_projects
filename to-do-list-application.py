def main():
    tasks = []
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3.Mark Task Complete")
        print("4. Delete Task")
        print("5. Quit")
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            name = input("Enter task name: ")
            due_date = input("Enter due date: ")
            task = {"name": name, "due_date": due_date, "status": "Incomplete"}
            tasks.append(task)
            print("Task added.")
        elif choice == "2":
            if not tasks:
                print("\n Your list is empty.")
            else:
                print("\nYOUR TASKS:")
                for idx, t in enumerate(tasks, 1):
                   print(f"{idx}. [{t['status']}] {t['name']} (Due: {t['due_date']})") 
        elif choice == "3":
            if not tasks:
                print("\nNothing to mark complete.")
                
            try:
                task_num = int(input("Enter task number to mark complete:"))
                tasks[task_num - 1]["status"] = "Complete"
                print("Status updated!")
            except (ValueError, IndexError):
                print("Invalid task number.")
        elif choice == "4":
            delete_input = input("Enter task number or name to delete:")
            if delete_input.isdigit():
                idx = int(delete_input) - 1
                if 0 <= idx < len(tasks):
                    removed = task.pop(idx)
                    print(f"Deleted ; {removed['name']}")
                else:
                    print("Invalid index.")
            else:
                original_len = len(tasks)
                tasks = [t for t in tasks if t['name'].lower() != delete_input.lower()]
                if len(tasks) < original_len:
                    print(f"Deleted task(s) named '{delete_input}'.")
                else:
                    print("Task name not found.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()