if __name__ == "__main__":
    text = list(input('input string: '))
    index = int(input('index to remove: '))
    for i, char in enumerate(text):
        if i == index:
            text[i] = ""
    print("".join(text))
