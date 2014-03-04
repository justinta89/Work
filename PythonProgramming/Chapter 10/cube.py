# cube.py


class Cube:

    def __init__(self, sidelength):
        self.sidelength = sidelength

    def sideLength(self):
        return self.sidelength

    def surfaceArea(self):
        self.surfaceArea = 6 * (self.sidelength ** 2)
        return self.surfaceArea

    def volume(self):
        self.volume = self.sidelength ** 3
        return self.volume