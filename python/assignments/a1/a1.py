# CPS109 - Assignment 1 - Nishil K.

"""
Game/Problem:
Mini-Blackjack - The objective of the game is to 'beat the dealer' and the aim of the game is to draw cards total 
value higher than the dealer and within 21. If it goes above 21, the player loses and if its exact 21 its known to 
be a 'blackjack'. There are different values of each cards: 2 through 10 count at face value i.e 2 counts as two and 10 as ten.
Face cards (j, k ,q) counts as 10, Ace or 1 are counted as 1 or 11 depending on the player and which helps the hand.
However, for simplicity, 1 will be counted as one only for this game. 

Algorithm/Procedure:
First, the cards will be dealt to the player 1 and whenever player 1 inputs 'hit' one random card will be dealt and added to your
total. After the player 1 is satisfied with their hand value (which should be under or equal to 21) he will input 'stand' which
locks their hand. However, if player 1's hand value exceedes 21, it's 'bust' and player will lose immediately and the
dealer wins. If the value is under and equals to 21, and player 1 has stood their hand, it will then move in to dealer's turn to
draw their cards and its their objective to draw cards higher than player 1. If they are unable to or get busted, they will lose.
This py program is one player game, where player 1 is the user and the dealer is the automated program which will also randomly draw
their cards depending on the player 1's hand value in order to win. 

Note: output.txt shows 3 arbitary game played and their output. 

-- To play the game, just run the program/py file --
"""

import random
import time

# ----------------------   UTILITY FUNCTIONS  ----------------------

# function to generate the cards deck
def generateDeck():
    global cards

    # [1...10, J...A] and * is used to spread/extend the list into its exisisting list.
    cards_number = [*list(range(2, 11)), "J", "Q", "K", "A"]
    card_suits = ["♥️", "♦️", "♣️", "♠️"]

    # nested loop to generate all possible permuation of cards for each suits and numbers.
    for n in cards_number:
        for f in card_suits:
            cards.append(str(str(n) + f))


# A reusable drawCard function, which randomly draws cards from the cards list and delete the value from the list
def drawCard():
    # global keyword is used to be able to manipulate a global variable.
    global cards

    # Randomly select a index from cards list
    c_i = random.randrange(0, len(cards))
    draw_card = cards[c_i]
    # Delete the value from the cards list; to avoid drawing the same card.
    del cards[c_i]
    return draw_card


# Function to calculate the total value based on the cards dealt.
def calculateTotal(cards):
    acc = 0
    for c in cards:
        # '10J' --> '10' , '9J' --> '9'
        c_n = c[:-2]
        if c_n == "J" or c_n == "Q" or c_n == "K":
            n = 10
        elif c_n == "A":
            n = 1
        elif int(c_n) > 0 and int(c_n) <= 10:
            n = int(c_n)

        acc += n

    return acc


# to avoid repetion of printing code during both player chances.
def printHand(player, player_cards, player_total, draw_card):
    print(f"{player} new card is: {draw_card}")
    print("Total: ", player_total)
    print(f"{player} cards: {player_cards}")


# -------------   GAME LOGIC  -------------


def blackjack():
    winner = ""

    # Player's Turn
    player_cards = []
    player_total = 0

    # Keep drawing the cards until the condition breaks the loops
    while True:
        i = input("\nh/hit or s/stand: ")

        # Hit
        if i == "h" or i == "hit":
            # Draw the card and add it to the player's card list and recalcalute the player hand value
            draw_card = drawCard()
            player_cards.append(draw_card)
            player_total = calculateTotal(player_cards)

            printHand("Your", player_cards, player_total, draw_card)

            # Bust Condition: if player total exceeds 21, they loses
            if player_total > 21:
                print("\nYou lose! ❌")
                winner = "Dealer!"
                return "\nWinner 🏆: " + winner
            # Blackjack condition: value equals 21.
            elif player_total == 21:
                print("\nBLACKJACK!")
                break

        # Stand: Player 1 decides to stop drawing cards
        elif i == "s" or i == "stand":
            print("You stand!", "Total: ", calculateTotal(player_cards))
            break

    # Dealer's Turn
    dealer_cards = []
    dealer_total = 0
    print("\nNow Dealer's chance\n-------------------\n")

    # Draws cards depending on the player 1 value in order to win.
    while True:
        # To slow down each loop and create a dramatic effect
        time.sleep(3)

        draw_card = drawCard()
        dealer_cards.append(draw_card)
        dealer_total = calculateTotal(dealer_cards)

        printHand("Dealer", dealer_cards, dealer_total, draw_card)
        print("\n")

        # Bust Condition
        if dealer_total > 21:
            print("\nYou win! 🥇")
            winner = "Player 1!"
            break
        # Dealer's Winning Condition
        elif dealer_total > player_total:
            print("\nYou lose! ❌")
            winner = "Dealer!"
            break
        # Tie Condition
        elif dealer_total == player_total:
            print("\nits a Tie! ❌")
            winner = "Tie!"
            break
        # If loop reaches till checking 21 that means player 1 also had blackjack.
        elif dealer_total == 21:
            print("\nBLACKJACK!")
            winner = "Tie!"
            break

    return "\nWinner 🏆: " + winner


if __name__ == "__main__":
    # global cards variable.
    cards = []
    generateDeck()
    print("Welcome to Blackjack!! 🃏\n--------------------")
    print(blackjack())
