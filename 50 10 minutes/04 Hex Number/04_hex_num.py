def hex_output(hex_num):
    dec_num = 0
    for power, digit in enumerate(reversed(hex_num)):
        dec_num += int(digit, 16) * (16 ** power)
    print(dec_num)


if __name__ == "__main__":
    hex_output(input("Enter a hex number to convert: "))
