def fibonacci(n):
    temp_list = [0, 1]
    if n > 1:
        for i in range(n-1):
            temp_list.append(temp_list[i+1]+temp_list[i])
    return temp_list[n]


if __name__ == "__main__":
    n = int(input("input number: "))
    print(fibonacci(n))
