import random


SYMBOLS = ["cherry", "lemon", "bell", "star", "seven"]
PAYOUTS = {"cherry": 2, "lemon": 3, "bell": 5, "star": 10, "seven": 50}


def spin():
    return [random.choice(SYMBOLS) for _ in range(3)]


def payout(reels):
    if reels[0] == reels[1] == reels[2]:
        return PAYOUTS[reels[0]]
    return 0


if __name__ == "__main__":
    reels = spin()
    print("Reels:", reels, "-> payout:", payout(reels))
