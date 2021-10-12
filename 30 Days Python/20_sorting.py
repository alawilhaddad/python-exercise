# https://www.hackerrank.com/challenges/30-sorting/problem

if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    num_swap = 0
    temp = None
    for i in range(len(a)):
        swaps = 0
        for j in range(1, len(a)):
            if a[j - 1] > a[j]:
                temp = a[j]
                a[j] = a[j - 1]
                a[j - 1] = temp
                swaps += 1
        num_swap += swaps
        if swaps == 0:
            break
    print(f"Array is sorted in {num_swap} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
