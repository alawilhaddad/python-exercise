if __name__ == "__main__":
    _list = []
    for i in range(int(input('length of list: '))):
        _list.append(input(f'index-{i+1}: '))
    element = input('element to remove: ')
    if not _list:
        print('Empty List')
    else:
        if element not in _list:
            print('Not Found')
        else:
            for i in range(_list.count(element)):
                _list.remove(element)
            print(_list)
