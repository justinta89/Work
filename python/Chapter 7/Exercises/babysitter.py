# babysitter.py
# A babysitter charges $2.50 an hour until 9:00pm when the rate drops to $1.75 an hour ( kids in bed). This program calculates the total bill based on start and end time (in a single 24 hour period). Partial hours are prorated.


def babysittingBill(startTime, endTime):
    nine = 9.0
    lower = 1.75
    regular = 2.50
    if endTime > nine:
        after_hours = endTime - nine
        reg_hours = nine - startTime
        bill = (after_hours * lower) + (reg_hours * regular)
    else:
        total_time = endTime - startTime
        bill = total_time * regular

    return bill


def main():
    start = float(input("Enter the start time: "))
    end = float(input("Enter the end time: "))

    bill = babysittingBill(start, end)

    print("The total bill is: {0}".format(bill))


if __name__ in ['__console__', '__main__']:
    main()