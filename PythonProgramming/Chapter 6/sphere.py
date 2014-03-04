import math


def sphereArea(radius):
    # calculate the area of a sphere given the radius
    # A = 4 * pi * r ** 2
    A = 4 * math.pi * radius ** 2
    return A


def sphereVolume(radius):
    # calculate the voume of a sphere given the radius
    # V = 4 / 3 * pi * r ** 3
    V = 4 / 3 * math.pi * radius ** 3
    return V


def main():
    r = int(input("Enter radius: "))
    area = sphereArea(r)
    vol = sphereVolume(r)

    print("Area: {0:0.4f} \nVolume: {1:0.4f}".format(area, vol))


main()