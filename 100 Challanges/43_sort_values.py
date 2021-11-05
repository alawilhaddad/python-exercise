if __name__ == "__main__":
    dictionary = {}
    for i in range(int(input('length of dictionary: '))):
        key = input(f'key-{i+1}: ')
        value = sorted(map(lambda x: int(x), input(f'value-{i+1}: ').split()))
        dictionary[key] = value

    print(dictionary)