import random
import string

def generate_password(length, uppercase=True, lowercase=True, numbers=True, special_chars=True):
    characters = ""
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    if not characters:
        print("Error: Please enable at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords, length, uppercase=True, lowercase=True, numbers=True, special_chars=True):
    passwords = []
    for _ in range(num_passwords):
        password = generate_password(length, uppercase, lowercase, numbers, special_chars)
        if password:
            passwords.append(password)
    return passwords

if __name__ == "__main__":
    print("Welcome to the Secure Password Generator!")

    length = int(input("Enter the length of the password: "))
    num_passwords = int(input("Enter the number of passwords to generate: "))
    uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    numbers = input("Include numbers? (y/n): ").lower() == 'y'
    special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    passwords = generate_multiple_passwords(num_passwords, length, uppercase, lowercase, numbers, special_chars)

    print("\nGenerated Passwords:")
    for i, password in enumerate(passwords, start=1):
        print(f"Password {i}: {password}")
