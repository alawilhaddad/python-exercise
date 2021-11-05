def factor(value):
    factor_list = []
    temp = value
    i = 2
    while i != temp + 1:
        if temp % i == 0:
            factor_list.append(i)
            temp = temp / i
            i = 2
        else:
            i += 1
    return factor_list


def fpb(factor_1, factor_2):
    temp = []
    for i in factor_1:
        if i in factor_2:
            temp.append(i)
            factor_2.remove(i)
            continue
    answer = 1
    for i in temp:
        answer *= i
    return answer


if __name__ == "__main__":
    a, b = list(map(lambda x: int(x), input("input x and y: ").split()))
    print(fpb(factor(a), factor(b)))
