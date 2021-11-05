if __name__ == "__main__":
    number = int(input("input number: "))
    answer = 1
    i = 1
    while i != number+1:
        answer *= i
        i += 1
    print(answer)