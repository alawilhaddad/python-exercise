# https://www.hackerrank.com/challenges/30-review-loop/problem

if __name__ == "__main__":
    for x in range(int(input())):
        s = input()
        print(f'{s[::2]} {s[1::2]}')


