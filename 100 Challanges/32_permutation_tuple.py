import itertools

if __name__ == '__main__':
    _list = sorted(input('input first list (separated by space): ').split(' '))
    x = []
    if len(_list) > 1:
        x = tuple(itertools.permutations(_list, len(_list)))
        print(x)
    else:
        print(tuple(_list))
