if __name__ == "__main__":
    _list = []
    my_dict = {}
    for i in range(int(input('length of list: '))):
        _list.append(input(f'index-{i+1}: ').split(" "))

    for value in _list:
        my_dict[value[0]] = value[1]

    print(my_dict)
