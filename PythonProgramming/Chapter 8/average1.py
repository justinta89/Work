# average1.py


def main():
    n = int(input("How many numbers do you have? "))
    sum = 0.0
    for i in range(n):
        x = float(input("Enter a number >> "))
        sum += x
    print("\nThe average of the numbers is {0}".format(sum / n))


if __name__ in ['__console__', '__main__']:
    main()