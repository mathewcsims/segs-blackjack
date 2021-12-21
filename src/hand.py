from src.stack import Stack


class Hand(Stack):
    def __init__(self):
        super().__init__()

    def running_total(self):
        total = 0
        for card in self.items:
            total += card["Value"]
        return total

    def list_cards(self):
        cards = []
        for card in self.items:
            card_string = card["Name"] + " of " + card["Suit"]
            cards.append(card_string)
        return cards
