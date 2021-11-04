if __name__ == "__main__":
    _list = []
    for i in range(int(input('length of list: '))):
        _list.append(input(f'index-{i+1}: '))
    if not _list:
        print('Empty List')
    else:
        for i, char in enumerate(_list):
            print(f'{char} {i}')
