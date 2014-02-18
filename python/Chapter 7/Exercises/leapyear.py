# leapyear.py
# calculates if a given year is a leap year


def leapyear(year):
    leap_century = year % 400
    leap = year % 4
    # test if year is centry year. year % 100 == 0
    century_year = year % 100
    if year % 100 == 0:
        century_year = year
        # if century_year % 400 == 0, the century_year a leap year.
        if century_year % 400 == 0:
            return "leap year"
        else:
            return "Not a leap year"
    else:
        # if year % 4 == 0 then the year is a leap year.
        if year % 4 == 0:
            return "leap year"
        else:
            return "Not a leap year"


def main():
    year = int(input("Enter a year: "))

    leap = leapyear(year)

    print(leap)


if __name__ in ['__console__', '__main__']:
    main()