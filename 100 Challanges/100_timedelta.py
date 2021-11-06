import datetime

if __name__ == "__main__":
    date_1 = list(map(lambda x: int(x), input('input first date (YYYY MM DD): ').split()))
    date_2 = list(map(lambda x: int(x), input('input second date (YYYY MM DD): ').split()))
    date_1_obj = datetime.date(date_1[0], date_1[1], date_1[2])
    date_2_obj = datetime.date(date_2[0], date_2[1], date_2[2])
    if date_2_obj > date_1_obj:
        print("Please enter valid dates.")
    else:
        difference = (date_2_obj - date_1_obj).days

        if difference == 0:
            print("These dates are equal.")
        elif difference == 1:
            print(f"There is 1 day between these dates.")
        else:
            print(f"There are {abs(difference)} days between these dates.")
