def main():
    n = int(input("How many numbers are there? "))

    #set max to be the first value
    max = float(input("Enter a number >> "))

    # now compare the n-1 successive values
    for i in range(n - 1):
        x = float(input("Enter a number >> "))
        if x > max:
            max = x

    print("The largest value is {0}".format(max))


if __name__ in ['__console__', '__main__']:
    main()