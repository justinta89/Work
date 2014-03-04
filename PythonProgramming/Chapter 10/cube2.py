# cube2.py

from cube import Cube


def getInput():
    l = float(input("Enter side length >> "))
    return l


def main():
    sidel = getInput()
    cube = Cube(sidel)

    area = cube.surfaceArea()
    vol = cube.volume()

    print("Area: {0} \nVolume: {1}".format(area, vol))


if __name__ in ['__console__', '__main__']:
    main()