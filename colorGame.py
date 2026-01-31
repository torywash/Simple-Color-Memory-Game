""" The kids game color memory, where the player has to remember and repeat a sequence of colors. """
# import modules
import random
import time
import os

# color list
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
color_codes = {'red': '\033[41m', 'blue': '\033[44m', 'green': '\033[42m', 'yellow': '\033[48;5;184m', 'orange': '\033[48;2;255;165;0m', 'purple': '\033[45m', 'reset': '\033[0m'}

# functions
    # makes a list of random combination of colors
def generateColors(numColors):
    generatedColors = []
    for i in range(numColors):
        generatedColors.append(random.choice(colors))
        i += 1
    return generatedColors

    # checks if the user input matches the generated colors
def checkColors(generatedColors, userColors, turn, totalTurns):
    for i in range(turn+1):
        if generatedColors[i].lower() != userColors[i].lower():
            print("You Lose! The correct sequence was:", generatedColors)
            showAllColors(generatedColors, totalTurns)
            playAgain()
            return False
    print("Correct!")
    time.sleep(0.75)
    clear_terminal()

    # get user input
def getUserColors(gameColors, turn, totalTurns):
    print(f"turn:", turn+1)
    userInput = input("Enter the colors in order, separated by spaces: ")
    userColors = userInput.split()
    return checkColors(gameColors, userColors, turn, totalTurns)

# set turtle window background color according to color
def displayColors(gameColors, turn, difficulty):
    # print colored block
    for i in range(turn):
        print(f"{color_codes[gameColors[i]]}          \n{color_codes[gameColors[i]]}          \n{color_codes[gameColors[i]]}          \n{color_codes[gameColors[i]]}          \n{color_codes['reset']}\n")
        time.sleep(difficulty)
        clear_terminal()
        i += 1

# show all colors
def showAllColors(gameColors, turns):
    for i in range(turns):
        print(f"{color_codes[gameColors[i]]}          {color_codes['reset']}")
        i += 1

# set game difficulty
def getDifficulty():
    difficulty = input("Choose difficulty (easy, medium, hard, insanse): ").lower()
    if difficulty == 'easy':
        return 0.5
    elif difficulty == 'medium':
        return 0.25
    elif difficulty == 'hard':
        return 0.15
    elif difficulty == 'insane':
        return 0.05
    else:
        print("Invalid difficulty. please choose again")
        getDifficulty()

# pulled a terminal clear from the internet
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def playAgain():
    again = input("Do you want to play again? (y/n): ").lower()
    if again == 'y':
        main()
    else:
        print("Thanks for playing!")

# main function
def main():
    difficulty = getDifficulty()
    turns = int(input("Enter number of colors to remember: "))
    clear_terminal()
    gameColors = generateColors(turns)
    start = time.time()
    for i in range(turns):
        displayColors(gameColors, i+1, difficulty)
        flag = getUserColors(gameColors, i, turns)
        if flag == False:
            return
    end = time.time()
    print("You Win!")
    print(f"Time taken: {end - start:.2f} seconds")
    playAgain()

# run game
main()