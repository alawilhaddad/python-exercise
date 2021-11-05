def power(x, y):
    answer = 1
    for i in range(y):
        answer *= x
    return answer


if __name__ == "__main__":
    a, b = list(map(lambda x: int(x), input("input x and y (x^y): ").split()))
    print(power(a, b))
