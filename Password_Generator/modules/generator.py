import string
import random

def generate_password(length, use_upper, use_lower, use_digits, use_symbols, exclude_chars):
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    characters = ''.join(c for c in characters if c not in exclude_chars)

    if not characters:
        return 'Error: No character set selected.'

    return ''.join(random.choice(characters) for _ in range(length))
