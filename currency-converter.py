rates = {
    "USD": 1.0,
    "EUR": 0.92,
    "GBP": 0.79,
    "KES": 130.0
}
def convert_currency():
    rates = {
        "USD": 1.0,
        "EUR": 0.92,
        "GBP": 0.79,
        "KES": 130.0
    }
    print("--- Currency Converter ---")
    print(f"Available currencies: {', '.join(rates.keys())}")
    while True:
        base = input("\nEnter base currency (or 'exit' to quit): ").upper()
        if base == 'EXIT': 
            break
        target = input("Enter target currency: ").upper()
        if base not in rates or target not in rates:
            print("Invalid currency code. Please try again.")
            continue
        try:
            amount = float(input(f"Enter amount in {base}: "))
        except ValueError:
            print("Please enter a valid numeric amount.")
            continue
        usd_amount = amount / rates[base]
        converted_amount = usd_amount * rates[target]
        print(f"{amount} {base} is equal to {converted_amount:.2f} {target}")
convert_currency()