import random
import string


def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(alphabet) for _ in range(length))


if __name__ == "__main__":
    print(generate_password(16))
