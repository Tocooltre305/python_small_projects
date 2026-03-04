import os
projects = {}
def main_menu():
    while True:
        print("\n--- PROJECT TASK MANAGER ---")
        print("1. Create Project\n2. Add Task\n3. Update Status\n4. View Progress\n5. Save\n6. Load\n7. Exit")
        choice = input("Select: ")
        if choice == '1': create_project()
        elif choice == '2': add_task()
        elif choice == '3': update_status()
        elif choice == '4': view_progress()
        elif choice == '5': save_data()
        elif choice == '6': load_data()
        elif choice == '7': break
def create_project():
    name = input("Project Name: ")
    if name in projects: return
    projects[name] = []
def add_task():
    name = input("Project Name: ")
    if name in projects:
        t_name = input("Task: ")
        projects[name].append({"task": t_name, "status": "Pending"})
def update_status():
    name = input("Project Name: ")
    if name in projects:
        for i, t in enumerate(projects[name]): print(f"{i}. {t['task']} [{t['status']}]")
        idx = int(input("Task Index: "))
        stat = input("Status (Pending/Progress/Completed): ")
        projects[name][idx]["status"] = stat
def view_progress():
    for name, tasks in projects.items():
        if not tasks: 
            print(f"{name}: 0% (No tasks)")
            continue
        done = len([t for t in tasks if t["status"] == "Completed"])
        perc = (done / len(tasks)) * 100
        print(f"{name}: {perc:.1f}% Complete ({done}/{len(tasks)} tasks)")
def save_data():
    with open("tasks.txt", "w") as f:
        for name, tasks in projects.items():
            t_str = "|".join([f"{t['task']}:{t['status']}" for t in tasks])
            f.write(f"{name},{t_str}\n")
def load_data():
    global projects
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as f:
            for line in f:
                p = line.strip().split(",")
                if len(p) == 2:
                    t_list = []
                    for t in p[1].split("|"):
                        if ":" in t:
                            tn, ts = t.split(":")
                            t_list.append({"task": tn, "status": ts})
                    projects[p[0]] = t_list
if __name__ == "__main__":
    main_menu()