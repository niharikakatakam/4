import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    """Generate a random password based on user-defined criteria."""
    characters = ""

    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Please choose at least one character set (letters, numbers, or symbols).")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    # Get user input for password criteria
    length = int(input("Enter the desired password length: "))
    use_letters = input("Include letters (yes/no)? ").lower() == 'yes'
    use_numbers = input("Include numbers (yes/no)? ").lower() == 'yes'
    use_symbols = input("Include symbols (yes/no)? ").lower() == 'yes'

    # Generate password
    password = generate_password(length, use_letters, use_numbers, use_symbols)

    # Display the generated password
    if password:
        print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()
