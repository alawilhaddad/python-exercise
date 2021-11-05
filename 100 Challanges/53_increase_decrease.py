if __name__ == "__main__":
    numbers = list(map(lambda x: int(x), input("input numbers (separated with space): ").split()))
    reference = numbers
    if numbers == sorted(reference):
        print("increasing order")
    elif numbers == sorted(reference, reverse=True):
        print("decreasing order")
    else:
        print("None")
