if __name__ == "__main__":
    text = input("input text: ")
    for i in range(1, len(text)+1):
        print(text[-i], end='')
