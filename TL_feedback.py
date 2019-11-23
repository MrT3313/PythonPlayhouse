# -*- WELCOME -*- #
## INPUT
    # .csv exported from: dashboards.lambdaschool.com > Overview > Student Feedback 

## Print
    # Individual Feedback
    # avg rating

## Export 
    # standard excel file --> .xlsx
# --------------- #

# -*- SETUP -*- #
# IMPORTS
import csv

# CLASS
class Feedback:
    def __init__(self,student, writtenFeedback, grade):
        self.student = student 
        self.writtenFeedback = writtenFeedback
        self.grade = grade
    def __str__(self):
        output = f'-*- FEEDBACK CLASS -*-\n'
        output += f'Student: {self.student}  '
        output += f'Written Feedback: {self.writtenFeedback}  '
        output += f'TL Grade: {self.grade}  '

        return output

# VARIABLES
# feedback = []
# --------------- #

# -*- START -*- #
# 1 # Set user input prompt
userInputPrompt = f'Please enter the absolute file path for your downloaded .cvs \n'
userInputPrompt += f'Note: This can be found by dragging the file from your downloads and dropping it into your terminal\n'
userInputPrompt = f'Enter File Path Here:  '

userFile = input(userInputPrompt)
print('User Entered Absolute File Path: ',userFile, type(userFile))

def analyzeFeedback(feedback = []):
    with open(userFile,'r') as importedFile:
        reader = csv.reader(importedFile)
        next(reader)
        for entry in reader:
            entry_studentName = entry[2]                                        # Student Name
            entry_writtenFeedback = None if len(entry[6]) == 0 else entry[6]    # Written Feedback
            entry_grade = entry[7]                                              # Tl Grade

            newFeedback = Feedback(entry_studentName, entry_writtenFeedback, entry_grade)
            print(newFeedback)

            feedback.append(newFeedback)
    return feedback

# --------------- #

# -*- RUN FUNCTION -*- #
analyzeFeedback()
