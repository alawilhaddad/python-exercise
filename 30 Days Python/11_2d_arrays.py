#https://www.hackerrank.com/challenges/30-2d-arrays/problem

def max_hourglass(arr):
    max = 0
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if i == j == 0:
                max = sum
            max = sum if max < sum else max
    return max

if __name__ == "__main__":
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    print(max_hourglass(arr))
