def counter(string):
    vowel = ('a', 'i', 'u', 'e', 'o')
    count = 0
    for char in string:
        if char in vowel:
            count += 1
    return count


if __name__ == "__main__":
    text = input("input text: ")
    print(counter(text))
