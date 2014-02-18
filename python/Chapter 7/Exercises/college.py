# college.py


def creditStandings(credits):
    # Students with < 7 credits are a freshman
    # Students with at least 7, but < 16 are a sophmore
    # credits < 16, but > 7 are junior
    # credits < 26 are seniors
    if credits < 7:
        year = "Freshman"
    elif credits > 7 and credits < 16:
        year = "Sophmore"
    elif credits > 16 and credits < 26:
        year = "Junior"
    else:
        year = "Senior"

    return year


def main():
    credits = int(input("Enter credit amount: "))
    standing = creditStandings(credits)

    print("Your standing: {0}".format(standing))


if __name__ in ['__console__', '__main__']:
    main()