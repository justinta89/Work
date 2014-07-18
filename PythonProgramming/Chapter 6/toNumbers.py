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

def main():
    strings = ["this is a string", "and another", "and one more"]

    print(toNumbers(strings))


main()