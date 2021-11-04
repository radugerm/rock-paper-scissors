import random

def game():
    count = 5
    choice = ["rock", "paper", "scissors"]

    your_score = 0
    computer_score = 0
    while count >= 0:
        computer = random.choice(choice)
        player = input("Please choose r for rock, p for paper ,s for scissors:").lower()
        count -= 1
        if (player == "r" and computer == "scissors") or (player == "s" and computer == "paper") or (
                player == "p" and computer == "rock"):
            your_score += 1
            print(f"computer chooses {computer} and you win")
        elif (computer == "rock" and player == "s") or (computer == "scissors" and player == "p") or (
                computer == "paper" and player == "r"):
            print(f"You lost ,computer chooses {computer}")
            computer_score += 1
        else:
            print(f"It's a draw ,computer chooses {computer}")

        print(f"Score = You {your_score}:{computer_score} Computer")
    if your_score > computer_score:
        print("You won the game!!!!")
    elif computer_score > your_score:
        print("You lost the game :(")
    else:
        print("It's a draw")
game()
