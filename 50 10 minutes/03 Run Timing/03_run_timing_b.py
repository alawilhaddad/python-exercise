from decimal import *


def add(a, b):
    getcontext().prec = 1
    answer = Decimal(a) + Decimal(b)
    print(answer)


if __name__ == "__main__":
    add(input("1: "), input("2: "))
