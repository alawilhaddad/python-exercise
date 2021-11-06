if __name__ == "__main__":
    source = '90_copy_text.txt'
    destination = '90_copy_text(copy).txt'
    with open(source) as file_source:
        lines = list(map(lambda x: x, file_source.readlines()))

    with open(destination, 'w') as file_destination:
        for line in lines:
            file_destination.write(line)
