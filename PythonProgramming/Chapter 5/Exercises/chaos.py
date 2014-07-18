# chaos.py
# A simple program illustratin chaotic behavior


def main():
    print("This program illustrates a chaotic function")
    x1 = float(input("Enter a number between 0 and 1: "))
    x2 = float(input("Enter another number between 0 and 1: "))

    print("Input     {0}          {1}".format(x1, x2))
    print("____________________________")
    for i in range(10):
        x1 = 3.9 * x1 * (1 - x1)
        x2 = 3.9 * x2 * (1 - x2)
        print("{0:2}      {1:0.5f}      {2:0.5f}".format(i + 1, x1, x2))


main()