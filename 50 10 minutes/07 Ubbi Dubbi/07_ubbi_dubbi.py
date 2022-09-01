def ubbi_dubbi(string):
    vowels = ['a', 'i', 'u', 'e', 'o']
    string_list = []
    for char in string:
        if char in vowels:
            string_list.append(f"ub{char}")
        else:
            string_list.append(char)
    return ''.join(string_list)


if __name__ == "__main__":
    word = input("enter word: ")
    print(ubbi_dubbi(word))
