def float_b_a(decimal, before, after):
    temp = str(decimal).split(".")
    answer = float(f'{temp[0][before - 1:]}.{temp[1][:after]}')
    return answer


if __name__ == "__main__":
    print(float_b_a(
        float(input("Enter decimal number: ")),
        int(input("Enter first number: ")),
        int(input("Enter second number: "))
    ))
