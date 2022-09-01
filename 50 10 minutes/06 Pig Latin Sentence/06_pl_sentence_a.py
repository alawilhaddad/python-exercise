def read_text(limit):
    file = open("06_pl_sentence_a.txt", "r")
    text = file.readlines()
    for i in range(limit):
        print(text[i], end="")


if __name__ == "__main__":
    read_text(5)
