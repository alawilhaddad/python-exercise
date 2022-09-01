def hex_output(hex_num):
    dec_num = 0
    for power, digit in enumerate(reversed(hex_num)):
        if digit.isnumeric():
            dec_num += chr(ord(digit)) * (16 ** power)
        else:
            dec_num += (ord(digit)-87) * (16 ** power)
    print(dec_num)


if __name__ == "__main__":
    hex_output(input("Enter a hex number to convert: "))
