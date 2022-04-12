import random

# deze functie maakt to split an integer into an array of digits, vorbeeld 1240 naar [1,2,4,0]
def array_digit(getal):
    return [int(i) for i in str(getal)]

# deze functie verandert list arrey naar int.
def magic(numList):
    s = ''.join(map(str, numList))
    return int(s)


alleCombinatie = [] # maakt een lege list
for i in range(1000,10000):
    alleCombinatie.append(array_digit(i)) # er wordt geloop van 1000 tot 10000, alles loops wordt toegevoegd aan de list
possible_code = sorted(alleCombinatie) # de lijst wordt gesorteerd van klein naar groot.

code_ = random.randrange(1000,10000) # dit zorgt voor dat er een random een nummer tussen 1000 en 10000 wordt gekozen.
code = array_digit(code_)   # dit is de code voor het spel mastermind


def reduce(possibleCodes,code,score):
  result = []
  for possibleCode in possibleCodes:
    # alleen codes die de gegeven score opleveren
    # kunnen het juiste antwoord zijn
     if score == evaluate(code,possibleCode):
        result.append(possibleCode)
  return result

def evaluate(guess,secret):
   score = [0,0]
   used = []
   # The black pins
   for position in range(len(guess)):
        if guess[position] == secret[position]:
            score[0] += 1
            used.append(position)
   # the white pins
   secretCopy = secret[::]
   for position in used:
       secretCopy.remove(secret[position])
   for i in range(len(guess)):
       if i not in used:
           if guess[i] in secretCopy:
               score[1] += 1
               secretCopy.remove(guess[i])
   return score



# stap 1
possible_code = [] # maakt een lege list
for i in range(1000,10000):
    possible_code.append(array_digit(i)) # er wordt geloop van 1000 tot 10000, alles loops wordt toegevoegd aan de list
possible_code = sorted(alleCombinatie) # de lijst wordt gesorteerd van klein naar groot.

# stap 2
code_ = random.randrange(1000,10000) # dit zorgt voor dat er een random een nummer tussen 1000 en 10000 wordt gekozen.
code = array_digit(code_)
print("dit is de code", code)



def simpel_algoritme( possible_codes ,answer):

    result = []
    guess = possible_codes[0]
    if evaluate(guess, answer) == [4, 0]:
        print(f"answer is {guess}")
        return guess

    for possibleCode in possible_codes:
        # alleen codes die de gegeven score opleveren
        # kunnen het juiste antwoord zijn
        if evaluate(guess, answer) == evaluate(guess, possibleCode):
            result.append(possibleCode)
    return simpel_algoritme(result, answer)


print(simpel_algoritme(possible_code, code))




#
#     # stap 2
#     secret = [8, 3, 5, 7]
#
#     # stap 3
#     guess = [5, 6, 3, 7]
#     e = []
#     vo = []
#
#     while e == [4, 0]:
#         e.append(evaluate(guess, secret))
#         re = reduce(sorted_alleCombinatie, guess, e)
#         vo.append(re)
#
#     return "dit is", vo
#
# print(simpel_algoritme())
#
#
# possible = []

# correct = []
#
# numbers_to_find = '235'
#
# lst = [str(i) for i in range(1000,10000)]
#
# for i in lst:
#     if numbers_to_find in i:
#         print(i)
#         correct.append(i)
#
# print(correct)
#
# #
#
#
# # deze functie maakt to split an integer into an array of digits, vorbeeld 1240 naar [1,2,4,0]
# def array_digit(getal):
#     return [int(i) for i in str(getal)]
#
# # deze functie verandert list arrey naar int.
# def magic(numList):
#     s = ''.join(map(str, numList))
#     return int(s)


# heights = [144, 180, 165, 120, 199]
# tall = [h for h in heights if h in [1]]
# print(tall)
#
#
# correct = 235
#
# # stap 2 maak een lijst met alle mogelijke combinatie/gok de lijst is gesorteerd.
# # bij deze stap wordt alle mogelijke  combinatie in een list toegevoegd en gesorteerd van klein naar groot.
# alleCombinatie = [] # maakt een lege list
# for i in range(1000,10000):
#     alleCombinatie.append(i) # er wordt geloop van 1000 tot 10000, alles loops wordt toegevoegd aan de list
# sorted_alleCombinatie = sorted(alleCombinatie) # de lijst wordt gesorteerd van klein naar groot.
#
# for i in sorted_alleCombinatie:
#     if correct in i:
#         print(i)
#
#
#
#



