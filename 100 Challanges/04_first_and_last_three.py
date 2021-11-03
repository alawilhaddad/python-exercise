if __name__ == '__main__':
    text = input('input string: ')
    if len(text) < 6:
        print("")
    else:
        print(f'{text[:3]}{text[-3:]}')