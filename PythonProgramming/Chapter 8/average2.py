# average2.py


def main():
    sum = 0.0
    count = 0
    xStr = input("Enter a numer (<Enter> to quit) >> ")
    while x >= 0:
        x = int(xStr)
        sum += x
        count += 1
        xStr = int(input("Enter a numer (<Enter> to quit) >> "))
    print("\nThe average of the numbers is {0}".format((sum / count)))


if __name__ in ['__console__', '__main__']:
    main()