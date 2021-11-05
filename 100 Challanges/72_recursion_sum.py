def sum_of(_list):
    answer = 0
    for i in _list:
        answer += i
    return answer


if __name__ == '__main__':
    _list = list(map(lambda x: int(x), (input('input first list (separated by space): ').split(' '))))
    print(sum_of(_list))
