import random
import string

print("===== PASSWORD GENERATOR =====")

# Get password length
length = int(input("Enter password length: "))

# User choices
use_letters = input("Include letters (y/n): ")
use_numbers = input("Include numbers (y/n): ")
use_symbols = input("Include symbols (y/n): ")

characters = ""

# Add selected character sets
if use_letters.lower() == "y":
    characters += string.ascii_letters

if use_numbers.lower() == "y":
    characters += string.digits

if use_symbols.lower() == "y":
    characters += string.punctuation

# Check if at least one option is selected
if characters == "":
    print("Error: Select at least one character type!")
else:
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:", password)
