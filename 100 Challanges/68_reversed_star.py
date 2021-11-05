if __name__ == "__main__":
    n = int(input("input number: "))
    k = (2 * n) - 2

    for i in range(n):
        for j in range(k):
            print("", end=" ")
        for j in range(i + 1):
            print("*", end=" ")
        print("")
        k = k - 2
