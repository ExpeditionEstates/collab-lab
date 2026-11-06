import random


def pick_numbers(count=6, top=49):
    return sorted(random.sample(range(1, top + 1), count))


def draw_ticket():
    numbers = pick_numbers()
    bonus = random.randint(1, 49)
    return numbers, bonus


if __name__ == "__main__":
    numbers, bonus = draw_ticket()
    print("Your lucky numbers:", numbers, "bonus:", bonus)
