import string

if __name__ == "__main__":
    n = int(input("input number: "))
    for i in range(n):
        print(f'{string.ascii_uppercase[i]} ' * (i+1))
