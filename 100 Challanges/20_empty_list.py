if __name__ == "__main__":
    _list = []
    for i in range(int(input('length of list: '))):
        _list.append(int(input(f'index-{i+1}: ')))
    if not _list:
        print('Empty')
    else:
        print(f'Not Empty')