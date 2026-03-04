import random
import string

def generate_password():
    print("\n--- Password Generator ---")
    try:
        length = int(input("Enter desired password length: "))
    except ValueError:
        print("Invalid input. Using default length of 12.")
        length = 12
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    char_pool = ""
    if use_upper: char_pool += string.ascii_uppercase
    if use_lower: char_pool += string.ascii_lowercase
    if use_digits: char_pool += string.digits
    if use_symbols: char_pool += string.punctuation
    if not char_pool:
        print("Error: You must select at least one character type!")
        return
    password = "".join(random.choice(char_pool) for _ in range(length))
    print("Generated Password:", password)
    return password
def check_strength():
    print("\n--- Password Strength Checker ---")
    password = input("Enter password to check: ")
    score = 0
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)
    if length >= 8: score += 1
    if length >= 12: score += 1
    if has_upper and has_lower: score += 1
    if has_digit: score += 1
    if has_symbol: score += 1
    if score <= 2:
       strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"
    print(f"Strength Rating: {strength} ({score}/5)")
def main():
    while True:
        print("\n1. Generate Password")
        print("2. Check Password Strength")
        print("3. Exit")
        choice = input("Select an option (1-3): ")

        if choice == '1':
            generate_password()
        elif choice == '2':
            check_strength()
        elif choice == '3':
            break
        else:
            print("Invalid selection.")
if __name__ == "__main__":
    main()