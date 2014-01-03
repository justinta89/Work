# futval.py
# A program to copute the value of an investment
# carried 10 years into the future.


def main():
    print("This program calculates the future value")
    print("of a 10 year investment.")

    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annual interest rate: "))

    for i in range(10):
        principal = principal * (1 + apr)

    print("The value in 10 years is: {0}".format(principal))


main()