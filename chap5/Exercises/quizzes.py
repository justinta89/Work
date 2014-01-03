# quizzes.py
#   This program will take a user input quiz score 1 - 5, then output the appropriate grade.


def main():
    # Get grade from user
    grade = int(input("Enter grade (0 - 5): "))

    # check to see what letter the number matches.
    letters = ['F', 'F', 'D', 'C', 'B', 'A']
    letterGrade = letters[grade]

    # return the correct grade based on the given number.
    print("The letter grade is: {0}".format(letterGrade))


main()