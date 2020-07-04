#!/usr/bin/python3

########################################################################################################
#
# Example Playground for the Deck class
#
########################################################################################################

# Need to grab the class from the file in the current folder
import sys
sys.path.append(".")
from card_shuffle import Deck
#############################


# FUNCTIONS #                               # DESCRIPTIONS #
cards = Deck()                              # This is how to instantiate a new deck of cards! (52 cards)
cards.display()                             # This is the function used to display the cards
cards.set_auto_display(1)                   # This value will have the cards automatically display after some of the functions are called (1 for auto-display, 0 for non auto-display)
cards.cut()                                 # This function cuts the deck in half and switches the bottom half and the top half
cards.shuffle()                             # This function does a standard shuffle (cuts the deck in 2 and then interlaces each of the cards)
cards.random_shuffle()                      # This algorithm shuffles the cards using a random shuffle algorithm
cards.move(51, 0)                           # This should take the card from the bottom of the deck (spot 51) and put it at the top of the deck (spot 0)
cards.sequence(2,7)                         # This will return True or False if you have 2 players being dealt 7 cards if they will have a 3 of a kind or a straight of 3 cards (one suite)
cards.restore()                             # This will return the deck back to the original state

### LET THE SHUFFLING BEGIN ###
cards.set_auto_display(0)
cards.shuffle()
for i in range(100): # Shuffling the deck 100 times
    cards.shuffle() 
cards.sequence(4,7)

cards.restore()

cards.set_auto_display(1)
for i in range(10):
    cards.move(51, 0) # This should take the card from the bottom of the deck and put it at the top of the deck
    cards.cut()

cards.set_auto_display(0)

cards.restore()

for i in range(100):
    cards.shuffle()
    cards.cut()

cards.display()

cards.random_shuffle()
cards.display()
cards.restore()

shuffle_counts = []
for num in range(100):
    cards.random_shuffle()
    shuffle_count = 0
    while not cards.sequence(2,9):
        cards.shuffle()
        shuffle_count += 1
        print("Shuffle Count ", shuffle_count)
    shuffle_counts.append(shuffle_count)
print(str(shuffle_counts))
