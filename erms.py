import os
results = {}
def main_menu():
    while True:
        print("\n--- EXAMINATION RESULT SYSTEM ---")
        print("1. Add Student\n2. Add Subject Marks\n3. View Rankings\n4. Performance Analysis\n5. Save\n6. Load\n7. Exit")
        choice = input("Select: ")
        if choice == '1': add_student()
        elif choice == '2': add_marks()
        elif choice == '3': view_rankings()
        elif choice == '4': performance_analysis()
        elif choice == '5': save_data()
        elif choice == '6': load_data()
        elif choice == '7': break
def add_student():
    s_id = input("Student ID: ")
    if s_id in results: return
    name = input("Name: ")
    results[s_id] = {"name": name, "subjects": {}}
def add_marks():
    s_id = input("Student ID: ")
    if s_id in results:
        sub = input("Subject Name: ")
        marks = float(input(f"Enter marks for {sub}: "))
        results[s_id]["subjects"][sub] = marks
def view_rankings():
    ranking = []
    for s_id, info in results.items():
        if info["subjects"]:
            avg = sum(info["subjects"].values()) / len(info["subjects"])
            ranking.append({"name": info["name"], "avg": avg})
    ranking.sort(key=lambda x: x["avg"], reverse=True)
    print("\n--- Student Rankings ---")
    for i, r in enumerate(ranking, 1):
        print(f"{i}. {r['name']} - Average: {r['avg']:.2f}")
def performance_analysis():
    all_marks = []
    for info in results.values():
        all_marks.extend(info["subjects"].values())
    if all_marks:
        print(f"Class Average: {sum(all_marks)/len(all_marks):.2f}")
        print(f"Highest Mark: {max(all_marks)}")
        print(f"Lowest Mark: {min(all_marks)}")
def save_data():
    with open("results.txt", "w") as f:
        for s_id, info in results.items():
            sub_str = "|".join([f"{k}:{v}" for k, v in info["subjects"].items()])
            f.write(f"{s_id},{info['name']},{sub_str}\n")
def load_data():
    global results
    if os.path.exists("results.txt"):
        with open("results.txt", "r") as f:
            for line in f:
                p = line.strip().split(",")
                if len(p) == 3:
                    subs = {}
                    if p[2]:
                        for entry in p[2].split("|"):
                            s_name, s_mark = entry.split(":")
                            subs[s_name] = float(s_mark)
                    results[p[0]] = {"name": p[1], "subjects": subs}
if __name__ == "__main__":
    main_menu()