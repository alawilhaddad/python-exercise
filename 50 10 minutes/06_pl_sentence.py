def pig_latin(string):
    vowels = ['a', 'i', 'u', 'e', 'o']
    if string[0] in vowels:
        return f"{string}way"
    else:
        return f"{string[1:]}{string[0]}ay"


def pl_sentence(words):
    for word in words:
        print(pig_latin(word), end=" ")


if __name__ == "__main__":
    sentence = input("enter sentence: ").split()
    pl_sentence(sentence)
