# exam.py
from graphics import *


def main():
    # open the exam score file
    infileName = input("Enter exam score file name: ")

    # create graphwin object
    win = GraphWin("Exam Scores", 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)

    # draw bar graph from data in exam score file

    # lable the bars with the corresponding last name from score file


"""
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
"""

main()
