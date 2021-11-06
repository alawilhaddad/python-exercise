import math

if __name__ == "__main__":
    r = int(input('input radius: ').strip(' '))
    # noinspection PyTypeChecker
    area = math.pi * (r**2)
    print(round(area, 2))
