import random


CHOICES = ["rock", "paper", "scissors"]
BEATS = {"rock": "scissors", "paper": "rock", "scissors": "paper"}


def play(player):
    computer = random.choice(CHOICES)
    if player == computer:
        return f"Tie! Both picked {player}."
    if BEATS[player] == computer:
        return f"You win! {player} beats {computer}."
    return f"You lose! {computer} beats {player}."


if __name__ == "__main__":
    print(play("rock"))
