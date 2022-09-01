def my_sum(numbers, init=0):
    answer = init
    for number in numbers:
        answer += number
    print(answer)


if __name__ == "__main__":
    print(my_sum(input("input numbers: ").split(" "), int(input("input initial number"))))
