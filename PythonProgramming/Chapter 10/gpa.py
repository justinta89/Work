"""
gpa.py
    Program to find student with highest GPA
"""

class Student:

    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints / self.hours


def makeStudent(infoStr):
    # infoStr is a tab-separated line: name hours qpoints
    # returns a corresponding student object
    name, hours, qpoints = infoStr.split("\t")
    return Student(name, hours, qpoints)


def main():
    """
    Get the file name from the user
    Open the file for reading
    Set the best to be the first student
    for each student s in the file
        if s.gpa() > best.gpa()
            set best to s
    print out information about best
    """

    # Open the input file for reading
    filename = input("Enter the file name: ")
    infile = open(filename, "r")

    # set best to the record for the first student in the file
    best = makeStudent(infile.readline())

    #process subsequent lines of the file
    for line in infile:
        # turn the line into a student record
        s = makeStudent(line)
        # if this student has the best gpa so far, remember it
        if s.gpa() > best.gpa():
            best = s

    infile.close()

    #print information about the best student
    print("The best student is: {0}".format(best.getname()))
    print("Hours: {0}".format(best.getHours()))
    print("GPA: {0}".format(best.gpa()))


if __name__ in ['__console__', '__main__']:
    main()