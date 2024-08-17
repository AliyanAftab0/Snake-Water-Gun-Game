import random

# Constants for the game
SNAKE = 1
WATER = -1
GUN = 0

# Mapping user input to game choices
youDict = {"s": SNAKE, "w": WATER, "g": GUN}
reversedDict = {SNAKE: "Snake", WATER: "Water", GUN: "Gun"}

# Function to get computer's choice
def get_computer_choice():
    return random.choice([SNAKE, WATER, GUN])

# Main game loop
while True:
    # Computer's choice
    computer = get_computer_choice()

    # User input
    youstr = input("Enter your choice (s for snake, w for water, g for gun) or 'q' to quit: ")
    if youstr == 'q':
        print("Thanks for playing!")
        break

    you = youDict.get(youstr)

    if you is None:
        print("Invalid choice!")
    else:
        print(f"You Choose {reversedDict[you]}\nComputer Choose: {reversedDict[computer]}")

        # Determine the winner using a dictionary for outcomes
        outcomes = {
            (SNAKE, WATER): "You Win!",
            (WATER, GUN): "You Win!",
            (GUN, SNAKE): "You Win!",
            (WATER, SNAKE): "You Lose!",
            (GUN, WATER): "You Lose!",
            (SNAKE, GUN): "You Lose!",
        }

        if computer == you:
            print("It's a tie!")
        else:
            print(outcomes.get((you, computer), "Invalid outcome!"))
