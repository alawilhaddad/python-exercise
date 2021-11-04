if __name__ == "__main__":
    _list = []
    for i in range(int(input('length of list: '))):
        _list.append(input(f'index-{i+1}: '))

    for i, char1 in enumerate(_list):
        for j, char2 in enumerate(_list):
            if i == j:
                pass
            else:
                if char1 == char2:
                    _list.pop(j)
    print(_list)
