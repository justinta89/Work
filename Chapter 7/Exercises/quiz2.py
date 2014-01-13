# quizzes.py
#   This program will take a user input quiz score 1 - 5, then output the appropriate grade.


def main():
    # Get grade from user
    score = int(input("Enter grade (0 - 5): "))

    letters = ['F', 'F', 'D', 'C', 'B', 'A']
    # check to see what letter the number matches.
    if score >= 0 and score <= 5:
        letterGrade = letters[score]
        # return the correct grade based on the given number.
         print("Grade: {0}".format(letterGrade))
    else:
        print("\nYou need to enter a score between 0 and 5.")

if __name__ in ['__console__', '__main__']:
    main()