def marching(num):
    print("The ants go marching {0} by {0} hurrah! hurrah!".format(num))


def verse(num, action, object):
    print("The ants go marching {0} by {0},".format(num))
    print("The little one stops to {0} his {1},".format(action, object))


def chorus():
    print("And they all go marching down...")
    print("In the ground...")
    print("To get out...")
    print("Of the rain.")
    print("Boom! Boom! Boom!")


def main():
    marching("one")
    marching("one")
    verse("one", "suck", "thumb")
    chorus()
    marching("two")
    marching("two")
    verse("two", "tie", "shoe")


main()