import src.new_game as new_game
import sys


def play():

    print("\n##########")
    print("Welcome to BlackJack!")
    print("##########")
    print("\nThe game will now create a deck of cards for you to play with.\n")

    # PLACEHOLDER -- if I wanted to create a menu allowing variations of the game to be played, it would go here
    # In the meantime, I will set some global variables here which could be altered using user input
    target = 21
    number_of_packs = 1

    # Create a shuffled Deck to play the game with and store as `deck`
    deck = new_game.shuffle(new_game.create_playing_deck(number_of_packs=number_of_packs))

    print("Your cards hae been created, and shuffled, for you.")
    print("There are", deck.size(), "cards in your playing deck.\n")

    # Now, we need to start the game and deal the player a starting hand
    print("#### Game Start ####")
    print("The dealer will now deal you your first two cards.\n")

    # Create a Hand (subclass of Stack) to hold the players hand
    player_hand = new_game.starting_hand(deck)

    # It is possible for the two cards initially dealt to a player to already total to more than 21
    # So, we need to add an if statement here to catch that scenario, and gracefully exit
    # Not forgetting this also means the player could win right away, so let's catch that too

    if player_hand.running_total() > target:
        print("Oh no! Your hand already totals more than 21. Unlucky. You can try again though.")
        sys.exit()
    elif player_hand.running_total() == target:
        print("CONGRATULATIONS! You scored 21 exactly!")
        sys.exit()

    # Now loop through hit or stand until the player decides to stop, or hits 21.
    # This is the 'game logic' - different versions of this could be created for different variations
    # If more variations of the game were created, it would make sense to separate this into some module

    while True:
        print("\n\nLet's start playing!")
        print("Your current hand is:")
        for card in player_hand.list_cards():
            print(" - " + card)
        print("And your running total is", player_hand.running_total(), "\n")
        keep_playing = input("Would you like to hit or stand (enter 'h' or 's')?\n")
        if keep_playing == "s":
            print("Well played! Your final total is", player_hand.running_total())
            sys.exit()
        elif keep_playing == "h":
            dealt_card = deck.pop()
            print("You were dealt the", dealt_card["Name"], "of", dealt_card["Suit"] + ".")
            player_hand.push(dealt_card)
            print("Your running total is:", player_hand.running_total(), "\n")
        if player_hand.running_total() > target:
            print("Oh no! You went over 21, the game is over!")
            sys.exit()
        elif player_hand.running_total() == target:
            print("CONGRATULATIONS! You scored 21 exactly!")
            sys.exit()


if __name__ == '__main__':
    play()
