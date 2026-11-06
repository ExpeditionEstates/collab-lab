import math


def gcd(a, b):
    return math.gcd(a, b)


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


if __name__ == "__main__":
    print(gcd(12, 18), lcm(12, 18))
