if __name__ == "__main__":
    _list = []
    for i in range(int(input('length of list: '))):
        x = input(f'index-{i+1}: ')
        if x.isnumeric():
            x = int(x)
        else:
            pass
        _list.append(x)
    factor = int(input('Multiplication factor: '))
    answer = list(map(lambda z: z * factor, _list))
    print(answer)
