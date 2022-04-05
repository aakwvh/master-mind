from itertools import permutations
import random


# algoritm
# stap 1, zoek een random nummer in de range van 1000 en 10000
code = random.randrange(1000,10000) # dit zorgt voor dat er een random een nummer tussen 1000 en 10000 wordt gekozen.
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


