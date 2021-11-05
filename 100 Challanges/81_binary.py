def binary(num):
    if num == 0:
        return '0'
    else:
        return (binary(num // 2) + str(num % 2)).lstrip("0")


if __name__ == "__main__":
    number = int(input("input number: "))
    binary(number)
