# https://www.hackerrank.com/challenges/30-scope/problem?h_r=next-challenge&h_v=zen

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        for i, number1 in enumerate(self.__elements):
            for j, number2 in enumerate(self.__elements):
                diff = abs(number1 - number2)
                if self.maximumDifference < diff:
                    self.maximumDifference = diff


if __name__ == "__main__":
    _ = input()
    a = [int(e) for e in input().split(' ')]

    d = Difference(a)
    d.computeDifference()

    print(d.maximumDifference)
