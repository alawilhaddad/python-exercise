def obj(_list):
    my_list = []
    for x in _list:
        try:
            my_list.append(int(float(x)))
        except ValueError:
            pass
    print(sum(my_list))


if __name__ == "__main__":
    obj(input("input list: ").split(" "))
