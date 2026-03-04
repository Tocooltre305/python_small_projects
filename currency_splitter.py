kes_amount = float(input("Enter amount in KES: "))
thousands_notes = kes_amount // 1000
five_hundred_notes = (kes_amount % 1000) // 500 
hundred_notes = (kes_amount % 1000) % 500 // 100
fifty_coins = (kes_amount % 1000) % 500 % 100 // 50
print("Thousands notes:", thousands_notes)
print("Five hundred notes:", five_hundred_notes)
print("Hundred notes:", hundred_notes)
print("Fifty coins:", fifty_coins)