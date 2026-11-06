import random


SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


def new_deck():
    deck = [f"{rank} of {suit}" for suit in SUITS for rank in RANKS]
    random.shuffle(deck)
    return deck


def deal(deck, count=5):
    return [deck.pop() for _ in range(count)]


if __name__ == "__main__":
    deck = new_deck()
    print("Your hand:", deal(deck))
    print("Cards left in deck:", len(deck))
