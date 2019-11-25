def append_Feedback_to_StudentCLASS(userFile, uniqueStudents):
    for i in uniqueStudents:
        print(i)

        for x in userFile:
            # print(i.name)
            # print(x[1])
            if x[1] == i.name:
                print('found')
                print(x)
                i.studentFeedback.append(x[2])
                i.tl_ratings.append(x[3])

    return uniqueStudents

