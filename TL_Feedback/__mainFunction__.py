# IMPORTS
# 1 # Functions
from readCSV import open_and_read_CSV
from getColumns import getColumns
from getUnique import getUnique
from make_CLASS_student import makeStudents
from set_DateRestrictions import set_dateRestrictions
from implement_dateRestrictions import implement_dateRestrictions
from overall_TL_average import overall_TL_average
from append_Feedback_to_StudentCLASS import append_Feedback_to_StudentCLASS

# 1 # Get User's .csv Data
# 1.1 # Create Prompt
userInputPrompt = f'Please enter the absolute file path for your downloaded .cvs \n'
userInputPrompt += f'Note: This can be found by dragging the file from your downloads and dropping it into your terminal\n'
userInputPrompt += f'Enter File Path Here:  '

# 1.2 # Send Prompt
userFilePath = input(userInputPrompt).replace("\"", "")
print('User Entered Absolute File Path: ',userFilePath, type(userFilePath))

# 2 # Open & Read .csv Data --> returns List
userFile = open_and_read_CSV(userFilePath)
# print('__mainFunction__: userFile',userFile)
print('__mainFunction__: readCSV type == ', type(userFile), len(userFile))

# 3 # Filter For Specific Columns
userFile = getColumns(userFile)
print('__mainFunction__: Filtered UserFile type == ', type(userFile), len(userFile))

# 4 # Get Unique Students
uniqueStudents = getUnique(userFile)
print('__mainFunction__: Unique Students type == ', type(uniqueStudents), len(uniqueStudents))

# 5 # Create Students w/ CLASS: Student
uniqueStudents = makeStudents(uniqueStudents, userFile)
print('__mainFunction__: List of CLASS Students type == ', type(uniqueStudents), len(uniqueStudents))

# 6 # REPL => Update CLASS: Students startDate & endDate
uniqueStudents = set_dateRestrictions(uniqueStudents)
print('__mainFunction__: CLASS Students w/ Date Restrictions type == ', type(uniqueStudents), len(uniqueStudents))

# 7 # Filter userFile By Date Restrictions
userFile = implement_dateRestrictions(userFile, uniqueStudents)
print('__mainFunction__: Date Restricted UserFile type == ', type(userFile), len(userFile))

# 8 # Get Overall TL Average
overall_AVG_TLrating = overall_TL_average(userFile, uniqueStudents)
print('__mainFunction__: Date Restricted Overall TL Average type == ', type(overall_AVG_TLrating), overall_AVG_TLrating)

# 9 # Push Feedback To CLASS: Student
uniqueStudents = append_Feedback_to_StudentCLASS(userFile, uniqueStudents)
print('__mainFunction__: Completed CLASS: Student type == ', type(uniqueStudents), len(uniqueStudents))


for i in uniqueStudents:
    print(i)



