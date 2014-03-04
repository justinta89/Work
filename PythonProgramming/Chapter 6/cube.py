def sumN(n):
    # returns the sum of the first n natural numbers
    total = 0
    for i in range(n):
        total += i + 1

    return total


def sumNCubes(n):
    # returns the sum of the cubes of the first n natrual numbers.
    total = 0
    for i in range(n):
        total = (n + 1) ** 3

    return total


def main():
    # get n from user
    n = int(input("Enter a number, n: "))
    sumn = sumN(n)
    sumncubes = sumNCubes(n)
    print("Sum of n natural numbers: {0} \n Sum of n natuarl numbers cubed: {1}".format(sumn, sumncubes))

main()