import random


def run():
    my_dict = {"i": 1,
               "you": 2,
               "we": 3,
               "they": 4,
               "he": 5,
               "she": 6,
               "it": 7}

    answer = random.choice(list(my_dict.keys()))
    index = my_dict.get(answer)
    chances = 3
    condition = False

    while chances > 0:
        guess = input("\nInput your guess: ").lower()
        try:
            if my_dict.get(guess) > index:
                print(f"Correct answer is earlier")
            elif my_dict.get(guess) < index:
                print(f"Correct answer is later")
            elif my_dict.get(guess) == index:
                print(f"Right!")
                condition = True
                break
        except TypeError:
            print("invalid")
        chances -= 1

    print("\nYou Win!") if condition else print("\nYou Lose!")


if __name__ == "__main__":
    run()
