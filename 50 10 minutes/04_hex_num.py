def hex_output():
    dec_num = 0
    hex_num = input("Enter a hex number to convert: ")
    for power, digit in enumerate(reversed(hex_num)):
        dec_num += int(digit, 16) * (16 ** power)
    print(dec_num)


if __name__ == "__main__":
    hex_output()
