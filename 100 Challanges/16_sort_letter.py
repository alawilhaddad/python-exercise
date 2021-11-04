if __name__ == "__main__":
    text = input('input string: ').split(' ')
    for i, word in enumerate(text):
        text[i] = ''.join(sorted(list(word.lower())))
    print(' '.join(text))
