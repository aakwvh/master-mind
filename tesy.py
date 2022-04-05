import random

# deze functie maakt to split an integer into an array of digits, vorbeeld 1240 naar [1,2,4,0]
def array_digit(getal):
    return [int(i) for i in str(getal)]

# deze functie verandert list arrey naar int
def magic(numList):
    s = ''.join(map(str, numList))
    return int(s)


# stap 1, zoek een random nummer in de range van 1000 en 10000
codeInt = random.randrange(1000,10000) # dit zorgt voor dat er een random een nummer tussen 1000 en 10000 wordt gekozen.
code = array_digit(codeInt)
print(code)


# stap 2 maak een lijst met alle mogelijke combinatie/gok de lijst is gesorteerd.
# bij deze stap wordt alle mogelijke  combinatie in een list toegevoegd en gesorteerd van klein naar groot.
alleCombinatie = [] # maakt een lege list
for i in range(1000,10000):
    alleCombinatie.append(i) # er wordt geloop van 1000 tot 10000, alles loops wordt toegevoegd aan de list
sorted_alleCombinatie = sorted(alleCombinatie) # de lijst wordt gesorteerd van klein naar groot.

# stap 3 stel een vraag: doe een gok?
guessInt = random.choice(sorted_alleCombinatie)
guess = array_digit(guessInt)
print("dit is guess",guess)


# stap 4

def right_inwrongplace(guess, code):
    # Create a list of Boolean values representing correct guesses.
    # for exemple: if numbers = [1,2,3,4] and guess = [1,2,9,9], correct_places will be [True,True,False,False]
    correct_places = [True if v == code[i] else False for i, v in enumerate(guess)]
    print(correct_places)
    # create a list with only the correct guesses.
    g = [v for  i, v in enumerate(guess) if  correct_places[i]]
    print("correct guess",g)
    # create a list with the numbers which weren't guessed correctly.
    n = [v for  i, v in enumerate(code) if not correct_places[i]]
    print(n)
    #return the amount of guesses that are correct but in the wrong place. (the numbers that are in both lists)
    return g

print(right_inwrongplace(guess, code))




# Python program to print all
# the possible combinations

#
#
# # The Main function
# if __name__ == '__main__':
#     # List of colors
#     colors = ["RED", "GREEN", "YELLOW", "BLUE", "BLACK", "ORANGE"]
#
#     # Mapping of colors to numbers
#     colors_map = {1: "RED", 2: "GREEN", 3: "YELLOW", 4: "BLUE", 5: "BLACK", 6: "ORANGE"}
#
#     # Randomly selecting a passcode
#     random.shuffle(colors)
#     passcode = colors[:4]
#
#     # Number of chances for the player
#     chances = 8
#
#     # The passcode to be shown to the user
#     show_passcode = ['UNK', 'UNK', 'UNK', 'UNK']
#
#     # The codes guessed by the player each turn
#     guess_codes = [['-', '-', '-', '-'] for x in range(chances)]
#
#     # The clues provided to the player each turn
#     guess_flags = [['-', '-', '-', '-'] for x in range(chances)]
