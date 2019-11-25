from datetime import datetime

def implement_dateRestrictions(fullList, uniqueStudents):
    print(len(fullList))
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
                # print(x)
                if x[1] == i.name:
                    print(x[1])
                    print(i.name)

                    
                    # Get and Split Date String
                    print(x[0])
                    # itemDate_split = x[0].split('/')
                    itemDate_split = x[0].split('-')
                    print('ITEM SPLIT',itemDate_split)

                    # Prepare Date Integers
                    # itemDate_year = int(itemDate_split[2])
                    # itemDate_month = int(itemDate_split[0])
                    # itemDate_day = int(itemDate_split[1])
                    itemDate_year = int(itemDate_split[0])
                    itemDate_month = int(itemDate_split[1])
                    itemDate_day = int(itemDate_split[2])

                    # Create Date Object
                    itemDate = datetime(
                        year=itemDate_year,
                        month=itemDate_month,
                        day=itemDate_day
                    )
                    print('NEW DATE OBJECT: itemDate',itemDate)
                    print('START DATE:', i.startDate)
                    print('END DATE',i.endDate)

                    print(itemDate <= i.endDate)
                    print(itemDate >= i.startDate)

                    # Date Conditional
                    if itemDate <= i.endDate and itemDate >= i.startDate:
                        print('PUSH THIS THROUGH')
                        # print(x)
                        listToReturn.append(x)

    print(len(listToReturn))
    return listToReturn