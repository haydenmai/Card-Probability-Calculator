### Card Guessing Game
## Authors: Benley Hsiang & Gia hue (Hayden) Mai

import random

# Description: Calculates the probability of rank/suit of the next card
def probabilityOf(typeDrawn, cardsDrawn, storeIndex, suitOrRank):
    totalRemain = 52 - cardsDrawn
    
    # Calculating remaining number of cards with the same suit
    if len(suitOrRank) == 4:
        typeRemain = 13 - typeDrawn

    # Calculating remaining number of cards with the same rank
    elif len(suitOrRank) == 13:
        typeRemain = 4 - typeDrawn

    print("{:<8} {:>10.2f} %".format(suitOrRank[storeIndex+1], float((typeRemain/totalRemain)*100)))

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

# List representing the hand of cards drawn from the deck
drawn = []

# Shuffled Deck Generator
while len(deck) < 52:
    # Generating a card with a random rank and random suit
    card = numbers[random.randint(1,13)] + ' of ' + suit[random.randint(1,4)]

    # Add the card to the deck if it's not already in the deck
    if card not in deck:
        deck.append(card)

print("\n\nFOR TESTING, DELETE LATER\n")
print(deck)
print("\nCard shuffling successful! Length of deck: ", len(deck))
print("FOR TESTING, DELETE LATER\n\n")

print("""Welcome to the Card Guessing Game! 
----------------------------------------
You can draw any number of cards you'd like from the deck and then guess the next card using the presented probabilities.
      
You will be presented with 2 different probabilities:
-> Probability of the next suit
-> Probability of the next rank

The objective of this game is to correctly guess as many cards as possible:
-> +10 points for correct guesses
-> +5 points for any partially correct guesses
-> +0 points for incorrect guesses

Have fun!
----------------------------------------""")

# Game loop

# Boolean for replaying the game or not
gameRunning = 1

# Counter for number of cards drawn
totalDrawn = 0

# Counter for game score
score = 0

while gameRunning:
    
    # Check if this is the first time drawn
    if totalDrawn == 0:
        
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


    # If this is not the first time, default to only 1 draw since we draw 1 card out per guess
    else:
        userDraw = 1

    # Increment counter for total cards drawn from the deck
    totalDrawn += userDraw

    print("Here are your drawn cards: \n",)        

    # Loop for drawing (removing) a card from the generated deck and adding it to the hand, in the style of a queue
    for i in range(userDraw):
        drawn.append(deck[0]) # Add the card from the deck to the hand
        deck.pop(0) # Remove that card from the deck

        # Takes the string representing a card and splits the string into its suit and rank
        # If it's the very first guess, i.e. when totalDrawn == initial number of cards specified by user
        if totalDrawn == userDraw:
            card = drawn[i] # Take card i from the drawn hand 

        # If it's not the very first guess, i.e. the number of cards to draw will always be 1
        else:  
            card = drawn[totalDrawn - 1] # Take the last card of the drawn hand, i.e. the card we just drew after guessing

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
    
    # Ranks 
    for i in range(13):
        probabilityOf(numbersDrawn[numbers[i + 1]], totalDrawn, i, numbers)
        
    # Suit
    print("")
    for i in range(4):
        probabilityOf(suitsDrawn[suits[i + 1]], totalDrawn, i, suits)

    # Booleans to check if the user input is valid
    validSuitInput = 0
    validRankInput = 0

    # Show score and number of cards remaining for every guess
    print("")    
    print("Total Points: {}".format(score))
    print("Cards remaining: {}".format(len(deck)))

    # Taking user input
    while validRankInput == 0:
        guess_rank = input("Guess the rank of the next card: ")
        guess_rank = guess_rank.capitalize().rstrip(" ") # Capitalize and remove white spaces
        
        # Checking for valid input
        if guess_rank in numbersDrawn:
            validRankInput = 1
        else:
            print("Invalid input, please try again")

    while validSuitInput == 0:
        guess_suit = input("Guess the suit of the next card: ") # Capitalize, remove white spaces and s
        guess_suit = guess_suit.capitalize().rstrip("s ")

        # Checking for valid input
        if guess_suit in suitsDrawn:
            validSuitInput = 1
        else:
            print("Invalid input, please try again")

    # Determining if the guess is correct or not:
    # If the suit and rank are guessed correctly
    if (guess_suit in deck[0]) and (guess_rank in deck[0]):
        print("\nCorrect!")
        print("+10 points")
        score += 10
        
    # If only the suit is guessed correctly
    elif guess_suit in deck[0]:
        print("\nCorrect suit, incorrect rank")
        print("+5 points")
        score += 5

    # If only the rank is guessed correctly
    elif guess_rank in deck[0]:
        print("\nCorrect rank, incorrect suit")
        print("+5 points")
        score += 5

    # If both are incorrectly guessed
    else:
        print("\nIncorrect.")

    print("The next card is the " + deck[0] + "s")
    print("\n------------------------------------------------------------\n")
    
    # If all the cards have been drawn from the deck, end the game
    if totalDrawn >= 51:
        gameRunning = 0


# End of game, printing results
print("Game Over!\nYour final score: {}".format(score))

# END OF CODE   