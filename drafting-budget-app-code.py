import json
import os
from datetime import datetime
DATA_DIR = "data"
TX_FILE = os.path.join(DATA_DIR, "transactions.json")
BD_FILE = os.path.join(DATA_DIR, "budgets.json")
def setup():
    if not os.path.exists(DATA_DIR): os.makedirs(DATA_DIR)
    for f in [TX_FILE, BD_FILE]:
        if not os.path.exists(f):
            with open(f, 'w') as file: json.dump([], file)
def load(p):
    with open(p, 'r') as f: return json.load(f)
def save(p, d):
    with open(p, 'w') as f: json.dump(d, f, indent=4)
def run_menu():
    setup()
    while True:
        print("\n" + "="*30)
        print("   PERSONAL FINANCE HELPER")
        print("="*30)
        print("1. Record a Receipt (Expense)")
        print("2. Record Income")
        print("3. See My Monthly Report")
        print("4. Set a Spending Limit")
        print("5. Exit Program")
        choice = input("\nWhat would you like to do? (Type 1-5): ")
        if choice in ['1', '2']:
            t_type = "expense" if choice == '1' else "income"
            cat = input("What is the category? (e.g. Food, Rent, Salary): ")
            try:
                amt_str = input("How much was it? (Just the numbers): ")
                amt = float(amt_str.replace('$', '').replace(',', ''))
                desc = input("Add a short note (e.g. 'Lunch at cafe'): ")
                data = load(TX_FILE)
                data.append({"date": datetime.now().strftime("%Y-%m-%d"), "type": t_type, "category": cat, "description": desc, "amount": amt})
                save(TX_FILE, data)
                print(f"✅ Success! I've written down that {t_type}.")
            except ValueError: print("❌ Error: Please type only numbers for the amount.")
        elif choice == '3':
            txs = load(TX_FILE)
            inc = sum(t['amount'] for t in txs if t['type'] == 'income')
            exp = sum(t['amount'] for t in txs if t['type'] == 'expense')
            print(f"\n--- YOUR SUMMARY ---")
            print(f"Total Money In:  ${inc:,.2f}")
            print(f"Total Money Out: ${exp:,.2f}")
            print(f"Money Leftover:  ${(inc - exp):,.2f}")
            if inc > 0:
                rate = ((inc - exp) / inc) * 100
                print(f"Savings Rate:    {rate:.1f}%")
        elif choice == '4':
            cat = input("Which category do you want a limit for?: ")
            try:
                limit = float(input(f"What is your monthly limit for {cat}?: "))
                buds = [b for b in load(BD_FILE) if b['category'] != cat]
                buds.append({"category": cat, "limit": limit})
                save(BD_FILE, buds)
                print(f"✅ OK! I'll watch your {cat} spending.")
            except ValueError: print("❌ Error: Use numbers for the limit.")
        elif choice == '5':
            print("Goodbye! Your data is safely saved.")
            break
if __name__ == "__main__":
    run_menu()