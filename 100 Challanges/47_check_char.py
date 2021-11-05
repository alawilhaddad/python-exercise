if __name__ == "__main__":
    vowel = ['a', 'i', 'u', 'e', 'o']
    char_type = None
    text = input("input text: ")
    for char in text:
        if char in vowel:
            char_type = 'vowel'
        elif char not in vowel and char.isalpha():
            char_type = 'consonant'
        else:
            char_type = 'not a letter'
        print(f'{char} is a {char_type}')
