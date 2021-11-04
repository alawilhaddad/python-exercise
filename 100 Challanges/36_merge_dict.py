if __name__ == "__main__":
    dictionary_1, dictionary_2 = {}, {}
    final_dict = dictionary_1
    for i in range(int(input('length of first dictionary: '))):
        key_value = input(f'new key-value (separate with space): ').split()
        dictionary_1[key_value[0]] = key_value[1]
    for i in range(int(input('length of second dictionary: '))):
        key_value = input(f'new key-value (separate with space): ').split()
        dictionary_2[key_value[0]] = key_value[1]

    for key in dictionary_2.keys():
        final_dict[key] = dictionary_2.get(key)
    print(final_dict)
