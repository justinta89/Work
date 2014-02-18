# index.py
# should function like myList.index(x)


def index(myList, x):
    count = 0
    for l in myList:
        if x == l:
            return count
        count += 1


def main():
    myList = [1, 2, 3]
    x = 3
    print(index(myList, x))


if __name__ in ['__console__', '__main__']:
    main()