if __name__ == "__main__":
    number = list(range(1,int(input("input number: "))+1))
    answer = 1
    for i in number:
        answer *= i
    print(answer)
