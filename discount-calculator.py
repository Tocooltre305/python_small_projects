original_price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage: "))
discounted_price = original_price * (1 - discount_percentage / 100)
discount_amount = original_price - discounted_price
print(f"The discounted price is {discounted_price} and the discount amount is {discount_amount}.")