import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ''
    digits = string.digits if use_digits else ''
    symbols = string.punctuation if use_symbols else ''

    all_chars = lower + upper + digits + symbols

    if not all_chars:
        return "❌ Please select at least one character set."

    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def menu():
    print("🔐 Welcome to Password Generator!")
    try:
        length = int(input("Enter desired password length (e.g., 12): "))
    except ValueError:
        print("⚠️ Invalid input. Using default length = 12.")
        length = 12

    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_upper, use_digits, use_symbols)
    print(f"\n✅ Your generated password is: {password}")

menu()
