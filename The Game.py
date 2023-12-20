import random

def rock_paper_scissors_game():
    choices = ["Rock", "Paper", "Scissors"]

    player_wins = 0
    computer_wins = 0

    while True:
        player = input("Choose Rock, Paper, or Scissors (type 'quit' to exit): ").capitalize()

        if player == 'Quit':
            break

        if player not in choices:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")
            continue

        computer_choice = random.choice(choices)

        print(f"Player chose: {player}")
        print(f"Computer chose: {computer_choice}")

        if player == computer_choice:
            print("It's a tie!")
        elif (player == "Rock" and computer_choice == "Scissors") or \
             (player == "Scissors" and computer_choice == "Paper") or \
             (player == "Paper" and computer_choice == "Rock"):
            print("Player wins!")
            player_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1

        print(f"Player: {player_wins} wins")
        print(f"Computer: {computer_wins} wins")

    print("Game over!")

rock_paper_scissors_game()