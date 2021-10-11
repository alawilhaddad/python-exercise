# https://www.hackerrank.com/challenges/30-recursion/problem

def factorial(n):
    result = 1
    for number in range(1, n+1):
        result = result * number
    return result


if __name__ == '__main__':
    factorial(input())
