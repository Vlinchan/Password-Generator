import secrets
import string

def generate_secure_password(length, use_upper, use_lower, use_digits, use_symbols):
    
    characters = ""
    
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: Please select at least one character type!"

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


# ---- User Input Section ----
print("🔐 SECURE PASSWORD GENERATOR 🔐")

length = int(input("Enter password length: "))

use_upper = input("Include Uppercase? (y/n): ").lower() == 'y'
use_lower = input("Include Lowercase? (y/n): ").lower() == 'y'
use_digits = input("Include Numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include Symbols? (y/n): ").lower() == 'y'

password = generate_secure_password(length, use_upper, use_lower, use_digits, use_symbols)

print("\nGenerated Secure Password:", password)