# reverse.py
# same functionality as myList.reverse()

# INCOMPLETE

def reverse(myList):
    # take first item in list and save it to temp var
    # set last item to first spot.
    # decrement down through the list

    i = len(myList)
    j = 0
    for l in myList:
        temp = l
        temp2 = myList[i]
        myList[j] = temp2
        myList[i] = temp
        j += 1
        i -= 1

    return myList

def main():
    l = [1, 2, 3]
    print(reverse(l))

if __name__ in ['__console__', '__main__']:
    main()