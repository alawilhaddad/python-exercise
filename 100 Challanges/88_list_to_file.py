if __name__ == "__main__":
    file_path = '88_list_to_file.txt'
    _list = input('input first list (separated by space): ').split(' ')

    with open(file_path, "w") as file:
        for element in _list:
            file.write(f"{element}\n")