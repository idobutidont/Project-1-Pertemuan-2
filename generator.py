import random
import string

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
