def sumList(nums):
    # nums is a list of numbers. Returns the sum of the numbers in the list.
    total = 0
    for n in nums:
        total += n
    return total


def squareEach(nums):
    n = []
    for i in nums:
        n.append(i ** 2)

    return n


def toNumbers(strList):
    # strList is a list of strings, each of which represents a number.
    # Modifies each entry in the list by converting it to a number.

    num = []
    for s in strList:
        s.split()
        for w in s:
            w.split()
            for ch in w:
                num.append(ord(ch))

    return num


def squareSums():
    # prompt user for a file name.
    file_name = input("Enter the file name: ")
    # open file, read in lines
    infile = open(file_name, "r")
    for line in infile:
        l = infile.readline()
        num = toNumbers(l)
        square = squareEach(num)
        total = sumList(square)
        print(total)
    # convert characters to number
    # add all the numbers together
    # print out sum of the squares of the values in the file

squareSums()