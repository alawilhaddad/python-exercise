if __name__ == "__main__":
    dictionary = {}
    for i in range(int(input('length of dictionary: '))):
        key = input(f'key-{i+1}: ')
        value = map(lambda x: int(x), input(f'value-{i+1}: ').split())
        dictionary[key] = value
        max_sum = sum(dictionary.get(key))

    for value in dictionary.values():
        # noinspection PyUnboundLocalVariable
        if sum(value) > max_sum:
            max_sum = sum(value)
    print(max_sum)
