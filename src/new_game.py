import random

from src.deck import Deck
from src.hand import Hand

# Functions needed to create a new game

# Define the suits and values of cards in a standard pack

suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
values = [
    ("Ace", 1),
    ("Two", 2),
    ("Three", 3),
    ("Four", 4),
    ("Five", 5),
    ("Six", 6),
    ("Seven", 7),
    ("Eight", 8),
    ("Nine", 9),
    ("Ten", 10),
    ("Jack", 11),
    ("King", 12),
    ("Queen", 13)
]


# Function to create a deck of cards for playing the game
def create_playing_deck(number_of_packs):
    n = 0
    deck = []
    while n < number_of_packs:
        for suit in suits:
            for value in values:
                card = {"Suit": suit, "Name": value[0], "Value": value[1]}
                deck.append(card)
        n += 1
    return deck


# Function to shuffle a deck
def shuffle(initial_deck):
    shuffled_deck = Deck()
    number_of_cards = len(initial_deck)
    n = 1  # counter so add the same number of cards to the stack as their care cards in starting_deck
    while n <= number_of_cards:
        random_card = random.randrange(len(initial_deck))
        card = initial_deck[random_card]
        shuffled_deck.push(card)
        del initial_deck[random_card]
        n += 1
    del initial_deck
    return shuffled_deck


# Function to create a starting hand
def starting_hand(deck, hand_size=2):  # `hand_size` is here to facilitate game variations being added later
    hand = Hand()
    n = 1
    while n < hand_size:
        dealt_card = deck.pop()
        print("You were dealt the", dealt_card["Name"], "of", dealt_card["Suit"], ".")
        n += 1
    print("The total if your starting hand is", )
    return hand

