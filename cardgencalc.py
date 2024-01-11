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

suit = {1:'Spade', 2:'Club', 3:'Heart', 4:'Diamond'}

num = {1:'Ace', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:'Jack', 12:'Queen', 13: 'King'}
stringToNum = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':11, 'Queen':12, 'King': 13}
deck = []
deckProb = []

# Deck Generator
while len(deck) < 52:
    card = num[random.randint(1,13)] + ' of ' + suit[random.randint(1,4)]

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

    # suits 0 = Spades, 1 = Clubs, 2 = Hearts, 3 = Diamonds in the list
    suitsDrawn = [0] * 4
    
    # numbers 0 = Ace, ..., 12 = King in the list
    numbersDrawn = [0] * 13

    # remove from deck and add to hand drawn queue style
    for i in range(userDraw):
        drawn.append(deck[0])
        deck.remove(drawn[i])  
        print(drawn[i]+"s")

        # counting
        # suits
        if "Spade" in drawn[i]:
            suitsDrawn[0] += 1
        elif "Club" in drawn[i]:
            suitsDrawn[1] += 1
        elif "Heart" in drawn[i]:
            suitsDrawn[2] += 1
        elif "Diamond" in drawn[i]:
            suitsDrawn[3] += 1

        # numbers
        if "Ace" in drawn[i]:
            numbersDrawn[0] += 1

        elif "2" in drawn[i]:
            numbersDrawn[1] += 1

        elif "3" in drawn[i]:
            numbersDrawn[2] += 1

        elif "4" in drawn[i]:
            numbersDrawn[3] += 1

        elif "5" in drawn[i]:
            numbersDrawn[4] += 1

        elif "6" in drawn[i]:
            numbersDrawn[5] += 1

        elif "7" in drawn[i]:
            numbersDrawn[6] += 1

        elif "8" in drawn[i]:
            numbersDrawn[7] += 1
            
        elif "9" in drawn[i]:
            numbersDrawn[8] += 1

        elif "10" in drawn[i]:
            numbersDrawn[9] += 1

        elif "Jack" in drawn[i]:
            numbersDrawn[10] += 1

        elif "Queen" in drawn[i]:
            numbersDrawn[11] += 1
            
        elif "King" in drawn[i]:
            numbersDrawn[12] += 1

    #Printing counted lists
    print("\nSuits:")
    for i in range(4):
        print("{}: {}".format(suit[i + 1], suitsDrawn[i]))
    
    print("\nNumbers:")
    for i in range(13):
        print("{}: {}".format(num[i + 1], numbersDrawn[i]))

    #Printing calculations
    print("\nHere are the probabilities of the next card being a: \n")
    
    for i in range(4):
        probabilityOf(suitsDrawn[i], userDraw, suit, i)
    
    print("\n")
    for i in range(13):
        probabilityOf(numbersDrawn[i], userDraw, num, i)
    
    # Calculating probabilities for the next card (2 attributes)
    for i in range(len(deck)):
        for key in stringToNum:
            if key in deck[i]:
                numbersDrawnPos = stringToNum[key] - 1
        
        deckProb.append(nextCardProb(numbersDrawn[numbersDrawnPos], userDraw))

    # Printing probabilities in deckProb
    print("\nProbabilities of the next card:")

    for i in range(len(deckProb)):
        print("{}s: {}%".format(deck[i], (deckProb[i]*100)))