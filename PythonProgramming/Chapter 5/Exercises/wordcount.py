# wordcount.py
#   Counts the number of words in a given sentence.


def main():
    # Get a sentence from the user.
    sentence = input("Enter a sentence to count: ")

    # Split the words into substrings.
    words = sentence.split()

    # Count the number of words in the given sentence.
    i = 0
    for w in words:
        i = i + 1

    # return the number of words.
    print("There are {0} words in this sentence.".format(i))


main()
