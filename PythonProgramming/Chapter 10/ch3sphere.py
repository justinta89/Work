# ch3sphere.py

from sphere import Sphere


def getInputs():
    r = float(input("Enter the radius of a sphere: "))
    return r


def main():
    radius = getInputs()
    sphere = Sphere(radius)
    surface = sphere.surfaceArea()
    vol = sphere.volume()

    print("\nSurface Area: {0:0.3f} \nVolume: {1:0.3f}".format(surface, vol))


if __name__ in ['__console__', '__main__']:
    main()