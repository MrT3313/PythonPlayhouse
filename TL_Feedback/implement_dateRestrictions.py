from datetime import datetime

def implement_dateRestrictions(fullList, uniqueStudents):
    listToReturn = []

    for i in uniqueStudents:
        # print(i)
        # print(i.startDate)
        # print(i.endDate)
        # print(i.startDate is None and i.endDate is None)
        if i.startDate is None and i.endDate is None:
            for z in fullList:
                if z[1] == i.name:
                    listToReturn.append(z)
        else:
            for x in fullList:
                if x[1] == i.name:
                    # Get and Split Date String
                    itemDate_split = x[0].split('/')

                    # Prepare Date Integers
                    itemDate_year = int(itemDate_split[2])
                    itemDate_month = int(itemDate_split[0])
                    itemDate_day = int(itemDate_split[1])

                    # Create Date Object
                    itemDate = datetime(
                        year=itemDate_year,
                        month=itemDate_month,
                        day=itemDate_day
                    )
                    # print('NEW DATE OBJECT: itemDate',itemDate)

                    # Date Conditional
                    if itemDate <= i.endDate and itemDate >= i.startDate:
                        # print('PUSH THIS THROUGH')
                        # print(x)
                        listToReturn.append(x)
    return listToReturn

def dateRestrictions_V1(fullList, students):
    restrictedList = fullList
    list_toReturn = []

    



    #             # Check for type conflict
    #             while True: 
    #                 # print(studentSelection)
    #                 # print(type(studentSelection))
    #                 # if studentSelection == "Q" or studentSelection == "q":
    #                 #     break

    #                 try:
    #                     studentSelection = int(studentSelection)
    #                     break
    #                 except ValueError:
    #                     # useInt_prompt = f'Please enter a number between 0 and ' & {len(students)-1}
    #                     studentSelection = input(f'Please enter a number between 0 and {len(students)}  ')

    #                 print("THIS LINE",studentSelection)
    #                 print(type(studentSelection))

    #             if studentSelection == "Q" or studentSelection == "q":
    #                 break
    #             elif studentSelection >= 0 and studentSelection < len(students):
                    
    #                 # Set Start Date
    #                 student_startDate = input(f"What is {students[studentSelection].name}'s Start Date? (Format: M/D/YY)  ")
    #                 print(student_startDate)

    #                 student_startDate_split = student_startDate.split('/')
    #                 print(student_startDate_split[0])
    #                 print(type(int(student_startDate_split[0])))

    #                 student_startDate_year = int(student_startDate_split[2])
    #                 # print('student_startDate_year', student_startDate_year)
    #                 student_startDate_month = int(student_startDate_split[0])
    #                 # print('student_startDate_month', student_startDate_month)
    #                 student_startDate_day = int(student_startDate_split[1])
    #                 # print('student_startDate_day', student_startDate_day)

    #                 student_startDate = datetime(
    #                     year=student_startDate_year,
    #                     month=student_startDate_month,
    #                     day=student_startDate_day
    #                 )
    #                 print('NEW DATE OBJECT: student_startDate',student_startDate)


    #                 # Set End Date
    #                 student_endDate_prompt = f"What is {students[studentSelection].name}'s End Date? (Format: M/D/YY)\n" 
    #                 student_endDate_prompt += f"If {students[studentSelection].name} is still currently your student press 'P':  "
    #                 student_endDate = input(student_endDate_prompt)
                    
    #                 print(student_endDate)
    #                 dateError = f'start and end dates are our of order'

    #                 if student_endDate == "P" or student_endDate == "p":
    #                     print("User Entered 'P' or 'p'")
                        
    #                     student_endDate = datetime.now()
    #                     print('NEW DATE OBJECT: student_endDate',student_endDate)

    #                     # break
    #                 else:
    #                     student_endDate_split = student_endDate.split('/')
    #                     print(student_startDate_split[0])
    #                     print(type(int(student_startDate_split[0])))

    #                     student_endDate_year = int(student_endDate_split[2])
    #                     # print('student_endDate_year', student_startDate_year)
    #                     student_endDate_month = int(student_endDate_split[0])
    #                     # print('student_endDate_month', student_startDate_month)
    #                     student_endDate_day = int(student_endDate_split[1])
    #                     # print('student_endDate_day', student_startDate_day)

    #                     student_endDate = datetime(
    #                         year=student_endDate_year,
    #                         month=student_endDate_month,
    #                         day=student_endDate_day
    #                     )
    #                     print('NEW DATE OBJECT: student_endDate',student_endDate)
    #                     # break

    #                 # Update Students Start & End Dates
    #                 for x in students:
    #                     if x.name == students[studentSelection].name:
    #                         x.startDate = student_startDate
    #                         x.endDate = student_endDate
    #                         print(x)


    #                 newStudentList = [
    #                     i for i in restrictedList if
    #                             i[1] == students[studentSelection].name 
    #                             and
    #                             datetime(
    #                                 year=int(i[0].split('/')[2]),
    #                                 month=int(i[0].split('/')[0]),
    #                                 day=int(i[0].split('/')[1])
    #                             ) >= students[studentSelection].startDate 
    #                             and 
    #                             datetime(
    #                                 year=int(i[0].split('/')[2]),
    #                                 month=int(i[0].split('/')[0]),
    #                                 day=int(i[0].split('/')[1])
    #                             ) <= students[studentSelection].endDate
    #                 ]
    #                 print(newStudentList)
    #                 print(len(newStudentList))

    #                 exSelectedStudent = [
    #                     i for i in restrictedList if i[1] != students[studentSelection].name
    #                 ]
    #                 print(exSelectedStudent)
    #                 print(len(exSelectedStudent))

    #                 restrictedList = exSelectedStudent + newStudentList
    #                 print(restrictedList)
    #                 print(len(restrictedList))
    #                 # for item in restrictedList:

    # print('FINAL RETURN',list_toReturn)
    # # return list_toReturn