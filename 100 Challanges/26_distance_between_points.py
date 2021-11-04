import math

if __name__ == '__main__':
    list_a = input('input first list (separated by space): ').split(' ')
    list_a = list(map(lambda x: int(x), list_a))

    list_b = input('input second list (separated by space): ').split(' ')
    list_b = list(map(lambda x: int(x), list_b))

    answer = []
    for i in range(3):
        answer.append((list_a[i] - list_b[i]) ** 2)
    print(math.sqrt(sum(answer)))
