# wc.py
# This program will be similary to 'wc' in linux/unix systems.


def main():
    # Get a file name from user
    infileName = input("Enter the file name: ")

    # open file
    infile = open(infileName, "r")

    # count the number of lines, words, and characters in the file
    s = 0
    i = 0
    wl = 0
    # for loop to count number of lines
    for line in infile:
        line = line.split()
        s += 1
        # counts the number of words
        for l in line:
            wl += len(l)
            i += 1

    # print the lines, words, and characters in the file to user.
    print("Lines: {0} \nWords: {1} \nCharacters: {2}".format(s, i, wl))


main()