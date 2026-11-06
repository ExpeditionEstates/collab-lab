import random


def flip(n=10):
    results = [random.choice(["heads", "tails"]) for _ in range(n)]
    return results, results.count("heads"), results.count("tails")


if __name__ == "__main__":
    flips, heads, tails = flip()
    print("Flips:", flips)
    print(f"Heads: {heads}  Tails: {tails}")
