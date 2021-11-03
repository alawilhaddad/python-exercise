if __name__ == "__main__":
    text = input('input string: ')
    if len(text) < 2:
        print(text)
    else:
        print(text[1::2])
