def sum_digit(number):
    answer = 0
    if number.isnumeric():
        for i in number:
            answer += int(i)
    return answer


if __name__ == "__main__":
    n = input("input number: ")
    print(sum_digit(n))
