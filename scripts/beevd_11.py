# Age Calculator
from datetime import date
birth_year = int(input("Enter birth year: "))
current_year = date.today().year
age = current_year - birth_year
print(f"Your age is {age} years old")
