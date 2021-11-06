if __name__ == "__main__":
    file_path = '84_first_n_lines.txt'
    content = []
    n = int(input("input n: "))

    with open(file_path) as file:
        lines = file.readlines()
        lines_num = len(file.readlines())

    if n > lines_num:
        for i in range(n):
            print(lines[i].rstrip('\n'))

    else:
        print(f"Please enter a valid value. The file has {lines_num} lines. ")
