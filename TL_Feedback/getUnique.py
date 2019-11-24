# def getUnique(fullList, column, operator ,condition):
def getUnique(fullList):
    uniqueListToReturn = []

    for i in fullList:
        # print(i)
        if i[1] not in uniqueListToReturn:
            uniqueListToReturn.append(i[1])
    
    print(uniqueListToReturn)
    return uniqueListToReturn