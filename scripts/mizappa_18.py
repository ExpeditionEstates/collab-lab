import random


def new_game(width=10, height=10):
    snake = [(height // 2, width // 2)]
    food = (random.randrange(height), random.randrange(width))
    return {"snake": snake, "food": food, "score": 0}


def step(game, direction):
    head = game["snake"][0]
    moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
    dy, dx = moves[direction]
    new_head = (head[0] + dy, head[1] + dx)
    game["snake"].insert(0, new_head)
    if new_head == game["food"]:
        game["score"] += 10
    else:
        game["snake"].pop()
    return game["score"]


if __name__ == "__main__":
    game = new_game()
    print("Score after moving right:", step(game, "right"))
