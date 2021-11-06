if __name__ == "__main__":
    file_path = '83_read_text.txt'
    content = []

    with open(file_path) as file:
        for line in file:
            content.append(line)
        print(content)
