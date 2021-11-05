if __name__ == "__main__":
    numbers = list(map(lambda x: int(x), input("input numbers (separated with space): ").split()))
    is_equal = True
    for i, number in enumerate(numbers):
        if i == 0:
            pass
        else:
            if numbers[i-1] != numbers[i]:
                is_equal = False
                break
    print(is_equal)
