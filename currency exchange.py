USD_amount = float(input("Enter amount in USD: "))
Exchange_usd_to_kes = USD_amount * 129
KES_amount = float(input("Enter amount in KES: "))
Exchange_kes_to_usd = KES_amount * 0.0078
print(USD_amount, "USD is equal to", Exchange_usd_to_kes, "KES")
print(KES_amount, "KES is equal to", Exchange_kes_to_usd, "USD")
