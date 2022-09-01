def pig_latin(string):
    vowels = ['a', 'i', 'u', 'e', 'o']
    my_dict = {}
    for i, char in enumerate(string):
        my_dict[i] = char.isupper()
    if string[0].lower() in vowels:
        answer = f"{string}way"
    else:
        answer = f"{string[1:]}{string[0]}ay"
    answer = list(answer)
    for i, char in enumerate(string):
        if my_dict.get(i):
            answer[i] = answer[i].upper()
        else:
            answer[i] = answer[i].lower()
    print(''.join(answer))


if __name__ == "__main__":
    word = input("enter word: ")
    pig_latin(word)
