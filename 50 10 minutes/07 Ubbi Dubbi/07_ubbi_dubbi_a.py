def ubbi_dubbi(string):
    vowels = ['a', 'i', 'u', 'e', 'o']
    string_list = []
    my_dict = {}
    for i, char in enumerate(string):
        my_dict[i] = char.isupper()
    for char in string:
        if char in vowels:
            string_list.append(f"ub{char}")
        else:
            string_list.append(char)
    answer = list(''.join(string_list))
    for i, char in enumerate(string):
        if my_dict.get(i):
            answer[i] = answer[i].upper()
        else:
            answer[i] = answer[i].lower()
    print(''.join(answer))


if __name__ == "__main__":
    word = input("enter word: ")
    ubbi_dubbi(word)
