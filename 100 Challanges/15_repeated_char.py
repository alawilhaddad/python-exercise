if __name__ == "__main__":
    text = input('input string: ').replace(' ', '')
    char_in_text = sorted(list(set(text)))
    repeated_char = []
    for i in char_in_text:
        count = 0
        for j in text:
            if i == j:
                count += 1
        if count > 1:
            repeated_char.append(i)
    if not repeated_char:
        repeated_char = 'None'
        length = 0
    else:
        length = len(repeated_char)
        repeated_char = ' '.join(repeated_char)
    print(length)
    print(repeated_char)
