def reverse_string(text):
    return text[::-1]


def reverse_words(sentence):
    return " ".join(word[::-1] for word in sentence.split())


if __name__ == "__main__":
    print(reverse_string("hello"))
    print(reverse_words("hello world"))
