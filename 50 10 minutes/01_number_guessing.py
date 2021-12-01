import random


def guessing_game():
    answer = random.randint(1, 101)
    chances = 3
    condition = False
    while chances > 0:
        guess = int(input("Input your guess: "))
        if guess < answer:
            print(f"{guess} is too small")
        elif guess > answer:
            print(f"{guess} is too big")
        elif guess == answer:
            print(f"{guess} is just right")
            condition = True
            break
        chances -= 1
    print("You Win!") if condition else print("You Lose!")


if __name__ == "__main__":
    guessing_game()
