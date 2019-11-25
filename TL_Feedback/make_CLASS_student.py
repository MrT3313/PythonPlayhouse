# IMPORTS
from __classes__ import Student

def makeStudents(uniqueStudentList, DataList_filteredColumns):
    # print(DataList_filteredColumns)
    newStudents = []
    for i in uniqueStudentList:
        # print(i)
        newStudent = Student(i)
        # print('NEW STUDENT: ',newStudent)

        newStudents.append(newStudent)
    # print(newStudents)
    return newStudents