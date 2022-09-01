def first_last(sequence):
    return [sequence[0], sequence[-1]]


if __name__ == "__main__":
    my_list = input("Enter number list: ").split(' ')
    print(first_last(my_list))
