# -*- WELCOME -*- #
## INPUT
    # .csv exported from: dashboards.lambdaschool.com > Overview > Student Feedback 

## Print
    # [x] overall avg rating
    # [] Individual Students
        # 1. Name
        # 2. List of written feedback
        # 3. List of TL grades
        # 4. Avg TL grade from unique student

## Export 
    # standard excel file --> .xlsx
# --------------- #

# -*- SETUP -*- #
# IMPORTS
import csv

# CLASSES
# 1 # Feedback
class Feedback:
    def __init__(self, student, writtenFeedback, grade):
        self.student = student 
        self.writtenFeedback = writtenFeedback
        self.grade = grade
    def __str__(self):
        output = f'-*- FEEDBACK CLASS -*-\n'
        output += f'Student: {self.student}\n'
        output += f'Written Feedback: {self.writtenFeedback}\n'
        output += f'TL Grade: {self.grade}  '

        return output
    def __repr__(self):
        return str(self)

# 2 # Student
class Student:
    def __init__(self, name, studentFeedback = [], tl_ratings = []):
        self.name = name
        self.studentFeedback = studentFeedback
        self.tl_ratings = tl_ratings
    def __str__(self):
        output = f'-*- STUDENT CLASS -*-\n'
        output += f'Name: {self.name}\n'
        output += f'Student Feedback: {self.studentFeedback} \n {len(self.studentFeedback)} entries\n'
        output += f'TL Ratings: {self.tl_ratings} \n {len(self.tl_ratings)} entries'

        return output
    def __repr__(self):
        return str(self)

# --------------- #

# -*- START -*- #
# 1 # Set user input prompt
userInputPrompt = f'Please enter the absolute file path for your downloaded .cvs \n'
userInputPrompt += f'Note: This can be found by dragging the file from your downloads and dropping it into your terminal\n'
userInputPrompt += f'Enter File Path Here:  '

# 2 # Get absolute file path from user
userFile = input(userInputPrompt)
print('User Entered Absolute File Path: ',userFile, type(userFile))

# 3 # Analyze Feedback Function
def analyzeFeedback(feedback = [], uniqueStudents = []):

    # 3.1 # Open & Read User Imported File
    with open(userFile,'r') as importedFile:
        reader = csv.reader(importedFile)
        next(reader)

        # 3.1 # Fill Feedback Parameter
        for entry in reader:
            entry_studentName = entry[2]                                        # Student Name
            entry_writtenFeedback = None if len(entry[6]) == 0 else entry[6]    # Written Feedback
            entry_grade = entry[7]                                              # TL Grade

            # 3.1.2 # Create Individual Feedback CLASSes
            newFeedback = Feedback(entry_studentName, entry_writtenFeedback, entry_grade)
            # print(newFeedback)

            # 3.1.2 # Append Created Feedback CLASS to Feedback Parameter
            feedback.append(newFeedback)
            # print('FEEDBACK',feedback)


        # 3.2 # Overall Avg TL Grade
            # 3.2.1 # Sum Of All TL Grades
            count = 0
            for i in feedback:
                count += int(i.grade)
            # print('sum of all grades', count)
            # print('total number of observations', len(feedback))

            # 3.2.2 # Calculate Overall Average
            overall_TL_Grade = count / len(feedback) 
            print(overall_TL_Grade)

        # 3.3 # Fill unique students parameter
        for i in feedback:

            # 3.3.1 # Check For Unique Student Status
            if i.student not in uniqueStudents:

                # 3.3.1.1 # Set Unique Student Variables --> will be used w/ CLASS: Student
                list_of_grades = []
                list_of_studentFeedback = []

                # 3.3.1.2 # Iterate Through Feedback List & Fill Unique Lists
                for x in feedback:

                    # 3.3.1.2.1 # Check If Current Student In Feedback == Current Unique Student
                    if i.student == x.student:

                            # 3.3.1.2.1.1 # Append Unique Student Feedback & Grades To Unique Student Variables
                            list_of_studentFeedback.append(x.writtenFeedback)
                            list_of_grades.append(x.grade)
                        # else:
                        #     print('NOT A MATCH')
                    
                # 3.3.1.3 # Use Unique Student Name & Unique Student Variables To Make New Student & Append to Unique Students List
                newStudent = Student(i.student, list_of_studentFeedback, list_of_grades)
                uniqueStudents.append(newStudent)

    for i in uniqueStudents:
        print('UNIQUE STUDENTS',i)

    print('STUDENT 0',uniqueStudents[0])
    print('STUDENT 5',uniqueStudents[5])
    print('OVERALL AVG TL GRADE',overall_TL_Grade)

    # RETURN
    return overall_TL_Grade
# # --------------- #

# -*- RUN FUNCTION -*- #
analyzeFeedback()
