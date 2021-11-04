if __name__ == '__main__':
    _list = input('input first list (separated by space): ').split(' ')
    _list = list(map(lambda x: int(x), _list))
    duplicate = _list
    if len(_list) < 2:
        second = None
    else:
        for i in range(duplicate.count(min(_list))):
            duplicate.remove(min(_list))
        print(f'second largest value: {min(duplicate)}')
