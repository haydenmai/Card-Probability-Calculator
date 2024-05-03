### Card Deck Generator and Probability Calculator
## Authors: Benley Hsiang & Gia hue (Hayden) Mai

# Make a card deck generator

import random
import math

# Description: Calculates the probability of rank/suit of the next card
def probabilityOf(typeDrawn, cardsDrawn, rankOrSuit, storeIndex):
    remain = 52 - cardsDrawn
    
    # Calculating remaining number of cards with the same suit
    if len(rankOrSuit) == 4:
        typeRemain = 13 - typeDrawn

    # Calculating remaining number of cards with the same number
    elif len(rankOrSuit) == 13:
        typeRemain = 4 - typeDrawn

    print("{:<8} {:>10.2f} %".format(rankOrSuit[storeIndex+1], float((typeRemain/remain)*100)))

# Description: Function for combinations
def combinations(n, r):
    answer = math.factorial(n) / (math.factorial(n - r) * math.factorial(r))
         
    return answer

# Description: Function for calculating the probablity of the next card drawn based on the numbers in hand
def nextCardProb(sameValue, drawn):

    # Finds the probability given that we know how many Numbers and total cards drawn
    # 
    prob = float(( combinations(3, sameValue) * (1/(52 - drawn)) ) / combinations(4, sameValue) ) 

    return prob

# For Value to String retrieval using dictionary for generation
suits = {1:'Spade', 2:'Club', 3:'Heart', 4:'Diamond'}

numbers = {1:'Ace', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:'Jack', 12:'Queen', 13: 'King'}

# Dictionaries for counting how many cards of a suit/number are drawn
# Accessing the type of suit using the dictionary `suits` above: 0 = Spades, 1 = Clubs, 2 = Hearts, 3 = Diamonds in the dictionary
suitsDrawn = {"Spade": 0, "Club": 0, "Heart": 0, "Diamond": 0}

# Accessing the type of number using the dictionary `numbers` above: 0 = Ace, ..., 12 = King in the dictionary
numbersDrawn = {'Ace': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'Jack': 0, 'Queen': 0, 'King': 0}

# Empty list to store a shuffled deck
deck = []

# Empty list to store the probability of the next card with 2 attributes
deckProb = []

# Deck Generator
while len(deck) < 52:
    card = numbers[random.randint(1,13)] + ' of ' + suits[random.randint(1,4)]

    if card not in deck:
        deck.append(card)

# Probability calculator
# Boolean to check if the user input is correct
validNumber = 0

while validNumber == 0:
    userDraw = input("\nEnter the initial number of cards to draw: ")

    try:
        userDraw = int(userDraw)
        if userDraw > 52 or userDraw < 1:
            print("Invalid input, please try again")
        else:
            validNumber = 1
    except ValueError:
        print("Invalid input, please try again")
    
print("Here are your drawn cards: \n")

# loop to print out cards
# This will draw from the deck first in first out
drawn = []

# remove from deck and add to hand drawn queue style
for i in range(userDraw):
    drawn.append(deck[0])
    deck.remove(drawn[i])  
    print(drawn[i]+"s")

    card = drawn[i]
    number, suit = card.split(" of ")
    # counting
    # suits
    if suit in suitsDrawn:
        suitsDrawn[suit] += 1

    # numbers
    if number in numbersDrawn:
        numbersDrawn[number] += 1

#Printing counted lists
print("\nNumber of Cards with the Following Rank:")
for i in range(13):
    print("{:<5} {:>5}".format(numbers[i + 1], numbersDrawn[numbers[i + 1]]))

print("\nNumber of Cards with the Following Suit:")
for i in range(4):
    print("{:<8} {:>8}".format(suits[i + 1], suitsDrawn[suits[i + 1]]))

#Printing calculations
print("\nHere are the probabilities of the next card being a:")

# Suits
for i in range(4):
    probabilityOf(suitsDrawn[suits[i + 1]], userDraw, suits, i)

# Numbers
print("")
for i in range(13):
    probabilityOf(numbersDrawn[numbers[i + 1]], userDraw, numbers, i)

# Calculating probabilities for the next card (both attributes: suit and number)
for i in range(len(deck)):
    for key in numbersDrawn:
        if key in deck[i]:        
            deckProb.append(nextCardProb(numbersDrawn[key], userDraw))

# Printing probabilities in deckProb
print("\nProbabilities of the next card:")

for i in range(len(deckProb)):
    print("{:<22} {:>10.2f} %".format(deck[i]+"s", (deckProb[i]*100)))

# END OF CODE