#investdouble.py


def investdouble(interest, initial):
    # use a while loop to determin how long it will take for initial investment to double

    # formula to find when interest has doubled:
    # A = Pe^rt where A = end amount, P = principal, r = rate, t = time
    # A / P = 2, because the money should double
    # e^rt = 2
    # ln(e^rt) = ln(2)
    # rt * ln(e) = ln(2)
    # since ln(e) = 1:
    # rt = ln(2)
    # find t, mult both sides by 1/r
    # t = ln(2)/r
    # substitude rate value for r to get t

    principal = 0
    i = 0
    while initial % principal != 2:
        principal = (initial * interest) + principal
        print(principal / initial)
        if principal / initial == 2:
            return i
            break
        i += 1


def main():
    rate = float(input("Enter interest rate: "))
    investment = float(input("Enter initial investment: "))
    double = investdouble(rate, investment)
    print("It took {0} days for your investment to double.".format(double))


if __name__ in ['__console__', '__main__']:
    main()