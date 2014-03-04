# gpasort.py
#   A program to sort student information into GPA order

from gpa import Student, makeStudent


def readStudents(filename):
    infile = open(filename, 'r')
    students = []
    for line in infile:
        students.append(makeStudent(line))
    infile.close()
    return students

def writeStudents(students, filename):
    outfile = open(filename, 'w')
    for s in students:
        print("{0}\t{1}\t{2}".format(s.getNam(), s.getHours(), s.getQPoints()) file = outfile)
    outfile.close()


def main():
    print("This program sorts student grade information by GPA.")
    filename = input("Enter the name of the data file: ")
    data = readStudents(filename)
    s = input("Enter the field to sort on: ")
    s.lower()

    if s == 'gpa':
        data.sort(key = Student.gpa)
    if s == 'name':
        data.sort(key = Student.getName)
    if s == 'credits':
        data.sort(key = Student.getQPoints)

    filename = input("Enter a name for the output file: ")
    writeStudents(data, filename)
    print("The data has been written to: {0}".format(filename))


if __name__ in ['__console__', '__main__']:
    main()