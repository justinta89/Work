# randomWalk.py
from random import randrange
# Get a random number of steps from the user
# flip a coin to determine step. 1 for heads, 0 for tails.
#       heads = step forward
#       tails = step backward
# how many steps away from starting point are you, based on coin flips.


def main():
    printIntro()
    flip = getInputs()
    steps = randSteps(flip)
    distance(steps)

def printIntro():
    print("\nThis will take a given number of coin flips and, based on a coin")
    print("flips outcome, tell the user to take a step forward or backward.\n")


def getInputs():
    flips = int(input("Enter number of times to filp coin: "))
    return flips


def coinFlip():
    # Check to see if coin flip was 1 or 0
    # if the coin flip was 1, heads
    # if the coin flip was 0, tails
    rand = randrange(0, 2)
    if rand == 1:
        coin = "heads"
    else:
        coin = "tails"

    return coin


def randSteps(flips):
    # check what headsTails is set to.
    # if heads, move forward one step
    # if tails, move backward one step
    step = 0
    for f in range(flips):
        headsTails = coinFlip()
        if headsTails == "heads":
            step += 1
        else:
            step -= 1

    return step


def distance(steps):
    # returns how far the user has traveled after coin flilps
    dist = "You have traveled {0} steps away from the starting point.".format(steps)
    print(dist)


if __name__ in ['__console__', '__main__']:
    main()