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


# Define a function that will create a specified number of packs of cards
def create(number_of_decks=1):
    n = 0
    decks = []
    while n < number_of_decks:
        for suit in suits:
            for value in values:
                card = {"Suit": suit, "Name": value[0], "Value": value[1]}
                decks.append(card)
        n += 1
    return decks
