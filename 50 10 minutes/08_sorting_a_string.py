def str_sort(string):
    return ''.join(sorted(string))


if __name__ == "__main__":
    word = input("enter word: ")
    print(str_sort(word))
