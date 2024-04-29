### Card Deck Generator and Probability Calculator
## Authors: Benley Hsiang & Gia hue (Hayden) Mai

# Make a card deck generator

import random
import math
    
def probabilityOf(typeDrawn, cardsDrawn, typeWant, storeIndex):
    remain = 52 - cardsDrawn
    
    # Calculating remaining number of cards with the same suit
    if len(typeWant) == 4:
        typeRemain = 13 - typeDrawn

    # Calculating remaining number of cards with the same number
    elif len(typeWant) == 13:
        typeRemain = 4 - typeDrawn

    print("{}: {}%".format(typeWant[storeIndex+1], float((typeRemain/remain)*100)))

def combinations(n, r):
    answer = math.factorial(n) / (math.factorial(n - r) * math.factorial(r))
         
    return answer

def nextCardProb(sameValue, drawn):
    prob = float(( combinations(3, sameValue) * (1/(52 - drawn)) ) / combinations(4, sameValue) ) 

    return prob

# For Value to String retrieval using dictionary for generation
suits = {1:'Spade', 2:'Club', 3:'Heart', 4:'Diamond'}

numbers = {1:'Ace', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:'Jack', 12:'Queen', 13: 'King'}

# for counting
# suits 0 = Spades, 1 = Clubs, 2 = Hearts, 3 = Diamonds in the dictionary
suitsDrawn = {"Spade": 0, "Club": 0, "Heart": 0, "Diamond": 0}
# numbers 0 = Ace, ..., 12 = King in the dictionary
numbersDrawn = {'Ace': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'Jack': 0, 'Queen': 0, 'King': 0}

deck = []
deckProb = []

# Deck Generator
while len(deck) < 52:
    card = numbers[random.randint(1,13)] + ' of ' + suits[random.randint(1,4)]

    if card not in deck:
        deck.append(card)

print(deck)
print("\nLength of deck: ", len(deck))

# Probability calculator
userDraw = int(input("\nEnter the number of cards to draw: "))
    
if userDraw <= 52 | userDraw >= 1:
    print("Here are your drawn cards: \n",)

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

# currently broken, update soon
    #Printing counted lists
    print("\nSuits:")
    for i in range(4):
        print("{}: {}".format(suits[i + 1], suitsDrawn[suits[i + 1]]))
    
    print("\nNumbers:")
    for i in range(13):
        print("{}: {}".format(numbers[i + 1], numbersDrawn[numbers[i + 1]]))

    #Printing calculations
    print("\nHere are the probabilities of the next card being a: \n")
    
    for i in range(4):
        probabilityOf(suitsDrawn[suits[i + 1]], userDraw, suits, i)
    
    print("\n")
    for i in range(13):
        probabilityOf(numbersDrawn[numbers[i + 1]], userDraw, numbers, i)
    
    # Calculating probabilities for the next card (2 attributes)
    for i in range(len(deck)):
        for key in numbersDrawn:
            if key in deck[i]:        
                deckProb.append(nextCardProb(numbersDrawn[key], userDraw))

    # Printing probabilities in deckProb
    print("\nProbabilities of the next card:")

    for i in range(len(deckProb)):
        print("{}s: {}%".format(deck[i], (deckProb[i]*100)))