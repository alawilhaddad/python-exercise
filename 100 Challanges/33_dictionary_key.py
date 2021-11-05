if __name__ == "__main__":
    dictionary = {}
    for i in range(int(input('length of dictionary: '))):
        key = input(f'key-{i+1}: ')
        value = input(f'value-{i+1}: ')
        dictionary[key] = value
    search = input("search: ")
    is_avail = True if search in dictionary.keys() else False
    print(is_avail)
