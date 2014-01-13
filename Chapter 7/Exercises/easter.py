# easter.py


def easter(year):
    if year >= 1900 and year <= 2099:
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 *d + 5) % 7
        day = 22 + d + e
        if year == 1954 or year == 1981 or year == 2049 or year == 2076:
            day = day - 7
        if day > 31:
            day = day - 31
            date = "April {0}, {1}".format(day, year)
        else:
            date = "March {0}, {1}".format(day, year)

        return date


def main():
    year = int(input("Enter year: "))
    easter_date = easter(year)

    print(easter_date)


if __name__ in ['__console__', '__main__']:
    main()