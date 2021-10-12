# https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem

if __name__ == '__main__':
    S = input()
    try:
        print(int(S))
    except ValueError:
        print("Bad String")