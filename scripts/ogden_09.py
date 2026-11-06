def is_palindrome(s):
    t = "".join(c.lower() for c in s if c.isalnum())
    return t == t[::-1]


if __name__ == "__main__":
    print(is_palindrome("Racecar"))
    print(is_palindrome("hello"))
