#!/usr/bin/python3

import random

# Deck of cards
class Deck:
    def __init__(self):
        self.clubs = ["2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC", "AC"]
        self.diamonds = ["2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD", "AD"]
        self.spades = ["2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS", "AS"]
        self.hearts = ["2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH", "AH"]
        self.deck = self.clubs + self.diamonds + self.spades + self.hearts
        self.clean_deck = self.deck # TODO ==> Make this a private attribute
        self.auto_display = 0

    def display(self):
        print("\n=============== Displaying the Deck ===============\n")
        for i in range(0, len(self.deck), 4):
            print(self.deck[i], self.deck[i+1], self.deck[i+2], self.deck[i+3])
            i = i + 4

    def show(self):
        if self.auto_display == 1:
            self.display()
        else:
            pass

    def set_auto_display(self, num):
        if num == 0:
            self.auto_display = 0
            print("Setting Auto-Display to 0")
        else:
            self.auto_display = 1
            print("\nSetting Auto-Display to 1")

    def shuffle(self):
        # Cut the deck and interweave the cards
        # This is in theory what a normal person would do to shuffle the cards
        thalf = self.deck[0:26]
        bhalf = self.deck[26:52]
        for x in range(0, len(self.deck), 2):
            self.deck[x] = thalf.pop(0)
            self.deck[x+1] = bhalf.pop(0)
        print("\n=============== Shuffling the Deck ===============\n")
        self.show()

    def random_shuffle(self):
        random.shuffle(self.deck)
        print("\n=============== Random Shuffling the Deck ===============\n")
        self.show()

    def restore(self):
        self.deck = self.clean_deck
        print("\n=============== Restoring Deck to original ===============\n")
        self.show()

    def cut(self):
        # This should split the deck into 2 and then put the bottom (26->51) on the top (0->25)
        thalf = self.deck[0:26]
        bhalf = self.deck[26:52]
        self.deck = bhalf + thalf
        print("\n=============== Cutting the Deck ===============\n")
        self.show()

    def move(self, org_spot, end_spot):
        # This will allow us to move cards around the deck
        # Top       -> 0
        # Bottom    -> 51
        pulled_card = self.deck.pop(org_spot)
        self.deck.insert(end_spot, pulled_card)
        print("\n=============== Moving card ===============\n")
        self.show()
    
    def sequence(self, num_players):
        # This is where we figure out if the cards are "fairly Shuffled"
        # We create a list of lists. The big list consists of the number of players
        # The other lists contain their cards
        pass # TODO ==> Placeholder for now

    def hand_sequence(self, num_players, cards_in_hand):
        # This is very similar to the sequence function except it is assumeing that only a certian number of cards are being distributed
        # into each person's hand
        pass # TODO ==> Place holder for now

    def is_fair(self, cards):
        # This is a helper function that will recieve a list of cards and will decyfer whether or not it is fair
        # Maybe if it's not fair it can then list out the hand 
        # Another feature to add would be that there are levels of fairness (maybe 2 cards in a row is fair or even 3, but any more than that is bad)
        pass # TODO ==> Place holder for now

#=========================================================================================================================================================================
# CLASS DEFINITION IS DONE
#=========================================================================================================================================================================

cards = Deck()
cards.display()
cards.set_auto_display(1)
cards.cut()
#cards.move(51, 0) # This should take the card from the bottom of the deck and put it at the top of the deck
#cards.random_shuffle()
cards.shuffle()
cards.set_auto_display(0)
for i in range(100): # Shuffling the deck 100 times
    cards.shuffle() 

cards.display()

cards.set_auto_display(1)

cards.restore()

cards.set_auto_display(0)

for i in range(10):
    cards.move(0, 51) # This should take the card from the bottom of the deck and put it at the top of the deck
    cards.cut()

cards.display()

cards.restore()
for i in range(100):
    cards.shuffle()
    cards.cut()

cards.display()
cards.restore()
cards.random_shuffle()
cards.display()
