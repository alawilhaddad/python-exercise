if __name__ == "__main__":
    my_dict = {}
    my_list = []
    for i in range(int(input('length of dictionary: '))):
        key = input(f'key-{i+1}: ')
        value = input(f'value-{i+1}: ').split()
        my_dict[key] = value

    for key in my_dict.keys():
        my_list.append([key, my_dict.get(key)])
    print(my_list)
