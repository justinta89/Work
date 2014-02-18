# isin.py
# functions like 'x in myList'


def isin(myList, x):

    for l in myList:
        if x == l:
            a = True

    return a


def main():
    myList = [1, 2, 3]
    x = 1
    print(isin(myList, x))


if __name__ in ['__console__', '__main__']:
    main()