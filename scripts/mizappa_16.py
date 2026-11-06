import random


def check(secret, guess):
    if guess < secret:
        return "Too low!"
    if guess > secret:
        return "Too high!"
    return "You guessed it!"


if __name__ == "__main__":
    secret = random.randint(1, 100)
    for guess in (10, 50, 75):
        print(guess, "->", check(secret, guess))
        if guess == secret:
            break
    print("The secret was:", secret)
