if __name__ == "__main__":
    dictionary = {}
    is_equal = None
    for i in range(int(input('length of first dictionary: '))):
        key_value = input(f'new key-value (separate with space): ').split()
        dictionary[key_value[0]] = key_value[1]

    if dictionary != {}:
        for i, value1 in enumerate(dictionary.values()):
            for j, value2 in enumerate(dictionary.values()):
                is_equal = True if value1 == value2 else False
        print(is_equal)
    else:
        print("Empty")
