import string

if __name__ == "__main__":
    alphabet = string.ascii_lowercase
    text = input('input string: ')
    is_all_letter = True
    for char in alphabet:
        if char not in text:
            is_all_letter = False
            break
    print(is_all_letter)
