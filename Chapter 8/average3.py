# average3.py


def main():
    fileName = input("What file are the numbers in? ")
    infile = open(fileName, 'r')
    sum = 0.0
    count = 0
    line = infile.readline()
    while line != "":
        sum = sum + int(line)
        count = count + 1
        line = infile.readline()
    print("\nThe average of the numbers is {0}".format(sum / count))


if __name__ in ['__console__', '__main__']:
    main()