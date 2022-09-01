def pig_latin(string):
    vowels = ['a', 'i', 'u', 'e', 'o']
    punctuation = []
    for i, char in enumerate(string):
        if char.isalpha():
            pass
        else:
            string.pop(i)
            punctuation.append(char)

    temp = string
    string = "".join(string)
    punctuation = "".join(punctuation)
    counter = 0
    for char in temp:
        if char in vowels:
            for i in range(temp.count(char)):
                temp.remove(char)
            counter += 1

    if counter >= 2:
        return f"{string}way{punctuation}"
    else:
        return f"{string[1:]}{string[0]}ay{punctuation}"


if __name__ == "__main__":
    word = list(input("enter word: ").lower())
    print(pig_latin(word))
