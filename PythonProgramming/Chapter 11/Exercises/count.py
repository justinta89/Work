# count.py
"""
Should have the same functionality as myList.count(x)
usability:
    count(myList, x)
"""


def count(myList, x):
    """
    Returns the number of times x appears in a list

    Take a list and a number as input
    Check to see how many times 'x' is in the list
        for l in myList:
            if x == l:
                num += 1
    Return the number of times x appeared.
    """
    num = 0
    for l in myList:
        if x == l:
            num += 1
    return num

def main():
    list = [1, 2, 3, 1, 1, 2]
    l = 3
    print(count(list, l))


if __name__ in ['__console__', '__main__']:
    main()