# exam.py
from graphics import *


def main():
    # get the exam score
    score = int(input("Enter exam score: "))

    # check to see if the score is an A B C D or F
    letterGrade = [("A", 90), ("B", 80), ("C", 70), ("D", 60), ("F", 0)]

    for lg in letterGrade:
        if score >= lg[1]:
            grade = lg[0]
            break

    # return correct letter grade for score.
    print("The letter grade is: {0}".format(grade))


if __name__ in ['__console__', '__main__']:
    main()