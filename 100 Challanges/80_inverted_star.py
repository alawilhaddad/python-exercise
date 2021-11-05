def star(number):
    for i in list(sorted(range(1, number + 1), reverse=True)):
        print("* " * i)


if __name__ == "__main__":
    number = int(input("input number: "))
    star(number)
