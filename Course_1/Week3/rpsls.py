"""
Week 4 practice project template for Python Programming Essentials
Rock-paper-scissors-lizard-Spock
"""

import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
    
def name_to_number(name):
    """
    Given string name, return integer 0, 1, 2, 3, or 4 
    corresponding to numbering in video
    """
  
    # convert name to number using if/elif/else
    # don't forget to return the result!
    result = 0;
    if(name == "rock"):
        result = 0
    elif(name == "Spock"):
        result = 1
    elif(name == "paper"):
        result = 2
    elif(name == "lizard"):
        result = 3
    else:
        result = 4
        
    return result
    
def number_to_name(number):
    """
    Given integer number (0, 1, 2, 3, or 4)
    corresponding name from video
    """
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    result = ""
    if(number == 0):
        result = "rock"
    elif(number == 1):
        result = "Spock"
    elif(number == 2):
        result = "paper"
    elif(number == 3):
        result = "lizard"
    else:
        result = "scissors"
        
    return result

def rpsls(player_choice):
    """
    Given string player_choice, play a game of RPSLS 
    and print results to console
    """
    
    # print a blank line to separate consecutive games
    print("")
    
    # print out the message for the player's choice
    print("Player plays", player_choice)

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out message for computer's choice
    print("Computer plays", comp_choice)

    # compute difference of player_number and comp_number modulo five
    diff = (player_number - comp_number) % 5

    # use if/elif/else to determine winner and print winner message
    if(diff >= 3):
        print("Computer wins!")
    elif(diff > 0):
        print("Player wins!")
    else:
        print("It's a draw")
     
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

