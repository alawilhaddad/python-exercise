def pig_latin(string):
    vowels = ['a', 'i', 'u', 'e', 'o']
    if string[0] in vowels:
        return f"{string}way"
    else:
        return f"{string[1:]}{string[0]}ay"


if __name__ == "__main__":
    word = input("enter word: ")
    print(pig_latin(word))
