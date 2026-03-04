import os
inventory = {}
total_revenue = 0.0

def main_menu():
    """
    Main control loop that keeps the program running.
    Provides the user interface for all system actions.
    """
    global total_revenue
    while True:
        print("\n--- INVENTORY MANAGEMENT SYSTEM ---")
        print("1. Add Product")
        print("2. View Products")
        print("3. Sell Product")
        print("4. Restock Product")
        print("5. View Reports")
        print("6. Save Data")
        print("7. Load Data")
        print("8. Exit")
        choice = input("Select an option (1-8): ")
        if choice == '1':
            add_product()
        elif choice == '2':
            view_products()
        elif choice == '3':
            sell_product()
        elif choice == '4':
            restock_product()
        elif choice == '5':
            view_reports()
        elif choice == '6':
            save_to_file()
        elif choice == '7':
            load_from_file()
        elif choice == '8':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")
def restock_product():
    p_id = input("Enter Product ID to restock: ")
    if p_id in inventory:
        try:
            add_qty = int(input(f"Current stock for {inventory[p_id]['name']} is {inventory[p_id]['stock']}. Enter amount to add: "))
            if add_qty > 0:
                inventory[p_id]['stock'] += add_qty
                print(f"Successfully restocked. New total: {inventory[p_id]['stock']}")
            else:
                print("Quantity must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")
    else:
        print("Error: Product ID not found.")
def add_product():
    """
    Step 1 & 3 Logic: Collects product details and 
    stores them in the nested dictionary structure.
    """
    p_id = input("Enter Product ID: ")
    if p_id in inventory:
        print("Error: Product ID already exists!")
        return
    name = input("Enter Product Name: ")
    try:
        price = float(input("Enter Price: "))
        stock = int(input("Enter Quantity in Stock: "))
        inventory[p_id] = {
            "name": name,
            "price": price,
            "stock": stock,
            "sold": 0
        }
        print(f"Product '{name}' added successfully.")
    except ValueError:
        print("Invalid input. Price must be a number and stock an integer.")
def view_products():
    """
    Displays all items. Includes logic to flag 
    low stock items (quantity less than 5).
    """
    if not inventory:
        print("Inventory is currently empty.")
        return
    print("\nID | Name | Price | Stock | Sold")
    print("-" * 35)
    for p_id, info in inventory.items():
        status = ""
        if info['stock'] < 5:
            status = " (LOW STOCK)"
        
        print(f"{p_id} | {info['name']} | ${info['price']} | {info['stock']} | {info['sold']}{status}")
def sell_product():
    """
    Step 3 Sell Logic: Checks for stock availability, 
    reduces stock, increases 'sold' count, and updates revenue.
    """
    global total_revenue
    p_id = input("Enter Product ID to sell: ")
    if p_id in inventory:
        try:
            qty = int(input("Enter quantity to purchase: "))
            if inventory[p_id]['stock'] >= qty:
                inventory[p_id]['stock'] -= qty
                inventory[p_id]['sold'] += qty
                sale_total = qty * inventory[p_id]['price']
                total_revenue += sale_total
                print(f"Sale Complete! Total Cost: ${sale_total:.2f}")
            else:
                print("Error: Not enough stock available.")
        except ValueError:
            print("Invalid quantity entered.")
    else:
        print("Error: Product ID not found.")
def view_reports():
    """
    Step 4 Reporting: Shows total revenue and 
    identifies the most sold product.
    """
    print(f"\n--- Business Report ---")
    print(f"Total Revenue: ${total_revenue:.2f}")
    if inventory:
        most_sold = max(inventory.values(), key=lambda x: x['sold'])
        if most_sold['sold'] > 0:
            print(f"Top Selling Product: {most_sold['name']} ({most_sold['sold']} units)")
        else:
            print("Top Selling Product: None yet.")
def save_to_file():
    """
    Step 5: File Storage. Iterates through the dictionary 
    and writes data to a comma-separated text file.
    """
    with open("inventory_data.txt", "w") as f:
        for p_id, info in inventory.items():
            line = f"{p_id},{info['name']},{info['price']},{info['stock']},{info['sold']}\n"
            f.write(line)
    print("Data saved to inventory_data.txt")
def load_from_file():
    """
    Step 5: Load Logic. Reads the file, splits the strings by commas, 
    converts types, and restores the dictionary.
    """
    global inventory
    if os.path.exists("inventory_data.txt"):
        inventory = {} 
        with open("inventory_data.txt", "r") as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 5:
                    p_id, name, price, stock, sold = parts
                    inventory[p_id] = {
                        "name": name,
                        "price": float(price),
                        "stock": int(stock),
                        "sold": int(sold)
                    }
        print("Data loaded successfully.")
    else:
        print("No save file found.")
if __name__ == "__main__":
    main_menu()