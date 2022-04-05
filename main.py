from itertools import permutations
import random


# algoritm
# stap 1, zoek een random nummer in de range van 1000 en 10000
code_ = random.randrange(1000,10000) # dit zorgt voor dat er een random een nummer tussen 1000 en 10000 wordt gekozen.

code = map(int,str(code_))
print("dit is de code", code)

# stap 2 maak een lijst met alle mogelijke combinatie/gok de lijst is gesorteerd.
# bij deze stap wordt alle mogelijke  combinatie in een list toegevoegd en gesorteerd van klein naar groot.
alleCombinatie = [] # maakt een lege list
for i in range(1000,10000):
    alleCombinatie.append(i) # er wordt geloop van 1000 tot 10000, alles loops wordt toegevoegd aan de list
sorted_alleCombinatie = sorted(alleCombinatie) # de lijst wordt gesorteerd van klein naar groot.

# stap 3 stel een vraag: doe een gok?
guess = random.choice(sorted_alleCombinatie)
print("dit is guess",guess)


# stap 4

# stap 4 dit functie geeft een list met de correcte guess

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


# Get all combination of [A, 2, 3]
# of length 3




alle_combi = []


#
# combinatie = permutations(['rood','groen','paars','oranje'], 4)
# for i in combinatie:
#     print(i)
#     alle_combi.append(i)
#
# print(sorted(alle_combi))
#
# vraag = 'wat is de eerste combinatie?'
# vraag_input = input("voeg hier input?")


