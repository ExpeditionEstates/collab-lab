import random
import string

def gen_password(n=12):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(n))

if __name__ == "__main__":
    print(gen_password())
