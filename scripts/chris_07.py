import math

def gcd_lcm(a, b):
    g = math.gcd(a, b)
    return g, a * b // g

if __name__ == "__main__":
    print(gcd_lcm(12, 18))
