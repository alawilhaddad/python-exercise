import string

if __name__ == "__main__":
    dictionary = {}
    text = input('input text: ')
    for char in text:
        x = char.lower()
        if x not in string.ascii_lowercase:
            pass
        else:
            if x not in dictionary.keys():
                dictionary[char.lower()] = 1
            else:
                dictionary[char.lower()] += 1
    print(dictionary)
