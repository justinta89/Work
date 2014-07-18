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


def main():
    hand = []
    for i in range(5):
        hand.append(randomCard())
    print(hand)


if __name__ in ['__console__', '__main__']:
    main()