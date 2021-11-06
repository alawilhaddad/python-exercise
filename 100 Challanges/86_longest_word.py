if __name__ == "__main__":
    file_path = '86_longest_word.txt'
    length = 0
    sel_index = 0

    with open(file_path) as file:
        lines = list(map(lambda x: x.rstrip("\n"), file.readlines()))
        lines_num = len(file.readlines())

    for i, word in enumerate(lines):
        if len(word) > length:
            length = len(word)
            sel_index = i
    print(lines[sel_index])
