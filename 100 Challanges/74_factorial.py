def factorial(number):
    answer = 1
    temp = list(range(number))

    if number == 0:
        return 1
    else:
        for i in temp:
            x = i + 1
            answer *= x
        return answer


if __name__ == "__main__":
    n = int(input("input number: "))
    print(factorial(n))