# def array_digit(getal):
#     return [int(i) for i in str(getal)]
#
# # stap 2 maak een lijst met alle mogelijke combinatie/gok de lijst is gesorteerd.
# # bij deze stap wordt alle mogelijke  combinatie in een list toegevoegd en gesorteerd van klein naar groot.
#
#
#
# def masterMind():
#     # stap 1, zoek een random nummer in de range van 1000 en 10000
#     code = random.randrange(1000,10000)  # dit zorgt voor dat er een random een nummer tussen 1000 en 10000 wordt gekozen.
#
#
#     # stap 2
#     alleCombinatie = []  # maakt een lege list
#     for i in range(1000, 10000):
#         alleCombinatie.append(i)  # er wordt geloop van 1000 tot 10000, alles loops wordt toegevoegd aan de list
#     sorted_alleCombinatie = sorted(alleCombinatie)  # de lijst wordt gesorteerd van klein naar groot.
#     print("sorted allecombi", sorted_alleCombinatie)
#
#     # stap 3 stel een vraag: doe een gok?
#     guess = random.choice(sorted_alleCombinatie)
#     print("dit is guess", guess)
#
#     if guess == code:
#         print("goed gedaan, je heb in 1 keer geraden!!!!")
#     else:
#         # ctr variable initialized. It will keep count of
#         # the number of tries the Player takes to guess the number.
#         ctr = 0
#
#         # while loop repeats as long as the Player
#         # fails to guess the number correctly.
#         while (guess != code):
#             # variable increments every time the loop
#             # is executed, giving an idea of how many
#             # guesses were made.
#             ctr += 1
#
#             count = 0
#
#             guess = str(guess)
#             print("str guess :", guess)
#             code = str(code)
#             print("code str:", code)
#
#             correct =[]
#             for i in range(0,4):
#                 # checking for equality of digits
#                 if (guess[i] == code[i]):
#                     # number of digits guessed correctly increments
#                     count += 1
#                     # hence, the digit is stored in correct[].
#                     correct.append(guess[i])
#                 else:
#                     continue
#                 # when not all the digits are guessed correctly.
#             if (count < 4) and (count != 0):
#                 print("Not quite the number. But you did get ", count, " digit(s) correct!")
#                 print("Also these numbers in your input were correct.")
#
#                 for k in correct:
#                     print(k, end=' ')
#
#                 print('\n')
#                 print('\n')
#                 n = int(input("Enter your next choice of numbers: "))
#
#                 # when none of the digits are guessed correctly.
#             elif (count == 0):
#                 print("None of the numbers in your input match.")
#                 n = int(input("Enter your next choice of numbers: "))
#
#
#
#
# print(masterMind())
#
#
#
# def right_inwrongplace(guess, code):
#     if guess == code:
#         print("goed gedaan, je heb in 1 keer geraden!!!!")
#     else:
#         # ctr variable initialized. It will keep count of
#         # the number of tries the Player takes to guess the number.
#         ctr = 0
#
#         # while loop repeats as long as the Player
#         # fails to guess the number correctly.
#         while (guess != code):
#             # variable increments every time the loop
#             # is executed, giving an idea of how many
#             # guesses were made.
#             ctr += 1
#
#             count = 0
#
#             correct =[]
#             for i in range(0,4):
#                 # checking for equality of digits
#                 if (guess[i] == code[i]):
#                     # number of digits guessed correctly increments
#                     count += 1
#                     # hence, the digit is stored in correct[].
#                     correct.append(guess[i])
#                 else:
#                     continue
#                 # when not all the digits are guessed correctly.
#             if (count < 4) and (count != 0):
#                 print("Not quite the number. But you did get ", count, " digit(s) correct!")
#                 print("Also these numbers in your input were correct.")
#
#                 for k in correct:
#                     print(k, end=' ')
#
#                 print('\n')
#                 print('\n')
#                 n = int(input("Enter your next choice of numbers: "))
#
#                 # when none of the digits are guessed correctly.
#             elif (count == 0):
#                 print("None of the numbers in your input match.")
#                 n = int(input("Enter your next choice of numbers: "))
#
#     # Create a list of Boolean values representing correct guesses.
#     # for exemple: if numbers = [1,2,3,4] and guess = [1,2,9,9], correct_places will be [True,True,False,False]
#     correct_places = [True if v == code[i] else False for i, v in enumerate(guess)]
#     print(correct_places)
#     # create a list with only the correct guesses.
#     g = [v for  i, v in enumerate(guess) if  correct_places[i]]
#     print("incorrect guess",g)
#     # create a list with the numbers which weren't guessed correctly.
#     n = [v for  i, v in enumerate(code) if  correct_places[i]]
#     print(n)
#     #return the amount of guesses that are correct but in the wrong place. (the numbers that are in both lists)
#     return len([i for i in g if i in n])
#
# print(right_inwrongplace(guess, code))
#
