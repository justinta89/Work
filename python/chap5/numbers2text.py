# number2text.py
#   A program to convert a sequence of Unicode numbers into a string of text.


def main():
    print("This program converts a sequence of Unicode numbers into")
    print("the string of text that it represents. \n")

    # Get the message to encode
    inString = input("Please enter the Unicode-encoded message: ")

    # loop through each substring and build Unicode message
    message = " "
    for numStr in inString.split():
        codeNum = int(numStr)
        message = message + chr(codeNum)

    print("\nThe decoded message is: {0}".format(message))

main()