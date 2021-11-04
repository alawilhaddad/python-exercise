if __name__ == "__main__":
    text = input('input string: ').split(' ')
    for i, word in enumerate(text):
        text[i] = word.swapcase()[::-1]
    print(' '.join(text))
