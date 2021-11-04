if __name__ == '__main__':
    list_a = input('input first list (separated by space): ').split(' ')
    list_b = input('input second list (separated by space): ').split(' ')
    diff = list_a
    for char2 in list_b:
        for char1 in diff:
            if char2 == char1:
                for i in range(diff.count(char2)):
                    diff.remove(char2)
    print(diff)