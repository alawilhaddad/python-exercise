if __name__ == '__main__':
    list_a = input('input first list (separated by space): ').split(' ')
    list_b = input('input second list (separated by space): ').split(' ')
    common = []

    for char1 in list_a:
        if char1 in list_b:
            common.append(char1)
    print(common)
