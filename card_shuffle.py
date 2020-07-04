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
        self._clean_deck = self.deck # TODO ==> Make this a private attribute
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
        self.deck = self._clean_deck
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

        
    def sequence(self, num_players, cards_per_player):
        # This is where we figure out if the cards are "fairly Shuffled"
        # We create a list of lists. The big list consists of the number of players
        # The other lists contain their cards
        # making a list of lists

        def is_fair(cards):
            # This is a helper function that will recieve a list of cards and will decyfer whether or not it is fair
            # Maybe if it's not fair it can then list out the hand 
            # Another feature to add would be that there are levels of fairness (maybe 2 cards in a row is fair or even 3, but any more than that is bad)
            def card_num_value(num):
                if 'J' in num:
                    return 11
                elif 'Q' in num:
                    return 12
                elif 'K' in num:
                    return 13
                elif 'A' in num:
                    return 14
                else:
                    return int(num)

            fair = True

            # ===================== If there are any cards in a row ==========================
            value = 0
            suite = ''
            in_a_row = 0
            for card in range(len(cards)):
                if card == 0:
                    suite = cards[card][-1]
                    value = card_num_value(cards[card][:-1])
                else:
                    temp_suite = cards[card][-1]
                    temp_value = card_num_value(cards[card][:-1])
                    if((int(temp_value) - int(value) == 1) and (temp_suite == suite)):
                        in_a_row += 1
                    else:
                        in_a_row = 0
                    value = temp_value
                    suite = temp_suite
                    if in_a_row == 2:
                        fair = False
            # ===================== If there are any three of a kinds ==========================           
            toak = []
            for card in cards:
                toak.append(card[:-1])
                toak.sort()
            for val in toak:
                if toak.count(val) > 2:
                    fair = False
            # ===================== Is the sequence fair? ==========================           
            if fair == True:
                print("The sequence is fair")
                return True
            else:
                print("The sequence is not fair")
                return False

        def value_system(e):
            enum = 0
            if 'J' in e:
                enum = 11
            elif 'Q' in e:
                enum = 12
            elif 'K' in e:
                enum = 13
            elif 'A' in e:
                enum = 14
            else:
                enum = int(e[:-1])
            if 'H' in e:
                return enum * 1
            elif 'S' in e:
                return enum * 15
            elif 'C' in e:
                return enum * 200
            else:
                return enum * 40000

        if (len(self.deck) % num_players != 0) or (len(self.deck) < (num_players * cards_per_player)):
            print("Deck is not able to be distributed evenly")
            exit()
        sequence = True
        for a in range(num_players):
            group = []
            count = 0
            for x in range(a, len(self.deck), num_players):
                if count == cards_per_player:
                    break
                else:
                    group.append(self.deck[x])
                    count += 1
            group.sort(key=value_system)
            print("Hand " + str(a) + ": " + str(group))
            if is_fair(group) == False:
                sequence = False
        return sequence
        self.show()

#=========================================================================================================================================================================
# CLASS DEFINITION IS DONE
#=========================================================================================================================================================================
