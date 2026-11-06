def are_anagrams(a, b):
    norm = lambda s: sorted(c.lower() for c in s if c.isalnum())
    return norm(a) == norm(b)


if __name__ == "__main__":
    print(are_anagrams("listen", "silent"))
    print(are_anagrams("hello", "world"))
