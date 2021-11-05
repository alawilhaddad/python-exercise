import random

if __name__ == "__main__":
    selection = ['Rock', 'Paper', 'Scissor']
    condition = None
    print("====== Welcome to the game ======")
    print("Please enter Rock, Paper, or Scissors below:")
    player = input().title()
    computer = random.choice(selection)
    if player == computer:
        condition = 'tie'
    elif player == "Rock" and computer == "Paper":
        condition = "lose"
    elif player == "Rock" and computer == "Scissors":
        condition = "win"
    elif player == "Paper" and computer == "Scissors":
        condition = "lose"
    elif player == "Paper" and computer == "Rock":
        condition = "win"
    elif player == "Scissors" and computer == "Paper":
        condition = "win"
    elif player == "Scissors" and computer == "Rock":
        condition = "lose"
    print(f"{condition.title()}! Your opponent choose '{computer}'")
