if __name__ == "__main__":
    _list = []
    for i in range(int(input('length of list: '))):
        _list.append(input(f'index-{i+1}: '))
    print(' '.join(_list))
