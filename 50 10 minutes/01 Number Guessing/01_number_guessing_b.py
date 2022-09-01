import random


def ran():
    number = random.randint(1, 101)
    base = random.choice([2, 10, 16])
    if base == 2:
        answer = bin(number)[2:]
    elif base == 10:
        answer = number
    else:
        answer = hex(number).upper()[2:]
    print(answer)


if __name__ == "__main__":
    ran()
