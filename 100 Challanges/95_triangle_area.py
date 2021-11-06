import math

if __name__ == "__main__":
    a, t = list(map(lambda x: int(x), input('input base length and height: ').split()))
    # noinspection PyTypeChecker
    area = 0.5 * a * t
    print(round(area, 2))
