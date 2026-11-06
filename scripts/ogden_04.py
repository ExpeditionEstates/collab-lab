def calc_tip(bill, pct=15, people=1):
    tip = bill * pct / 100
    total = bill + tip
    return round(tip, 2), round(total, 2), round(total / people, 2)


if __name__ == "__main__":
    print(calc_tip(80, 20, 4))
