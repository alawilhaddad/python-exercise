if __name__ == "__main__":
    file_path = '87_word_frequency.txt'
    frequency = {}

    with open(file_path) as file:
        lines = list(map(lambda x: x.rstrip("\n"), file.readlines()))
        lines_num = len(file.readlines())

    for word in lines:
        if word not in frequency.keys():
            frequency[word] = 1
        else:
            frequency[word] += 1
    print(frequency)
