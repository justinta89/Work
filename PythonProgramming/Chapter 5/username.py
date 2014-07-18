# username.py
#       Simple string processing program to generate usernames


def main():
    print("This program generates computer usernames.\n")

    # get users first and last name
    first = input("Please enter your first name (all lowercase): ")
    last = input("Please enter your last name (all lowercase): ")

    # concatenate first initial with 7 chars of last name
    uname = first[0] + last[:7]

    # output username
    print("Your username is: {0}".format(uname))


main()