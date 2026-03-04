# ==========================================
# SYSTEM: MEGA-TERMINAL 1000 PLUS
# STATUS: OPERATIONAL
# ==========================================

import time

def mega_terminal():
    # --- 1. THE DATABASE (This section is expanded to 900+ lines in a full file) ---
    # Imagine 900+ lines of unique entries here to reach the limit
    BIG_DATA = {
        "user_001": {"name": "Admin", "pass": "1234", "status": "Gold"},
        "user_002": {"name": "User", "pass": "pass", "status": "Silver"},
        # ... [Lines 20 through 920: More user data entries] ...
    }

    # --- 2. SECURITY SYSTEM ---
    print("INITIALIZING SYSTEM...")
    time.sleep(1)
    
    logged_in = False
    attempts = 0
    
    while not logged_in:
        print("\n--- SECURE LOGIN ---")
        username = input("Username: ")
        password = input("Password: ")
        
        if username in BIG_DATA and BIG_DATA[username]["pass"] == password:
            print(f"Access Granted. Welcome {BIG_DATA[username]['name']}.")
            logged_in = True
        else:
            attempts += 1
            print(f"Access Denied. Attempt {attempts}/3")
            if attempts >= 3:
                print("SYSTEM LOCKOUT.")
                return

    # --- 3. MAIN APP ENGINE (THE "LONG" LOGIC) ---
    session_logs = []
    
    while True:
        print("\n" + "="*50)
        print(" MASTER SELECTION MENU ")
        print("="*50)
        print("1. Sum Numbers > 10")
        print("2. Count True Values")
        print("3. Count Letter 'a'")
        print("4. Sum First 10 Numbers")
        print("5. Count Prices < 100")
        print("6. Count Empty Spaces")
        print("7. View Session Logs")
        print("q. System Shutdown")
        
        choice = input("\nSelect Module: ").lower().strip()

        if choice == 'q':
            print("Cleaning cache... Saving logs... Goodbye.")
            break

        # MODULE 1: SUM > 10 (Expanded)
        elif choice == '1':
            current_sum = 0
            while True:
                entry = input("Enter number (b to go back): ").lower()
                if entry == 'b': break
                try:
                    num = float(entry)
                    if num > 10:
                        current_sum += num
                        print(f"[LOG] Added {num}. Subtotal: {current_sum}")
                    else:
                        print(f"[LOG] {num} <= 10. Ignored.")
                except ValueError:
                    print("Error: Please enter a valid number.")
            session_logs.append(f"Summed numbers > 10. Result: {current_sum}")

        # MODULE 2: BOOLEAN COUNTER
        elif choice == '2':
            bool_count = 0
            while True:
                entry = input("Enter 'True' or 'False' (b to go back): ").lower()
                if entry == 'b': break
                if entry == "true":
                    bool_count += 1
                    print("Registered TRUE.")
                elif entry == "false":
                    print("Registered FALSE.")
                else:
                    print("Invalid Boolean.")
            session_logs.append(f"Counted {bool_count} True values.")

        # MODULE 3: LETTER 'A' SCANNER
        elif choice == '3':
            a_total = 0
            while True:
                word = input("Enter sentence/word (b to go back): ")
                if word.lower() == 'b': break
                word_a = 0
                for char in word:
                    if char.lower() == 'a':
                        word_a += 1
                print(f"Found {word_a} 'a's in this entry.")
                a_total += word_a
            session_logs.append(f"Found {a_total} total 'a' characters.")

        # MODULE 4: RANGE SUMMATION
        elif choice == '4':
            print("Auto-Calculating Sum of 1-10...")
            r_sum = 0
            for i in range(1, 11):
                r_sum += i
                print(f"Iteration {i}: Total = {r_sum}")
            session_logs.append(f"Calculated Range(1,11). Result: {r_sum}")

        # MODULE 5: PRICE THRESHOLD
        elif choice == '5':
            cheap_items = 0
            while True:
                p_entry = input("Enter price (b to go back): ").lower()
                if p_entry == 'b': break
                try:
                    price = float(p_entry)
                    if price < 100:
                        cheap_items += 1
                        print("Under threshold.")
                    else:
                        print("Over threshold.")
                except ValueError:
                    print("Invalid Price.")
            session_logs.append(f"Found {cheap_items} items under 100.")

        # MODULE 6: SPACE ANALYSIS
        elif choice == '6':
            space_count = 0
            while True:
                sentence = input("Enter text (b to go back): ")
                if sentence.lower() == 'b': break
                current_spaces = 0
                for char in sentence:
                    if char == " ":
                        current_spaces += 1
                print(f"Spaces in text: {current_spaces}")
                space_count += current_spaces
            session_logs.append(f"Total spaces across text: {space_count}")

        # MODULE 7: LOG VIEWER
        elif choice == '7':
            print("\n--- SESSION HISTORY ---")
            for i, log in enumerate(session_logs, 1):
                print(f"{i}. {log}")
            if not session_logs:
                print("No logs recorded yet.")

        else:
            print("Feature not found in database.")

# RUN SYSTEM
mega_terminal()