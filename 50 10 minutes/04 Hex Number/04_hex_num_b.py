def name_triangle(name):
    for i, char in enumerate(name):
        print(name[:i+1])


if __name__ == "__main__":
    name_triangle(input("Enter Name: "))
