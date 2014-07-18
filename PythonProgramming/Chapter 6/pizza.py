import math


def area(r):
    # calculate area of a circle
    # A = 4 * pi * r ** 2
    A = 4 * math.pi * r ** 2
    return A


def pricePerInch(area, price):
    cost = price / area
    return cost


def main():
    # get the price per square inch of a pizza based on the area and price.
    # A = 4 * pi * r ** 2

    # get radius of pie from user
    size = int(input("Enter size of pizza: "))
    r = size / 2

    # get price of pizza from user
    price = float(input("Enter price of pizza: "))

    A = area(r)
    per_inch= pricePerInch(A, price)

    print(per_inch)


main()