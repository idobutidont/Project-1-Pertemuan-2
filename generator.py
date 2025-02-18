import random
import string
import os

def generate_password(length, char_upper, char_lower, digits, special):
    if char_upper + char_lower + digits + special > length:
        raise ValueError("The sum of specified character counts exceeds the total password length")

    password = []
    password += random.choices(string.ascii_uppercase, k=char_upper)
    password += random.choices(string.ascii_lowercase, k=char_lower)
    password += random.choices(string.digits, k=digits)
    password += random.choices(string.punctuation, k=special)

    if len(password) < length:
        remaining_length = length - len(password)
        password += random.choices(string.ascii_letters + string.digits + string.punctuation, k=remaining_length)

    random.shuffle(password)
    return ''.join(password)

def print_password():
    length = int(input("Enter the length of the password: "))
    num_uppercase = int(input("Enter the number of uppercase letters: "))
    num_lowercase = int(input("Enter the number of lowercase letters: "))
    num_digits = int(input("Enter the number of digits: "))
    num_special = int(input("Enter the number of special characters: "))
    os.system('clear')

    print(f"Your newly generated password is: {generate_password(length, num_uppercase, num_lowercase, num_digits, num_special)}")