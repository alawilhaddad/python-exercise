if __name__ == '__main__':
    _list = sorted(input('input first list (separated by space): ').split(' '))
    frequency = {}
    for char in _list:
        if char not in frequency:
            frequency[char] = 1
        else:
            frequency[char] += 1
    print(frequency)
