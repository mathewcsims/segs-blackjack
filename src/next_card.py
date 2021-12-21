# Takes the next card from the top of a deck
# Returns either a card object (in the form of a dict), or 0 if there are no cards left in the deck

def next_card(deck):
    if deck.size() == 0:
        return 0
    else:
        return deck.pop()