def overall_TL_average(userFile, uniqueStudents):
    # Set Variables
    totalSum = 0
    entries = len(userFile)

    # Calculate Total
    for i in userFile:
        # print(i[3])
        totalSum += int(i[3])

    # Calculate Overall Average
    calculated_AVG = totalSum / entries
    print(calculated_AVG)
    print(type(calculated_AVG))

    # Append Overall Avg To Individual Students
    for x in uniqueStudents:
        x.overall_avg_tlrating = round(calculated_AVG, 2)

    return calculated_AVG

