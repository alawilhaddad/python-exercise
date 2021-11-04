if __name__ == "__main__":
    text = input('input string: ')
    suf = input('suffix to check: ')
    suf_check = True if text[len(text)-len(suf)::] == suf else False
    print(suf_check)
