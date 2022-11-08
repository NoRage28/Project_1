import random
import string


def get_random_username():
    letters = string.ascii_letters
    username = "".join(random.choice(letters) for _ in range(random.randint(5, 10)))
    return username


def get_random_password():
    characters = string.ascii_letters + string.digits
    password = "".join(random.choice(characters) for _ in range(random.randint(8, 10)))
    return password


def get_random_text():
    characters = string.ascii_lowercase + string.whitespace
    text = "".join(random.choice(characters) for _ in range(random.randint(5, 10)))
    return text
