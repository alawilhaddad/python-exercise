if __name__ == "__main__":
    text = input('input string: ')
    pref = input('prefix to check: ')
    pref_check = True if text[:len(pref):] == pref else False
    print(pref_check)
