if __name__ == "__main__":
    fahrenheit = int(input('input radius: ').strip(' '))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit} Fahrenheit = {celsius} Celsius")
