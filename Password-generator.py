import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("You must select at least one type of character to include in the password.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired password length: "))
        
        if length <= 0:
            print("Please enter a positive number.")
            return

        use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        print("Generated Password:", password)
        
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()