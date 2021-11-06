import calendar

if __name__ == "__main__":
    year, month = list(map(lambda x: int(x), input('input base height and weight: ').split()))
    print(calendar.month(year, month))
