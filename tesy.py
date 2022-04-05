import random

# The Main function
if __name__ == '__main__':
    # List of colors
    colors = ["RED", "GREEN", "YELLOW", "BLUE", "BLACK", "ORANGE"]

    # Mapping of colors to numbers
    colors_map = {1: "RED", 2: "GREEN", 3: "YELLOW", 4: "BLUE", 5: "BLACK", 6: "ORANGE"}

    # Randomly selecting a passcode
    random.shuffle(colors)
    passcode = colors[:4]

    # Number of chances for the player
    chances = 8

    # The passcode to be shown to the user
    show_passcode = ['UNK', 'UNK', 'UNK', 'UNK']

    # The codes guessed by the player each turn
    guess_codes = [['-', '-', '-', '-'] for x in range(chances)]

    # The clues provided to the player each turn
    guess_flags = [['-', '-', '-', '-'] for x in range(chances)]
