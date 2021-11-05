if __name__ == "__main__":
    seasons = {"1": "Spring",
              "2": "Summer",
              "3": "Fall",
              "4": "Winter"}
    number = input("input number: ")
    season = seasons.get(number)
    if season is not None:
        print(season)
    else:
        print("Enter a valid number")
