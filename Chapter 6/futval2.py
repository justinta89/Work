# futval2.py

from graphics import *


def drawBar(window, year, height):
    bar = Rectangle(Point(year, 0), Point(year + 1, height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(window)


def createLabledWindow():
    # Create a graphics window with labels on left edge
    window = GraphWin("Investment Growth Chart", 320, 240)
    window.setBackground("white")
    window.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1, 0), ' 0.0K').draw(window)
    Text(Point(-1, 2500), ' 2.5k').draw(window)
    Text(Point(-1, 5000), ' 5.0k').draw(window)
    Text(Point(-1, 7500), ' 7.5k').draw(window)
    Text(Point(-1, 10000), '10.0k').draw(window)
    return window


def main():
    # Introduction
    print("This program plts the growth of a 10 year period")

    # Get principal and interest rate
    principal = int(input("Enter the initial principal: "))
    apr = float(input("Enter the annualized interest rate: "))

    win = createLabledWindow()
    drawBar(win, 0, principal)
    for year in range (1, 11):
        principal = principal * (1 + apr)
        drawBar(win, year, principal)

    input("Press <Enter> to quit.")
    win.close()


main()