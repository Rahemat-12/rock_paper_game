import random


def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def get_user_choice():
    while True:
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'draw'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'paper' and computer_choice == 'rock') or \
            (user_choice == 'scissors' and computer_choice == 'paper'):
        return 'user'
    else:
        return 'computer'

def display_result(user_choice, computer_choice, winner):
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == 'draw':
        print("It's a draw!")
    elif winner == 'user':
        print("You win!")
    else:
        print("Computer wins!")


def play_game():
    user_score = 0
    computer_score = 0
    rounds = 1

    while True:
        print(f"\nRound {rounds}")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1

        display_result(user_choice, computer_choice, winner)

        print(f"Score -> You: {user_score} | Computer: {computer_score}")

        play_again = input("Do you want to play another round? (y/n): ").lower()
        if play_again != 'y':
            break
        rounds += 1

    print("Thanks for playing! Final Score -> You: {} | Computer: {}".format(user_score, computer_score))


if __name__ == "__main__":
    play_game()
