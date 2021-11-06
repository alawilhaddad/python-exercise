if __name__ == "__main__":
    file_path = '89_char_count.txt'

    with open(file_path) as file:
        lines = list(map(lambda x: x.rstrip("\n"), file.readlines()))
        lines = list(map(lambda x: x.replace(" ", ""), lines))
    count = 0
    for sentence in lines:
        for char in sentence:
            count += 1

    print(count)
