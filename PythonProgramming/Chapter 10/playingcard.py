# playingcard.py


class PlayingCard:

    def __init__(self, rank, suit):
        """
        Rank is an int in the range 1 - 13 indicating the
        ranks Ace - King, and a suit is a single character
        "d", "c", "h", or "s" indicating the suit (diamonds,
        clubs, hearts, or spades).
        """
        self.rank = rank
        self.suit = suit
        self.card_name = ""
        self.card_ranks = ""
        self.card_bjvalues = 0

    def getRankName(self):
        """ Returns the rank name of the card. """
        ranks = {
            1: "Ace",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Jack",
            12: "Queen",
            13: "King"
            }
        self.card_ranks = ranks[self.rank]

        return self.card_ranks

    def BJValue(self):
        """ Returns the Black jack value of a card.
        Ace counts as 1, face cards count as 10 """
        values = {
            "Ace": 1,
            "Two": 2,
            "Three":3,
            "Four": 4,
            "Five": 5,
            "Six": 6,
            "Seven": 7,
            "Eight": 8,
            "Nine": 9,
            "Ten": 10,
            "Jack": 10,
            "Queen": 10,
            "King": 10
        }
        self.card_bjvalues = values[self.card_ranks]

        return self.card_bjvalues

    def getSuit(self):
        return self.suit

    def __str__(self):
        """ Returns string name of card. For example,
        "Ace of Spades". """
        card_name = "{0} of {1}".format(self.card_ranks, self.suit)

        return card_name