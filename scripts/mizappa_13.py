import random


def roll(n=2, sides=6):
    return [random.randint(1, sides) for _ in range(n)]


if __name__ == "__main__":
    dice = roll()
    print("You rolled:", dice, "total:", sum(dice))
