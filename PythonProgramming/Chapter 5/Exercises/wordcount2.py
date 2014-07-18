# wordcount2.py
# Calculates the average word length of words in a sentence.


def main():
    # Get a sentence from the user.
    sentence = input("Enter a sentence to count: ")

    # Split the words into substrings.
    words = sentence.split()

    # Count the number of words in the given sentence.
    i = 0
    word_length = 0
    for w in words:
        word_length += len(w)
        i = i + 1

    avg_word = word_length / i

    # return the number of words.
    print("The average word length is {0}".format(avg_word))


main()
