import random


def guessing_game(s=0):
    answer = random.randint(1, 101)
    while s != answer:
        guess = int(input("Input your guess: "))
        if guess < answer:
            print(f"{guess} is too small")
        elif guess > answer:
            print(f"{guess} is too big")
        elif guess == answer:
            print(f"{guess} is just right")
            break


if __name__ == "__main__":
    guessing_game()
