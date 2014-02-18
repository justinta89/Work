# acronym.py


def main():
    # get user input of a phrase
    phrase = input("Enter a phrase: ")
    ph = phrase.upper()
    phSplit = ph.split()
    print(phSplit)

    acronym = []
    # get the first letter of each word
    for p in phSplit:
        letter = p[0]
        acronym.append(letter)

    # print new acronym
    fa = "".join(acronym)
    print("This is the new acronym: {0}".format(fa))


main()