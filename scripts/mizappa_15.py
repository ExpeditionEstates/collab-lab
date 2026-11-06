import random


WORDS = ["python", "galaxy", "puzzle", "rocket", "meadow"]


def hangman(word, guesses):
    shown = "".join(c if c in guesses else "_" for c in word)
    wrong = [g for g in guesses if g not in word]
    return shown, len(wrong)


if __name__ == "__main__":
    word = random.choice(WORDS)
    shown, wrong = hangman(word, ["p", "y", "e"])
    print(f"Word: {shown}  wrong guesses: {wrong}")
