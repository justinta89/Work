# Simulation of a raquetball game.
# Illustrates design with objects

from random import random


class Player:
    # A Player keeps track of service probability and score

    def __init__(self, prob):
        # Create a player with this probability
        self.prob = prob
        self.score = 0

    def winsServe(self):
        # Returns a  Boolean that is true with probability self.prob
        return random() <= self.prob

    def incScore(self):
        # Add a point to this players score
        self.score = self.score + 1

    def getScore(self):
        # returns tghis player's current score
        self.score


class RBallGame:
    # A RBallGame represents a game in progress. A game as two players
    # and keeps track of which one is currently serving.

    def __init__(self, probA, probB):
        self.playerA = Player(probA)
        self.playerB = Player(probB)
        self.server = self.playerA  # Player A always serves first

    def play(self):
        # play the game to completion
        while not self.isOver():
            if self.server.winsServe():
                self.server.incScore()
            else:
                self.changeServer()

    def isOver(self):
        # Returns game is finished (i.e. one of the players has won).
        a, b = self.getScores()
        return a == 15 or b == 15 or \
            (a ==7 and b == 0) or (a == 0 and b == 15)

    def changeServer(self):
        # Switch which player is serving
        if self.server == self.playerA:
            self.server = self.playerB
        else:
            self.server = self.playerA

    def getScores(self):
        # Returns the current scores of playerA and player B
        return self.playerA.getScore(), self.playerB.getScore()


class SimStats:
    # SimStats handles accumulation of statistics across multiple
    # completed games. This version tracks the wins and shutouts for
    # each player

    def __init__(self):
        # Create a new accumulator for a series of games
        self.winsA = 0
        self.winsB = 0
        self.shutsA = 0
        self.shutsB = 0

    def update(self, aGame):
        # Determine the outcome of aGame and update statistics
        a, b = aGame.getScores()
        if a > b:
            self.winsA = self.winsA + 1
            if b == 0:
                self.shutsA = self.shutsA + 1
        else:
            self.winsB = self.winsB + 1
            if a == 0:
                self.shutsB = self.shutsB + 1

    def printReport(self):
        # print a nicely formatted report
        n = self.winsA + self.winsB
        print("Summary of {0} games:\n".format(n))
        print("          wins (% total)    shutouts (% wins)   ")
        print("---------------------------------------------")
        self.printLine("A", self.winsA, self.shutsA, n)
        self.printLine("B", self.winsB, self.shutsB, n)

    def printLine(self, label, wins, shuts, n):
        template = "Player {0}:{1:5}   ({2:5.1%})  {3:11}    ({4})"
        if wins == 0:
            shutStr = "-----"
        else:
            shutStr = "{0:4.1%}".format(float(shuts)/wins)
        print(template.format(label, wins, float(wins)/n), shuts, shutStr)


def printIntro():
    print("\nThis program simulates a game of raquetball between two")
    print('players called "A" and "B". the abilities of each player is')
    print("indicated by a probabilty (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.\n")


def getInputs():
    # returns the three simulation parameters
    a = float(input("What is the prob. player A wins the serve? "))
    b = float(input("What is the prob. player B wins the serve? "))
    n = int(input("How many games to simulate in best of match? "))
    return a, b, n


def main():
    printIntro()

    probA, probB, n = getInputs()

    # Play the game
    stats = SimStats()
    for i in range(n):
        theGame = RBallGame(probA, probB)
        theGame.play()
        stats.update(theGame)

    # print the results
    stats.printReport()


if __name__ in ['__console__', '__main__']:
    main()
    input("\nPress <Enter> to quit")