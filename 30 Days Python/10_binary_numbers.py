# https://www.hackerrank.com/challenges/30-binary-numbers/problem

def consecutive(binary):
    count = 1
    max_num = 1
    for i, number in enumerate(binary):
        if i == 0:
            pass
        else:
            if binary[i] == binary[i-1]:
                count += 1
                max_num = count if count > max_num else max_num
            else:
                count = 1
    return max_num


if __name__ == "__main__":
    binary = bin(int(input()))[2:]
    print(binary)
    print(consecutive(binary))
