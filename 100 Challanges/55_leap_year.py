if __name__ == "__main__":
    year = int(input("input year: "))
    year_type = None
    if year % 4 != 0 or year % 400 == 0:
        year_type = "not a"
    else:
        year_type = "a"
    print(f'{year} is {year_type} leap year')