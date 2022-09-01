def my_sum(numbers):
    answer = 0
    for number in numbers:
        answer += number
    return answer


if __name__ == "__main__":
    print(my_sum(input("input numbers: ").split(" ")))
    