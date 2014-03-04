def farm():
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")


def farmAnimal(animal, sound):
    print("And on the farm he had a {0}, Ee-igh, Ee-igh, Oh!".format(animal))
    print("With a {0}, {0} here and a {0}, {0} there".format(sound))
    print("Here a {0}, there a {0}, everywhere a {0}, {0}".format(sound))


def main():
    farm()
    farmAnimal("cow", "moo")
    farm()


main()