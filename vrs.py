import json
from datetime import datetime
class VehicleRentalSystem:
    def __init__(self):
        self.fleet = {}
        self.revenue = 0.0
        self.load_data()
    def save_data(self):
        data = {"fleet": self.fleet, "revenue": self.revenue}
        with open("rental_data.json", "w") as f:
            json.dump(data, f)
    def load_data(self):
        try:
            with open("rental_data.json", "r") as f:
                data = json.load(f)
                self.fleet = data.get("fleet", {})
                self.revenue = data.get("revenue", 0.0)
        except FileNotFoundError:
            pass
    def add_vehicle(self):
        vid = input("ID: ")
        self.fleet[vid] = {
            "model": input("Model: "),
            "category": input("Category (SUV/Sedan/Luxury): "),
            "rate": float(input("Daily Rate: ")),
            "status": "Available",
            "customer": None,
            "date": None,
            "rent_count": 0
        }
    def view_fleet(self):
        for vid, v in self.fleet.items():
            print(f"[{vid}] {v['model']} | {v['category']} | ${v['rate']}/day | {v['status']}")
    def rent_vehicle(self):
        vid = input("Enter ID: ")
        if vid in self.fleet and self.fleet[vid]["status"] == "Available":
            self.fleet[vid]["customer"] = input("Customer Name: ")
            self.fleet[vid]["date"] = input("Date (YYYY-MM-DD): ")
            self.fleet[vid]["status"] = "Rented"
            self.fleet[vid]["rent_count"] += 1
        else:
            print("Unavailable")
    def return_vehicle(self):
        vid = input("Enter ID: ")
        if vid in self.fleet and self.fleet[vid]["status"] == "Rented":
            d1 = datetime.strptime(self.fleet[vid]["date"], "%Y-%m-%d")
            d2 = datetime.strptime(input("Return Date (YYYY-MM-DD): "), "%Y-%m-%d")
            days = max((d2 - d1).days, 1)
            bill = days * self.fleet[vid]["rate"]
            self.revenue += bill
            self.fleet[vid].update({"status": "Available", "customer": None, "date": None})
            print(f"Total Bill: ${bill}")
    def report(self):
        print(f"Total Revenue: ${self.revenue}")
        cats = [v["category"] for v in self.fleet.values()]
        if cats:
            print(f"Most Popular Category: {max(set(cats), key=cats.count)}")
        print("Currently Rented:", [k for k, v in self.fleet.items() if v["status"] == "Rented"])
    def menu(self):
        actions = {"1": self.add_vehicle, "2": self.view_fleet, "3": self.rent_vehicle, "4": self.return_vehicle, "5": self.report, "6": self.save_data}
        while True:
            print("\n1.Add 2.View 3.Rent 4.Return 5.Report 6.Save 7.Exit")
            ch = input("> ")
            if ch == "7": break
            if ch in actions: actions[ch]()
if __name__ == "__main__":
    VehicleRentalSystem().menu()