# hours.py
# Calculates the total wages for the week where hours worked and hourly rate are inputs. Any hours over 40 are time and a half


def wages(hours, rate):
    # check to see if hours are <= 40
    # check for hours > 40
    if hours > 40:
        # calculates how much hourly rate is after 40 hours
        extra_hours = hours - 40
        time_half_pay = (rate / 2) + rate
        timeHalf = extra_hours * time_half_pay
        # adds regular 40 hour pay to time and a half pay
        pay = float((rate * hours) + timeHalf)
    else:
        pay = float(rate * hours)

    return pay


def main():
    hours = float(input("How many hours were worked? "))
    rate = float(input("What is hourly rate? "))

    pay = wages(hours, rate)
    print("Your wages are: {0}".format(pay))


if __name__ in ['__console__', '__main__']:
    main()