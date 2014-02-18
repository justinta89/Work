# cards.py

from playingcard import PlayingCard
import random


def randomCard():
    # rolls a random int and returns the corresponding card rank and suit

    rcard_rank = random.randint(1, 13)
    suit = random.choice(['Diamonds', 'Clubs', 'Hearts', 'Spades'])

    pc = PlayingCard(rcard_rank, suit)
    c = pc.getRankName()
    card = pc.__str__()

    return card


def royalFlush(card_list):
    # take a card list as a parameter
    # compare each card's suit
    # compare each card value
    # if cardvalue in cardlist
    card_list.sort()
    spades = [
        'Ten of Spades',
        'Jack of Spades',
        'Queen of Spades',
        'King of Spades',
        'Ace of Spades' ]
    diamonds = [
        'Ten of Diamonds',
        'Jack of Diamonds',
        'Queen of Diamonds',
        'Kind of Diamonds',
        'Ace of Diamonds' ]
    hearts = [
        'Ten of Hearts',
        'Jack of Hearts',
        'Queen of Hearts',
        'Kind of Hearts',
        'Ace of Hearts' ]
    clubs = [
        'Ten of Clubs',
        'Jack of Clubs',
        'Queen of Clubs',
        'Kind of Clubs',
        'Ace of Clubs' ]

    rf_list = [spades, diamonds, hearts, clubs]
    if card_list in rf_list:
        return card_list
    else:
        return none


def pokerHand(card_list):
    # check to see what hand was given
    return none


def main():
    hand = []
    for i in range(5):
        hand.append(randomCard())

    rf = royalFlush(hand)
    print(hand)


if __name__ in ['__console__', '__main__']:
    main()