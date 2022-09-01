def pig_latin(string):
    vowels = ['a', 'i', 'u', 'e', 'o']
    punctuation = []
    for i, char in enumerate(string):
        if char.isalpha():
            pass
        else:
            string.pop(i)
            punctuation.append(char)
    string = "".join(string)
    punctuation = "".join(punctuation)
    if string[0].lower() in vowels and string[0].isupper():
        return f"{string}WAY{punctuation}"
    elif string[0] in vowels:
        return f"{string}way{punctuation}"
    elif string[0].isupper():
        return f"{string[1:]}{string[0]}AY{punctuation}"
    else:
        return f"{string[1:]}{string[0]}ay{punctuation}"


if __name__ == "__main__":
    word = list(input("enter word: "))
    print(pig_latin(word))
