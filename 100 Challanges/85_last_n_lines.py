if __name__ == "__main__":
    file_path = '85_last_n_lines.txt'
    content = []
    n = int(input("input n: "))

    with open(file_path) as file:
        lines = file.readlines()
        lines_num = len(file.readlines())
    if n > lines_num:
        for i in lines[lines_num-n::]:
            print(i.rstrip('\n'))

    else:
        print(f"Please enter a valid value. The file has {lines_num} lines. ")
