if __name__ == "__main__":
    months = {"January": 31,
              "February": 28,
              "March": 31,
              "April": 30,
              "May": 31,
              "June": 30,
              "July": 31,
              "August": 31,
              "September": 30,
              "October": 31,
              "November": 30,
              "December": 31}
    entry = input("input month: ")
    month = months.get(entry.title())
    if month is not None:
        print(month)
    else:
        print("Enter a valid month")
