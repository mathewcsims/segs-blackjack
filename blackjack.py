from src.create_cards import create
from src.deck import Deck
from src.hand import Hand
from src.next_card import next_card
import random
import sys


def play():
    # First job, create the cards (asking the user how many decks they would like to use).
    # At this point, I'm just creating a list of card objects (playing_deck).

    # Later, I will use more advanced data structures but a list allows me to easily shuffle the cards
    # using random.randrange(len(list) when it comes time to do the shuffling.

    try:
        number_of_decks = int(input("How many decks of cards would you like to play with?\n"))
        starting_deck = create(number_of_decks=number_of_decks)
    except ValueError:
        print("I don't think you entered a sensible answer. Try again, and next time use an integer.")
        sys.exit()

    print("\nPlaying deck created, now shuffling your cards.")

    # Second, give the cards a shuffle.
    # I'm going to store the shuffled packs, used cards, and player hand, as stacks (Miller and Ranum style)
    # This makes it easy for me to manage the cards using, e.g., push/pop methods

    number_of_cards = len(starting_deck)
    n = 1  # counter so add the same number of cards to the stack as their care cards in starting_deck

    shuffled_deck = Deck()  # create a Stack to hold the shuffled deck

    # We can use random.randrange() to choose a random card from the starting deck and push to the playing deck

    while n <= number_of_cards:
        random_card = random.randrange(len(starting_deck))
        card = starting_deck[random_card]
        shuffled_deck.push(card)
        del starting_deck[random_card]
        n += 1

    print("Cards shuffled.")
    print("There are", shuffled_deck.size(), "cards in your playing deck.\n")

    # Now, we need to deal the player a starting hand

    print("#### Game Start ####")
    print("The dealer will now deal you your first two cards.\n")

    # Create a Hand (subclass of Stack) to hold the players hand
    player_hand = Hand()

    # Create a function to add cards to player_hand
    def add_card(deck):
        initial_dealt_card = next_card(deck)
        if initial_dealt_card == 0:
            print("There are no cards in the deck, something went wrong. You can try again.")
            sys.exit()
        else:
            print("You were dealt the", initial_dealt_card["Name"], "of", initial_dealt_card["Suit"], ".")
            player_hand.push(initial_dealt_card)
            print("Your running total is:", player_hand.running_total(), "\n")

    # Deal the players initial hand of two cards
    add_card(shuffled_deck)
    add_card(shuffled_deck)

    # It is possible for the two cards initially dealt to a player to already total to more than 21
    # So, we need to add an if statement here to catch that scenario, and gracefully exit

    if player_hand.running_total() > 21:
        print("Oh no! Your hand already totals more than 21. Unlucky. You can try again though.")
        sys.exit()

    # Now loop through hit or stand until the player decides to stop, or hits 21.

    while True:
        print("Your current hand is:")
        for card in player_hand.list_cards():
            print(card)
        print("And your running total is", player_hand.running_total(), "\n")
        keep_playing = input("Would you like to hit or stand (enter 'h' or 's')?\n")
        if keep_playing == "s":
            print("Well played! Your final total is", player_hand.running_total())
            sys.exit()
        elif keep_playing == "h":
            dealt_card = next_card(shuffled_deck)
            if dealt_card == 0:
                print("There are no cards left, the game is over. Your final total was", player_hand.running_total())
                sys.exit()
            else:
                print("You were dealt the", dealt_card["Name"], "of", dealt_card["Suit"] + ".")
                player_hand.push(dealt_card)
                print("Your running total is:", player_hand.running_total(), "\n")
            if player_hand.running_total() > 21:
                print("Oh no! You went over 21, the game is over!")
                sys.exit()
            elif player_hand.running_total() == 21:
                print("CONGRATULATIONS! You scored 21 exactly!")
                sys.exit()


if __name__ == '__main__':
    play()
