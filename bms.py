import os
accounts = {}
def main_menu():
    while True:
        print("\n--- BANKING SYSTEM ---")
        print("1. Create Account\n2. Login\n3. Exit")
        choice = input("Select: ")
        if choice == '1': create_account()
        elif choice == '2': login()
        elif choice == '3': break
def create_account():
    acc_num = input("Account Number: ")
    if acc_num in accounts: return
    name = input("Name: ")
    pin = input("Set 4-Digit PIN: ")
    accounts[acc_num] = {"name": name, "pin": pin, "balance": 0.0, "history": []}
def login():
    acc_num = input("Account Number: ")
    if acc_num in accounts:
        attempts = 0
        while attempts < 3:
            pin = input("Enter PIN: ")
            if pin == accounts[acc_num]["pin"]:
                account_dashboard(acc_num)
                return
            attempts += 1
            print(f"Incorrect. {3-attempts} attempts left.")
def account_dashboard(acc_num):
    while True:
        print(f"\nWelcome {accounts[acc_num]['name']} | Balance: {accounts[acc_num]['balance']}")
        print("1. Deposit\n2. Withdraw\n3. Transfer\n4. History\n5. Logout")
        choice = input("Select: ")
        if choice == '1':
            amt = float(input("Amount: "))
            accounts[acc_num]["balance"] += amt
            accounts[acc_num]["history"].append(f"Deposited {amt}")
        elif choice == '2':
            amt = float(input("Amount: "))
            if accounts[acc_num]["balance"] >= amt:
                accounts[acc_num]["balance"] -= amt
                accounts[acc_num]["history"].append(f"Withdrew {amt}")
            else: print("Insufficient funds.")
        elif choice == '3':
            target = input("Target Account: ")
            if target in accounts:
                amt = float(input("Amount: "))
                if accounts[acc_num]["balance"] >= amt:
                    accounts[acc_num]["balance"] -= amt
                    accounts[target]["balance"] += amt
                    accounts[acc_num]["history"].append(f"Transferred {amt} to {target}")
                    accounts[target]["history"].append(f"Received {amt} from {acc_num}")
            else: print("Account not found.")
        elif choice == '4':
            for entry in accounts[acc_num]["history"]: print(entry)
        elif choice == '5': break
def save_data():
    with open("bank.txt", "w") as f:
        for acc, info in accounts.items():
            hist = "|".join(info["history"])
            f.write(f"{acc},{info['name']},{info['pin']},{info['balance']},{hist}\n")
def load_data():
    global accounts
    if os.path.exists("bank.txt"):
        with open("bank.txt", "r") as f:
            for line in f:
                p = line.strip().split(",")
                if len(p) == 5:
                    h = p[4].split("|") if p[4] else []
                    accounts[p[0]] = {"name": p[1], "pin": p[2], "balance": float(p[3]), "history": h}
if __name__ == "__main__":
    load_data()
    main_menu()
    save_data()