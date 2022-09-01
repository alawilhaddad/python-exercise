def string_list():
    my_list = []
    answer = []
    while True:
        temp = input("input list: ")
        temp_list = temp.split(" ")
        if temp:
            my_list.append(temp_list)
        else:
            break
    for i, a in enumerate(my_list):
        answer.append([])
        for j, b in enumerate(a):
            answer[i].append(my_list[j][i])

    print(my_list)
    print(answer)


if __name__ == "__main__":
    string_list()
