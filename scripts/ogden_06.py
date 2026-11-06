def to_roman(num):
    table = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
             (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
             (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    out = ""
    for value, symbol in table:
        while num >= value:
            out += symbol
            num -= value
    return out


if __name__ == "__main__":
    print(to_roman(2026))
