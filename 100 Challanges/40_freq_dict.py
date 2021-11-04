if __name__ == "__main__":
    my_dict, freq_dict = {}, {}
    is_equal = None
    for i in range(int(input('length of first dictionary: '))):
        key_value = input(f'new key-value (separate with space): ').split()
        my_dict[key_value[0]] = key_value[1]

    for value in my_dict.values():
        if value in freq_dict.keys():
            freq_dict[value] += 1
        else:
            freq_dict[value] = 1
    print(freq_dict)
