if __name__ == "__main__":
    _list = []
    count = 0
    for i in range(int(input('length of list: '))):
        _list.append(int(input(f'index-{i+1}: ')))

    for num in _list:
        if num > 3:
            count +=1
    print(count)