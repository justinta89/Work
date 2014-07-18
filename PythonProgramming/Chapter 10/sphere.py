# sphere.py
# Class to represent the geometric solid sphere.
import math


class Sphere:

    def __init__(self, radius):
        """ Creates a sphere having the given radius """
        self.radius = radius

    def getRadius(self):
        return self.radius

    def surfaceArea(self):
        """ Determines the Surface Area of a sphere """
        self.surfaceArea = 4 * math.pi * (self.radius ** 2)
        return self.surfaceArea

    def volume(self):
        """ Determines the volume of a sphere """
        self.volume = (4 / 3) * math.pi * (self.radius ** 3)
        return self.volume