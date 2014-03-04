# numericvalue.py
# This is a program to calculate the numeric value of a given name.


def main():
    # Get name from user
    # make all lowercase
    name = input("Enter your name: ")
    name = name.lower()

    # split name into individual characters
    # Get numeric value of each char with ord()
    number = 0
    for n in name:
        if n == " ":
            number += 0
        else:
            number += ord(n) - 96
    print("The numeric value of your name is: {0}".format(number))


main()