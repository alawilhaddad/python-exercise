def word_calc(*words):
    length = list(map(len, words))
    _list = [max(length), min(length), average(length)]
    print(_list)


def average(numbers):
    answer = sum(numbers) / len(numbers)
    return answer


if __name__ == "__main__":
    word_calc(input("input words: ").split(" "))
