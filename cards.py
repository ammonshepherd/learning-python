# Exercise 12.2 A playing card consists of a suit ("Hearts", "Spades", "Clubs",
# "Diamonds") and a value (2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King",
# "Ace"). 
#
# Create a list of all possible playing cards, which is a deck. 
# Then create a function that shuffles the deck, producing a random order.

from random import randint

suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]

def cards(values, suits):
    cards = []
    for v in values:
        for s in suits:
            cards.append((v,s))
    return cards

def shuffle(cards):
    shuffled = []
    while len(cards) > 0:
        randIndex = randint(0, len(cards)-1)
        shuffled.append(cards.pop(randIndex))
    return shuffled

if __name__ == '__main__':
    print("The shuffled deck:")
    deck = cards(values, suits)
    sDeck = shuffle(deck)
    print(sDeck)
