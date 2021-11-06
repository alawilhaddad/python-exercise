def search(_list, x):
    count = 0
    for num in _list:
        if num == x:
            count += 1
    return count


if __name__ == "__main__":
    numbers = list(map(lambda x: int(x), input("input numbers (separated with space): ").split()))
    obj = int(input("number to search: "))
    print(search(numbers, obj))
