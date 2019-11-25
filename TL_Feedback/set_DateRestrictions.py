from datetime import datetime

def set_dateRestrictions(uniqueStudents):
    '''
        This is a REPL where the user can update the CLASS: Student.startDate & Student.endDate 
        Attirbutes left at their defualt value of None will be set to datetime.now()
    '''

    while True:
        # 1 # Set Date Restrictions Initial Prompt
        initialPrompt = f'Did any of your students join your team party way through the program? '
        initialPrompt += f'Type "Y" for YES // Type "N" for NO // "Q" to QUIT the program  '
        
        # 2 # User Input
        userInput = input(initialPrompt)
        print(userInput)
        print(type(userInput))
        
        # 3 # User Selection Conditional
        # 3.1 #
        if userInput == "Q" or userInput == "q":
            exit()
        # 3.2 #
        elif userInput == "N" or userInput == "n":
            return uniqueStudents
        # 3.3 #
        elif userInput == "Y" or userInput == "y":
            while True: 
                # 3.3.1 # Print Available Students
                count = 0
                for i in uniqueStudents:
                    if count != len(uniqueStudents):
                        # print('THIS IS I',i)
                        # print('THIS IS TYPE',type(i))
                        # print(type(i.endDate))
                        # print(type(i.startDate))
                        
                        output = f''
                        if i.startDate is not None and i.endDate is not None:
                            # print('THIS IS PRINTING')
                            output += f'{count}: {i.name}\n'
                            output += f'    Start Date: {i.startDate}\n'
                            output += f'    End Date: {i.endDate}'
                            
                            print(output)
                        else:
                            # print('this is printing')
                            output += f'{count}: {i.name}'

                            print(output)
                    else:
                        break # Break out of FOR LOOP if count = length of list (out of bounds)
                    count += 1
                
                while True:
                    # 3.3.2 # Student Selection Prompt
                    studentSelection_prompt = f'Please enter the number of the student you with to add date restrictions to:\n' 
                    studentSelection_prompt += f'or "X" if you are finished adding date restrictions\n'
                    studentSelection_prompt += f'or "Q" to Quit the program:  '

                    studentSelection = input(studentSelection_prompt)
                    
                    if studentSelection == "Q" or studentSelection == "q":
                        exit()
                    elif studentSelection == "X" or studentSelection == "x":
                        result = True

                        # Check Dates
                        for index, value in enumerate(uniqueStudents, start=0):
                            # print(value.check_dates())
                            if value.check_dates() == False:
                                output = f'The start and end dates for {value.name} are out of order. Please Update the dates'
                                print(output)

                                print(type(index), index)
                                studentSelection = index
                                result = False

                                break

                        if result == True:
                            # Return     
                            print('All Dates are GOOD')
                            return uniqueStudents
                    else: 
                        # 3.3.3 # Try Catch For Value Error
                        try: 
                            studentSelection = int(studentSelection)
                            print(studentSelection)   

                            break 
                        except ValueError:    
                            print(f'Please enter a number between 1 & {len(uniqueStudents)}')

                # 3.3.4 # Set Start Date
                student_startDate = input(f"What is {uniqueStudents[studentSelection].name}'s Start Date? (Format: M/D/YYYY)  ")
                print(student_startDate)

                student_startDate_split = student_startDate.split('/')

                student_startDate_year = int(student_startDate_split[2])
                student_startDate_month = int(student_startDate_split[0])
                student_startDate_day = int(student_startDate_split[1])

                student_startDate = datetime(
                    year=student_startDate_year,
                    month=student_startDate_month,
                    day=student_startDate_day
                )
                print('NEW DATE OBJECT: student_startDate',student_startDate)

                uniqueStudents[studentSelection].startDate = student_startDate

                # 3.3.5 # Set End Date
                # Set Prompt
                student_endDate_prompt = f"What is {uniqueStudents[studentSelection].name}'s End Date? (Format: M/D/YYYY)\n" 
                student_endDate_prompt += f"If {uniqueStudents[studentSelection].name} is still currently your student press 'P':  "

                # Query User
                student_endDate = input(student_endDate_prompt)
                print(student_endDate)

                # End Date Conditional For Present Student
                if student_endDate == "P" or student_endDate == "p":
                    print("User Entered 'P' or 'p'")
                    
                    student_endDate = datetime.now()
                else: 
                    # Make New Date Object
                    student_endDate_split = student_endDate.split('/')

                    student_endDate_year = int(student_endDate_split[2])
                    student_endDate_month = int(student_endDate_split[0])
                    student_endDate_day = int(student_endDate_split[1])

                    student_endDate = datetime(
                        year=student_endDate_year,
                        month=student_endDate_month,
                        day=student_endDate_day
                    )
                print('NEW DATE OBJECT: student_endDate',student_endDate)

                # Update Selected User CLASS: Student
                uniqueStudents[studentSelection].endDate = student_endDate
        # 3.4 #
        else:
            print(f'User entry of {userInput} is not a menu option')