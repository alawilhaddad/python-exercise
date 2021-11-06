if __name__ == "__main__":
    text = input("enter string: ")
    if text[:2] and text[-4:]:
        print("match")
    else:
        print("no match")
