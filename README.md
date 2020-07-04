I wondered "What does it look like for a deck of cards to be shuffled randomly...?"

This is basically a playground to do that 

I have a couple of ideas in mind, but the biggest ones are as follows

Where a "fair hand" is defined by a sequence of cards in which there are no 3 number of cards in a row in the deck or 3 of a kind or more

FUNCTIONS                                					DESCRIPTIONS
- cards = Deck()                             					This is how to instantiate a new deck of cards! (52 cards)
- cards.display()                            					This is the function used to display the cards
- cards.set_auto_display(<0 or 1>)           					This value will have the cards automatically display after some of the functions are called (1 for auto-display, 0 for non auto-display)
- cards.cut()                                					This function cuts the deck in half and switches the bottom half and the top half
- cards.shuffle()                            					This function does a standard shuffle (cuts the deck in 2 and then interlaces each of the cards)
- cards.random_shuffle()                      					This algorithm shuffles the cards using a random shuffle algorithm
- cards.move(<original card location>, <new card location>)                       This should take the card from the bottom of the deck (spot 51) and put it at the top of the deck (spot 0)
- cards.sequence(<number of players>,<number of cards dealt>)                     This will return True or False if you have 2 players being dealt 7 cards if they will have a 3 of a kind or a straight of 3 cards (one suite)
- cards.restore()                             					This will return the deck back to the original state

