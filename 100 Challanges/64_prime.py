if __name__ == "__main__":
    number = int(input("input number: "))
    is_prime = True
    if number < 2:
        is_prime = False
    for i in range(number):
        if i < 2:
            pass
        else:
            if number % i == 0:
                is_prime = False

    if is_prime:
        print("Prime")
    else:
        print("Not Prime")
