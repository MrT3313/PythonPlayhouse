


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
            # print(overall_TL_Grade)

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
                print('THIS IS A NEW STUDENT YO HOMIE',newStudent)
                uniqueStudents.append(newStudent)
                print(len(uniqueStudents))

        # 3.4 # Setting Students Individual AVG TL Grades
        for i in uniqueStudents:
            i.get_student_AVG_rating()


    # for i in uniqueStudents:
    #     print('UNIQUE STUDENTS',i)

    # print('STUDENT 0',uniqueStudents[0])
    # print('STUDENT 5',uniqueStudents[5])
    print('OVERALL AVG TL GRADE',overall_TL_Grade)

    # 3.2 # Prompt for REPL
    prompt_REPL = f'Welcome to your student explorer REPL\n'
    prompt_REPL += f'Please choose a number between 0 & {len(uniqueStudents) - 1}'

    # 3.3 # Get Student Number From User
    userInput_REPL = input(prompt_REPL)
    print(userInput_REPL)

    # while True: 
    #     if 
# # --------------- #

# -*- RUN FUNCTION -*- #
analyzeFeedback()
