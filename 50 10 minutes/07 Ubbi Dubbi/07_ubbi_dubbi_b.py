def remover():
    words = []
    file = open("07_ubbi_dubbi_b.txt", "r")
    text = file.read().strip("\n").split()
    for i, word in enumerate(text):
        if word[:9] == "Einstein":
            print(i)
            text[i] = "_"
    print(" ".join(text))


if __name__ == "__main__":
    remover()
