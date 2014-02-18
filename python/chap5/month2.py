# month2.py
#       A program to print the month abbreviation, given it's number


def main():

    # months is a list used as a lookup table
    months = ["Jan", "Feb", "Mar", "Apr", "Jun", "Jul",
            "Aug", "Sep", "Oct", "Nov", "Dec"]

    n = int(input("Enter a month number (1 - 12): "))

    print("The month abbreviation is {0}.".format(months[n - 1]))


main()