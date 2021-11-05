if __name__ == "__main__":
    print('=== Welcome to your Interactive Python Calculator ===')
    value1 = int(input("Please enter the first value: "))
    value2 = int(input("Please enter the second value: "))
    print('''
Great! Now enter the operation.
These are the available options:
1 - Addition
2 - Subtraction
3 - Multiplication
4 - Division
5 - Integer Division
6 - Modulo
''')
    try:
        selection = int(input("--> Enter the corresponding integer: "))
        answer = 0
        if selection == 1:
            answer = value1 + value2
            operator = "+"
        elif selection == 2:
            answer = value1 - value2
            operator = "-"
        elif selection == 3:
            answer = value1 * value2
            operator = "*"
        elif selection == 4:
            answer = value1 / value2
            operator = "/"
        elif selection == 5:
            answer = value1 // value2
            operator = "//"
        elif selection == 6:
            answer = value1 % value2
            operator = "%"
        print(f'The result of {value1} {operator} {value2} is: {answer}')
    except NameError:
        print("Please choose a valid operation")
