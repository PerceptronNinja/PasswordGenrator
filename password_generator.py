import random
import string

def generate_password(length, include_uppercase, include_numbers, include_special):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_uppercase else ""
    numbers = string.digits if include_numbers else ""
    special = string.punctuation if include_special else ""
    all_chars = lower + upper + numbers + special

    if not all_chars:
        return "Please select at least one option!"

    return "".join(random.choice(all_chars) for _ in range(length))
