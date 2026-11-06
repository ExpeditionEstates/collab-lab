num = int(input("Enter a number: "))
digits = str(num)
power = len(digits)
total = sum(int(d) ** power for d in digits)
if total == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
