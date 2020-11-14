import random


def gen_pass():
    chars = list(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890[];:.,<>?/|~`!@#$%^&*()_-+="
    )
    password = ""
    for _ in range(random.choice(range(15, 21))):
        password += random.choice(chars)

    print(password)


if __name__ == "__main__":
    gen_pass()
