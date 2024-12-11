# Dependency imports
import random

"""
Create function
params::
player_choice: input() ->> Get user input 
computer_choice: 
"""
def get_choices():
    player_choice = input("Enter a choice(rock, paper, scissors: )")
    computer_opt = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer_opt)
    choices = {"player": player_choice, "computer": computer_choice}

    return choices

"""
Create function
check win 
if -> elif different test scenarios
return result
"""
def check_win(player, computer):
    print(f"You chose {player}, computer chose  {computer}")
    if player == computer:
        return "It's a tie"
    elif player == "rock" and computer == "scissors":
        # Winning scenarios
        return "You win! Yay!"
    elif player == "paper" and computer == "rock":
        return "You win! Yay!"
        # Losing scenarios
    elif player == "rock" and computer == "paper":
        return "Computer wins! Try again!"
    elif player == "paper" and computer == "scissors":
        return "Computer wins! Try again!"
    else:
        return "Error! Something went wrong"

choices = get_choices

result = check_win(choices["player"], choices["computer"])

print(result)


