# program keeps track of conference attendees

# attendee class
#       - Name
#       - Company
#       - State
#       - Email address

# should be able to add new attendee, delete attendee, get info of attendee
# get name and email addresses of all attendees

# attendee list should be a file that is loaded when the program starts
from attendee import Attendee

def intro():
    # intro
    print("This program will open a file and allow the user to get")
    print("a list of all atendees for the conference.")
    print("It will show their full name, company, state, and email address.")
    print()

def getInputs():
    print("Below is your selection:")
    print("1: display atendee informataion")
    print("2: Add new atendee")
    print("3: Delete attendee")
    print("4: Get all email addresses")
    print("5: List all names and email addresses")
    print("-------------------------------------")

    selection = int(input("Enter your selection >> "))

    return selection


def openFile(fileName, option):
    f = open(fileName, option)


def attendeeInfo():
    """
    Outputs attendee information
    """

    f = open("alist", "r")
    for line in f:
        name, email, company, state = line.split(',')
        a = Attendee(name, email, company, state)
        info = a.getInfo()
        print(info)
    f.close()


def addNewAttendee(name, email, co, st):
    """
    Adds new attendee to the file
    """

    newfile = open("alist", "a")
    newattendee = "\r\n{0},{1},{2},{3}".format(name, email, co, st)
    newfile.write(newattendee)
    newfile.close()
    return None


def delAttendee(n):
    """
    Deletes specified attendee from list.
    """

    f = open("alist", "r")
    lines = f.readlines()
    f.close()
    f = open("alist", "w")
    for line in lines:
        name, email, company, state = line.split(',')
        if n != name:
            f.write("{0}, {1}, {2}, {3}".format(name, email, company, state))
    f.close()


def getEmails():
    """
    Returns the email addresses of all the attendees
    """

    f = open("alist", "r")
    print("Emails:")
    for line in f:
        name, email, company, state = line.split(',')
        a = Attendee(name, email, company, state)
        em = a.getEmail()
        print(em)
    f.close()


def nameAndEmail():
    """
    Returns the name and email address of every attendee
    """

    f = open("alist", "r")
    print("Name:                 Email:")
    print("-----------------------------------")
    for line in f:
        name, email, company, state = line.split(',')
        a = Attendee(name, email, company, state)
        em = a.getEmail()
        na = a.getName()
        print("{0:20} {1:20}".format(na, em))
    f.close()

def userChoice(num):
    """
    Returns correct information based on user input
    """

    if num == 1:
        return attendeeInfo()
    elif num == 2:
        name, email, co, st = input(
            "Enter the name, email, company, and state of new\
            attendee: ").split(',')
        return addNewAttendee(name, email, co, st)
    elif num == 3:
        name = input("Enter the name to delete: ")
        return delAttendee(name)
    elif num == 4:
        return getEmails()
    elif num == 5:
        return nameAndEmail()


def main():
    intro()
    choice = getInputs()
    userChoice(choice)


if __name__ in ['__console__', '__main__']:
    main()