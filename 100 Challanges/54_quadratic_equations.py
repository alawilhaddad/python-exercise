import math

if __name__ == "__main__":
    numbers = []
    while len(numbers) != 3:
        numbers = list(map(lambda x: int(x), input("input numbers (separated with space): ").split()))
    a, b, c = numbers
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        print("Complex Roots")
    elif discriminant == 0:
        x1 = (-b + math.sqrt(discriminant))/(2 * a)
        print(x1)
    else:
        x1 = (-b - math.sqrt(discriminant))/(2 * a)
        x2 = (-b + math.sqrt(discriminant))/(2 * a)
        print(f"{x1} {x2}")
