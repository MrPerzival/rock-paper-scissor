import random

def get_user_choice():
    user_choice = input("Enter your choice (Rock/Paper/Scissors): ")
    user_choice = user_choice.lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        user_choice = input("Invalid choice. Please enter Rock, Paper, or Scissors: ")
        user_choice = user_choice.lower()
    return user_choice

def get_computer_choice():
    computer_choice = random.choice(["rock", "paper", "scissors"])
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Let's play Rock, Paper, Scissors!")
    user_wins = 0
    computer_wins = 0
    for _ in range(3):
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print("Your choice:", user_choice)
        print("Computer's choice:", computer_choice)
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if "win" in result:
            user_wins += 1
        elif "Computer" in result:
            computer_wins += 1
    
    print("Final Score:")
    print("You:", user_wins)
    print("Computer:", computer_wins)

play_game()
