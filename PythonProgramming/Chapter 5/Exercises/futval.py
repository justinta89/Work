# futval.py
# A program to copute the value of an investment
# carried 10 years into the future.


def main():
    print("This program calculates the future value")
    print("of a 10 year investment.")

    """
    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annual interest rate: "))

    print("Year       Value")
    print("________________")
    for i in range(10):
        principal = principal * (1 + apr)
        print("{0:2}       ${1:0.2f}".format(i, principal))
    """

    infileName = input("Enter the file name: ")
    outfileName = input("Enter the destination file name: ")

    infile = open(infileName, "r")
    outfile = open(outfileName, "w")

    for line in infile:
        principal = principal * (1 + apr)
        print(principal, file=outfile)

    infile.close()
    outfile.close()

    print("The principal projections have been written to: {0}".format(oufileName))

main()