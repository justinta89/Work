# rball.py
# Revision 1: Computes the results for best of n game matches.
#             First service alternates. Player A serves on odd matches,
#             Player B serves on even matches.

from random import random


def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)


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


def simNGames(n, probA, probB):
    # simulates n games of raquetball between palyers whose abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B

    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB, n)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB


def simOneGame(probA, probB, game):
    #Simulates a single game or  raquetball between players whose abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B

    # determines if game is even or odd game in best of match.
    # if game is odd, player A serves
    # if game is even, player B serves.
    if game / 2 != 0:
        serving = "A"
    else:
        serving = "B"

    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA, scoreB


def gameOver(a, b):
    # a and b represent scores for a raquetball game
    # returns True if the game is over, False otherwise
    return a == 15 or b == 15


def printSummary(winsA, winsB):
    # Prints a summary of wins for each player.
    n = winsA + winsB
    print("\nGames simulated: {0}".format(n))
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA / n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB / n))


if __name__ in ['__console__', '__main__']:
    main()