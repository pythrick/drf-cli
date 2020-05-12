import random
import string
import os


def create_random_secret_key():
    chars = string.ascii_letters + string.digits + "!@#$%ˆ*()-_+=[]]{}\/?.,'"
    secret_key = "".join(random.choice(chars) for _ in range(32))
    with open(".secrets.yaml", "w+") as secrets_file:
        secrets_file.write("default:")
        secrets_file.write(f"  SECRET_KEY: {secret_key}")


if __name__ == '__main__':
    create_random_secret_key()
