### Card Guessing Game
## Authors: Benley Hsiang & Gia hue (Hayden) Mai

# Make a card deck generator

import random

# Description: Calculates the probability of rank/suit of the next card
def probabilityOf(typeDrawn, cardsDrawn, typeWant, storeIndex):
    remain = 52 - cardsDrawn
    
    # Calculating remaining number of cards with the same suit
    if len(typeWant) == 4:
        typeRemain = 13 - typeDrawn

    # Calculating remaining number of cards with the same rank
    elif len(typeWant) == 13:
        typeRemain = 4 - typeDrawn

    print("{}: {:.2f} %".format(typeWant[storeIndex+1], float((typeRemain/remain)*100)))

suit = {1:'Spade', 2:'Club', 3:'Heart', 4:'Diamond'}

# For Value to String retrieval using dictionary for generation
suits = {1:'Spade', 2:'Club', 3:'Heart', 4:'Diamond'}

numbers = {1:'Ace', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:'Jack', 12:'Queen', 13: 'King'}

# Dictionary for counting how many cards of a suit are drawn
# Accessing the type of suit using the dictionary `suits` above: 0 = Spades, 1 = Clubs, 2 = Hearts, 3 = Diamonds in the dictionary
suitsDrawn = {"Spade": 0, "Club": 0, "Heart": 0, "Diamond": 0}

# Dictionary for counting how many cards of a rank are drawn
# Accessing the type of number using the dictionary `numbers` above: 0 = Ace, ..., 12 = King in the dictionary
numbersDrawn = {'Ace': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'Jack': 0, 'Queen': 0, 'King': 0}

# Empty list to store a shuffled deck
deck = []

# This will draw from the deck first in first out
drawn = []

# Shuffled Deck Generator
while len(deck) < 52:
    # Generating a card with a random rank and random suit
    card = numbers[random.randint(1,13)] + ' of ' + suit[random.randint(1,4)]

    # Add the card to the deck if it's not already in the deck
    if card not in deck:
        deck.append(card)

print("\nFOR TESTING, DELETE PRINTED DECK LATER")
print(deck)
print("\nCard shuffling successful! Length of deck: ", len(deck))

print("""Welcome to the Card Guessing Game! 
----------------------------------------
You can draw any number of cards you'd like from the deck and then guess the next card using the presented probabilities.
      
You will be presented with 2 different probabilities:
- Probability of the next suit
- Probability of the next rank

The objective of this game is to correctly guess as many cards as possible:
- +10 points for correct guesses
- +5 points for any partially correct guesses
- 0 points for incorrect guesses

Have fun!
----------------------------------------""")

# Game loop

# Counter for tracking the high score
highScore = 0

# Boolean for replaying the game or not
gameRunning = 1

# Counter for number of cards drawn
totalDrawn = 0

# Counter for game score
score = 0

while gameRunning:
    
    # Check if this is the first time drawn
    if totalDrawn == 0:
        userDraw = int(input("\nEnter the number of cards to draw: "))
    # If this is not the first time, default to only 1 draw since we draw 1 card out per guess
    else:
        userDraw = 1

    # Increment counter for total cards drawn from the deck
    totalDrawn += userDraw

    if userDraw <= 52 | userDraw >= 1:
        print("Here are your drawn cards: \n",)        

        # Loop for drawing (removing) a card from the generated deck and adding it to the hand, in the style of a queue
        for i in range(userDraw):
            drawn.append(deck[0]) # Add the card from the deck to the hand
            deck.pop(0) # Remove that card from the deck

            card = drawn[i]
            number, suit = card.split(" of ")
            
            # Counting the number of...
            # Suits
            suitsDrawn[suit] += 1

            # Ranks
            numbersDrawn[number] += 1
        
        # Print out the drawn hand
        for i in range(totalDrawn):
            print(drawn[i] + "s")

        # Printing calculations
        print("\nHere are the probabilities of the next card being a:")
        
        # Suits
        for i in range(4):
            probabilityOf(suitsDrawn[suits[i + 1]], totalDrawn, suits, i)
        
        # Ranks 
        print("")
        for i in range(13):
            probabilityOf(numbersDrawn[numbers[i + 1]], totalDrawn, numbers, i)

    # Storing the player's guesses
    guess_suit = input("\nGuess the suit of the next card: ")
    guess_rank = input("Guess the rank of the next card: ")

    # Determining if the guess is correct or not:
    # If the suit and rank are guessed correctly
    if (guess_suit in deck[0]) and (guess_rank in deck[0]):
        print("\nCorrect!")
        print("The next card is the " + deck[0] + "s")
        print("\n+10 points")
        score += 10
        
    # If only the suit is guessed correctly
    elif guess_suit in deck[0]:
        print("\nCorrect suit, incorrect rank")
        print("The next card is the " + deck[0] + "s")
        print("\n+5 points")
        score += 5

    # If only the rank is guessed correctly
    elif guess_rank in deck[0]:
        print("\nCorrect rank, incorrect suit")
        print("The next card is the " + deck[0] + "s")
        print("\n+5 points")
        score += 5

    # If both are incorrectly guessed
    else:
        print("\nIncorrect.")
        print("The next card is the " + deck[0] + "s")

    print("Total Points: {}".format(score))
    print("------------------------------------------------------------")
    # If all the cards have been drawn from the deck, end the game
    if totalDrawn >= 51:
        gameRunning = 0


# End of game, printing results
print("\nGame Over!\nYour final score: {}".format(score))

#if score > highScore:
#    highScore = score

#print("\nHigh score: " + highScore)

#replay = input("\n\nPlay again? (Y/n): ")

#if replay == "n":
#    gameRunning = 0

#print("\n\n\n")       