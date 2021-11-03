if __name__ == '__main__':
    text = input('input string: ')
    i = int(input('index: '))

    if text == "":
        print('Empty String')
    else:
        try: print(text[i])
        except IndexError:
            print("i is out of range")

