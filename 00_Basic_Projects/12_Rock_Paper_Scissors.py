import random
options = ("rock", "paper", "scissors")

player = None
computer = random.choice(options)
running = True
while running:
    while player not in options:

        player = input("Enter your Choice (rock, paper, scissors): ")
        print(f"Player: {player}")
        print(f"Computer: {computer}")

        if player == computer:
            print("It's a tie.")
        elif player == "rock" and computer == "scissors":
            print("You Win")
        elif player == "paper" and computer == "rock":
            print("You Win")
        elif player == "scissors" and computer == "paper":
            print("You Win")
        else:
            print("You Lose !")
            break
running = False

