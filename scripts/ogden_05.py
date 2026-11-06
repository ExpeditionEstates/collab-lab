from datetime import date


def days_between(d1, d2):
    return abs((d2 - d1).days)


if __name__ == "__main__":
    print(days_between(date(2026, 1, 1), date(2026, 11, 6)))
