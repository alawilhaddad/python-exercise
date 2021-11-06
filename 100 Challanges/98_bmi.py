if __name__ == "__main__":
    h, w = list(map(lambda x: int(x), input('input base height and weight: ').split()))
    bmi = w / (h/100)**2
    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi < 25:
        print("Normal")
    elif 25 <= bmi < 30:
        print("Overweight")
    elif 30 < bmi:
        print("Obesity")
