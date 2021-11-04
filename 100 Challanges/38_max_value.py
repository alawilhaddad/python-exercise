if __name__ == "__main__":
    dictionary = {}
    is_equal = None
    for i in range(int(input('length of first dictionary: '))):
        key_value = input(f'new key-value (separate with space): ').split()
        dictionary[key_value[0]] = int(key_value[1])

    if dictionary != {}:
        print(max(dictionary.values()))
    else:
        print("Empty")
