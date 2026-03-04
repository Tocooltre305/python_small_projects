import os
from datetime import datetime
rooms = {}
def main_menu():
    while True:
        print("\n--- HOTEL RESERVATION SYSTEM ---")
        print("1. Add Room\n2. View Availability\n3. Book Room\n4. Check Out\n5. Save\n6. Load\n7. Exit")
        choice = input("Select: ")
        if choice == '1': add_room()
        elif choice == '2': view_rooms()
        elif choice == '3': book_room()
        elif choice == '4': check_out()
        elif choice == '5': save_data()
        elif choice == '6': load_data()
        elif choice == '7': break
def add_room():
    r_num = input("Room Number: ")
    if r_num in rooms: return
    r_type = input("Type (Single/Double/Suite): ")
    price = float(input("Price per Night: "))
    rooms[r_num] = {"type": r_type, "price": price, "status": "Available", "guest": None, "check_in": None}
def view_rooms():
    for r_num, info in rooms.items():
        print(f"Room {r_num} [{info['type']}] - {info['status']} - ${info['price']}/night")
def book_room():
    r_num = input("Room Number: ")
    if r_num in rooms and rooms[r_num]["status"] == "Available":
        rooms[r_num]["guest"] = input("Guest Name: ")
        rooms[r_num]["check_in"] = input("Check-in Date (YYYY-MM-DD): ")
        rooms[r_num]["status"] = "Occupied"
        print("Room booked successfully.")
    else: print("Room not available or doesn't exist.")
def check_out():
    r_num = input("Room Number: ")
    if r_num in rooms and rooms[r_num]["status"] == "Occupied":
        out_date = input("Check-out Date (YYYY-MM-DD): ")
        d1 = datetime.strptime(rooms[r_num]["check_in"], "%Y-%m-%d")
        d2 = datetime.strptime(out_date, "%Y-%m-%d")
        nights = (d2 - d1).days
        if nights < 1: nights = 1
        total = nights * rooms[r_num]["price"]
        print(f"Guest: {rooms[r_num]['guest']} | Nights: {nights} | Total: ${total:.2f}")
        rooms[r_num]["status"] = "Available"
        rooms[r_num]["guest"] = None
        rooms[r_num]["check_in"] = None
def save_data():
    with open("hotel.txt", "w") as f:
        for r_num, i in rooms.items():
            f.write(f"{r_num},{i['type']},{i['price']},{i['status']},{i['guest']},{i['check_in']}\n")
def load_data():
    global rooms
    if os.path.exists("hotel.txt"):
        with open("hotel.txt", "r") as f:
            for line in f:
                p = line.strip().split(",")
                rooms[p[0]] = {"type": p[1], "price": float(p[2]), "status": p[3], "guest": p[4] if p[4] != 'None' else None, "check_in": p[5] if p[5] != 'None' else None}
if __name__ == "__main__":
    main_menu()