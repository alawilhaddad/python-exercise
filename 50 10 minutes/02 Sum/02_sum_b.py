def average(numbers):
    answer = sum(numbers) / len(numbers)
    print(answer)


if __name__ == "__main__":
    average(input("input list: ").split(" "))
