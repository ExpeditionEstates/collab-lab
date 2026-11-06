def count_vowels(text):
    vowels = "aeiou"
    counts = {v: 0 for v in vowels}
    for ch in text.lower():
        if ch in counts:
            counts[ch] += 1
    return counts


if __name__ == "__main__":
    print(count_vowels("Hello World"))
