if __name__ == "__main__":
    _list = []
    flatten = []
    for i in range(int(input('length of list: '))):
        _list.append(input(f'index-{i+1}: ').split(" "))
    for item in _list:
        for j in item:
            flatten.append(j)
    print(flatten)
