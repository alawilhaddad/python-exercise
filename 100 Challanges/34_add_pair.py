if __name__ == "__main__":
    dictionary = {}
    for i in range(int(input('length of dictionary: '))):
        key = input(f'key-{i+1}: ')
        value = input(f'value-{i+1}: ')
        dictionary[key] = value
    new_key = input(f'new key-value (separate with space): ').split()
    if new_key[0] in dictionary.keys():
        pass
    else:
        dictionary[new_key[0]] = new_key[1]
    print(dictionary)
