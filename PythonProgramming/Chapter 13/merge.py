def merge(lst1, lst2, lst3):
    # merge sorted lists lst1, lst2, lst3

    # these indexes keep track of current position in each list
    i1, i2, i3 = 0, 0, 0
    n1, n2 = len(lst1), len(lst2)

    # loop while both lst1 and lst2 have more items
    while i1 < n1 and i2 < n2:
        if lst1[i1] < lst2[i2]:
            lst3[i3] = lst1[i1]
            i1 += 1
        else:
            lst3[i3] = lst2[i2]
            i2 += 1
        i3 += 1

    # Here either lst1 or lst2 is done. One of the following loops will
    # execute to finish up the merge.

    # copy remaining items (if any) from lst1
    while i1 < n1:
        lst3[i3] = lst[i1]
        i1 += 1
        i3 += 1
    # Copy remaining items (if any) from lst2
    while i2 < n2:
        lst3[i3] = lst2[i2]
        i2 += 1
        i3 += 1