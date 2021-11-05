if __name__ == "__main__":
    n = int(input("input number: "))
    if n % 2 == 1:
        middle_rows = (n + 2) // 2

        for i in range(middle_rows):
            print(" " * (middle_rows - i), "*" * (i * 2 + 1))

        for i in range(middle_rows - 2, -1, -1):
            print(" " * (middle_rows - i), "*" * (i * 2 + 1))

    else:
        print("enter odd number")