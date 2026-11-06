def word_count(text):
    return len(text.split())

if __name__ == "__main__":
    s = input("Enter text: ")
    print(f"Words: {word_count(s)}")
